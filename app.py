from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from pygments.styles import get_all_styles
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///snippets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class CodeSnippet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    code = db.Column(db.Text, nullable=False)
    language = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'code': self.code,
            'language': self.language,
            'category': self.category,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/snippets', methods=['GET'])
def get_snippets():
    snippets = CodeSnippet.query.order_by(CodeSnippet.created_at.desc()).all()
    return jsonify([snippet.to_dict() for snippet in snippets])

@app.route('/api/snippets', methods=['POST'])
def create_snippet():
    data = request.json
    snippet = CodeSnippet(
        title=data['title'],
        code=data['code'],
        language=data['language'],
        category=data['category']
    )
    db.session.add(snippet)
    db.session.commit()
    return jsonify(snippet.to_dict()), 201

@app.route('/api/snippets/search', methods=['GET'])
def search_snippets():
    query = request.args.get('q', '').lower()
    category = request.args.get('category', '')
    language = request.args.get('language', '')
    
    snippets = CodeSnippet.query
    
    if query:
        snippets = snippets.filter(db.or_(
            CodeSnippet.title.ilike(f'%{query}%'),
            CodeSnippet.code.ilike(f'%{query}%')
        ))
    if category:
        snippets = snippets.filter(CodeSnippet.category == category)
    if language:
        snippets = snippets.filter(CodeSnippet.language == language)
        
    snippets = snippets.order_by(CodeSnippet.created_at.desc()).all()
    return jsonify([snippet.to_dict() for snippet in snippets])

@app.route('/api/themes', methods=['GET'])
def get_themes():
    # Get all available Pygments styles
    themes = list(get_all_styles())
    return jsonify(themes)

@app.route('/api/highlight', methods=['POST'])
def highlight_code():
    data = request.json
    code = data['code']
    language = data['language']
    theme = data.get('theme', 'monokai')  # Default to monokai if no theme specified
    
    try:
        lexer = get_lexer_by_name(language, stripall=True)
        formatter = HtmlFormatter(style=theme)
        highlighted = highlight(code, lexer, formatter)
        return jsonify({
            'highlighted_code': highlighted,
            'css': formatter.get_style_defs()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

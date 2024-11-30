# Code Snippet Manager

A web application for developers to save, categorize, and search their code snippets with syntax highlighting support for multiple programming languages.

## Features

- Save code snippets with titles and categories
- Syntax highlighting for multiple programming languages
- Search snippets by title, content, category, or language
- Clean and responsive user interface
- Real-time syntax highlighting preview

## Supported Languages

- Python
- JavaScript
- TypeScript
- HTML
- CSS
- Java
- C++
- C#
- PHP
- Ruby
- Swift
- Go
- Rust
- Kotlin
- Dart
- SQL
- Shell Script
- YAML
- JSON
- Markdown
- XML

And more (easily extensible through Pygments)

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and navigate to `http://localhost:5000`

## Usage

1. **Adding a Snippet**:
   - Fill in the snippet title
   - Select the programming language
   - (Optional) Add a category
   - Paste your code
   - Click "Save Snippet"

2. **Searching Snippets**:
   - Use the search bar to find snippets by title or content
   - Filter by category or language using the dropdown menus
   - Results update in real-time as you type

## Technologies Used

- Backend: Flask
- Database: SQLite with SQLAlchemy
- Frontend: HTML, JavaScript, Tailwind CSS
- Syntax Highlighting: Pygments

## Credits

This project was developed using [Windsurf](https://www.codeium.com/windsurf), the world's first agentic IDE that revolutionizes how developers write and maintain code. Windsurf is a product by Codeium, providing intelligent coding assistance and project management capabilities.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

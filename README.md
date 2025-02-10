# Invoice Data Extractor

A streamlined application for processing and extracting data from PDF invoices using Large Language Models.

## 🌟 Features

- PDF invoice processing and data extraction
- Streamlit-based user interface
- LLM-powered information extraction
- JSON output format
- Easy-to-use file upload system
- Supports electric car charging invoices

## 🛠️ Technologies

- Python 3.10
- Streamlit
- Langchain
- Ollama (LLM)
- Poetry (Package Management)

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- pip or Poetry

### Installation

1. Clone the repository:
```bash
git clone [your-repository-url]
cd [repository-name]
```

2. Set up the Python environment:

Using pip:
```bash
pip install -r requirements.txt
```

OR using Poetry:
```bash
# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Install dependencies
poetry install
```

3. Run the application:
```bash
# Using pip
PYTHONPATH=$PYTHONPATH:src streamlit run src/insights/invoice_app.py

# Using Poetry
poetry run streamlit run src/insights/invoice_app.py
```

4. Access the application at:
```
http://localhost:8501
```

## 📝 Usage

1. Open the application in your web browser
2. Upload a PDF invoice using the file uploader
3. Wait for the processing to complete
4. View the extracted data in JSON format
5. Download the results if needed

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📫 Contact

- **Author**: Amer Alnajdawi
- **Email**: amernajdawi8@gmail.com

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
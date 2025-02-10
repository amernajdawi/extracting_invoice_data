import json
import subprocess
import time

from langchain.prompts import PromptTemplate
from langchain_community.llms.ollama import Ollama

from src.insights.pdf_to_text import pdf_to_string
from src.insights.prompts import EXTRACTION_PROMPT


def ensure_ollama_running():
    try:
        subprocess.run(["curl", "http://localhost:11434"], capture_output=True, check=True)
    except:
        subprocess.Popen(["ollama", "serve"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        max_retries = 5
        for i in range(max_retries):
            try:
                time.sleep(5)
                subprocess.run(["curl", "http://localhost:11434"], capture_output=True, check=True)
                break
            except:
                if i == max_retries - 1:
                    raise Exception("Failed to start Ollama after multiple attempts")

    result = subprocess.run(["ollama", "pull", "qwen:0.5b"], capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Failed to pull model: {result.stderr}")


def init_llm():
    return Ollama(
        model="mistral",
        temperature=0,
        base_url="http://ollama:11434",
        num_thread=4,
        num_ctx=2048,
        repeat_last_n=64,
    )


def parse_json_response(response):
    """Helper function to parse JSON response from LLM."""
    try:
        return json.loads(response)
    except json.JSONDecodeError:
        cleaned_response = response.strip()
        if "```json" in cleaned_response:
            cleaned_response = cleaned_response.split("```json")[1].split("```")[0].strip()
        try:
            return json.loads(cleaned_response)
        except:
            return {"error": "Invalid JSON response from model"}


def process_invoice(text, llm):
    prompt = PromptTemplate(template=EXTRACTION_PROMPT, input_variables=["text"])
    try:
        response = llm(prompt.format(text=text))
        result = parse_json_response(response)
        
        if "FileList" not in result and "error" not in result:
            return {"error": "Response missing FileList structure"}
        
        return result
    except Exception as e:
        return {"error": f"Failed to get response from model: {str(e)}"}


class InvoiceProcessor:
    def __init__(self):
        self.llm = init_llm()

    def process_pdf(self, pdf_file):
        try:
            text = pdf_to_string(pdf_file)
            return process_invoice(text, self.llm)
        except Exception as e:
            return {"error": f"Processing failed: {str(e)}"}

from typing import Any

import pdfplumber


def pdf_to_string(path: Any) -> str:
    """
    converts the PDF file content to Text and
    Returns the raw content of the lab report file
    Args:
    path (str): The raw text
    :return: string
    """
    pdf_object = pdfplumber.open(path)  # read PDf
    total_pages = len(pdf_object.pages)
    text = ""
    for page_number in range(total_pages):  # iterate over all pages
        page = pdf_object.pages[page_number]
        page_text = page.extract_text(
            layout=False, y_tolerance=4.8, x_tolerance=20, y_density=20, x_density=20
        )  # extract whole pdf as string
        text += "\n" + page_text
    return text

import json

import streamlit as st

from insights.invoice_processor import InvoiceProcessor

st.set_page_config(page_title="Invoice Data Extractor", page_icon="📄", layout="wide")


def display_results(result):
    if not result.get("FileList"):
        st.error("No data found")
        return

    st.json(result)


def main():
    st.title("📄 Invoice Processor")

    try:
        processor = InvoiceProcessor()
        uploaded_file = st.file_uploader("Upload PDF", type="pdf")

        if uploaded_file:
            with st.spinner("Processing..."):
                result = processor.process_pdf(uploaded_file)
                if "error" in result:
                    st.error(result["error"])
                else:
                    st.success("Processing complete!")
                    display_results(result)

                    # Download option
                    st.download_button(
                        "JSON herunterladen",
                        json.dumps(result, indent=2, ensure_ascii=False),
                        "rechnung_daten.json",
                        "application/json",
                    )

    except Exception:
        st.error("Failed to initialize processor")


if __name__ == "__main__":
    main()

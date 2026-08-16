"""
Write a class VectorStore with:

__init__ that takes a list of DocumentChunk objects and stores them
an add(chunk) method that appends a new chunk
a count() method that returns how many chunks are stored
a __str__ that returns "VectorStore(n=<count> chunks)"
"""

# class VectorStore:
#     def __init__(self, chunks) -> None:
#         self.chunks = chunks

#     def add(self, chunk) -> None:
#         self.chunks.append(chunk)

#     def count(self) -> int:
#         return len(self.chunks)

#     def __str__(self) -> str:
#         return f"VectorStore(n={self.count}) chunks"

import json
from pathlib import Path

import PyPDF2


def json_dumping(file, data):
    path = Path(file)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(file, "w") as f:
        json.dump(data, f)


data = {"name": "yash", "student": "IT", "College": "VESIT"}
json_dumping("output/file.json", data)


# Yield
def extract_pdf_text(pdf_file, output_file):
    with open(pdf_file, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            yield page.extract_text()


for page_text in extract_pdf_text(
    "data/Accidental-Death-Benefit-101B001V01.pdf", "output/extracted_text.txt"
):
    with open("output/extracted_text.txt", "a") as f:
        f.write(page_text)


def read_in_chunks(file_path, chunk_size=500):
    with open(file_path, "r", encoding="utf-8") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk




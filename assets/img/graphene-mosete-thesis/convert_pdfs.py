r"""Convert every PDF in this folder to a same-named PNG (browsers cannot show PDFs inside <img>).

Usage (PowerShell, from img\graphene-mosete-thesis):
    pip install pymupdf
    python convert_pdfs.py
"""
from pathlib import Path
import fitz  # PyMuPDF

folder = Path(__file__).resolve().parent
for pdf in sorted(folder.glob("*.pdf")):
    out = pdf.with_suffix(".png")
    with fitz.open(pdf) as doc:
        pix = doc[0].get_pixmap(dpi=250, alpha=False)  # white background, first page only
        pix.save(out)
    print(f"{pdf.name} -> {out.name} ({pix.width}x{pix.height})")

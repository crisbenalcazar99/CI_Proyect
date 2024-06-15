import os
import shutil
from PyPDF2 import PdfFileReader, PdfFileWriter
import fitz
import cv2
import numpy as np

def copy_files(root_path, target_path, number_files):
    cont = 0

    if not os.path.exists(target_path):
        os.makedirs(target_path)

    for filename in os.listdir(root_path)[:number_files]:
        extension = os.path.splitext(filename)[1]
        src_file = os.path.join(root_path, filename)
        dst_file = os.path.join(target_path, str(cont))
        separate_pages_from_PDF(src_file, target_path, dst_file)
        cont += 1


def separate_pages_from_PDF(root_path, target_path, name_new_file):
    with open(root_path, "rb") as input_pdf:
        try:
            pdf_reader = PdfFileReader(input_pdf)
            for page_number in range(pdf_reader.getNumPages()):
                output_pdf_writer = PdfFileWriter()
                output_pdf_writer.addPage(pdf_reader.getPage(page_number))
                output_path = name_new_file + f"_{page_number}.pdf"
                with open(output_path, "wb") as output_pdf_file:
                    output_pdf_writer.write(output_pdf_file)
                    print(f"Page {page_number} saved to {output_path}")
        except Exception as e:
            pass


def transform_PDF_Image(root_path, target_path):
    if not os.path.exists(target_path):
        os.makedirs(target_path)

    for filename in os.listdir(root_path):
        try:
            src_file = os.path.join(root_path, filename)
            pdf_document = fitz.open(src_file)
            page = pdf_document.load_page(0)

            # Crear una matriz de transformación para aumentar la resolución
            zoom_matriz = 4
            matrix = fitz.Matrix(zoom_matriz, zoom_matriz)

            image = page.get_pixmap(matrix=matrix)
            img_array = np.frombuffer(image.samples, dtype=np.uint8).reshape(image.height, image.width, 3)
            img = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
            dst_file = os.path.join(target_path, os.path.splitext(filename)[0])
            print(dst_file)
            cv2.imwrite(dst_file + ".png", img)
        except Exception as e:
            pass

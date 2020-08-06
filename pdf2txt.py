import os
import PyPDF2
from slugify import slugify


if __name__ == '__main__':
	print("Ingrese la ruta de la carpeta de los PDFs")
	input_path = input()

	print("Ingrese la ruta de la carpeta donde estaran los archivos de texto")
	output_path = input()

	pdfs = [f for f in os.listdir(input_path) if f.endswith(".pdf")]

	for pdf in pdfs:
		reader = PyPDF2.PdfFileReader(f"{input_path}/{pdf}")
		print(f"Convirtiendo: {pdf}. Cant de Pag: {reader.getNumPages()}")

		path_to_save = f"{output_path}/{slugify(pdf)}"
		print(path_to_save)

		if not os.path.exists(path_to_save):
			os.makedirs(path_to_save)

		for i in range(1, reader.getNumPages()):
			text_page = reader.getPage(i).extractText()

			text_file = open(f"{path_to_save}/page_{i}.txt", "w", encoding="utf-8")
			text_file.write(text_page)
			text_file.close()





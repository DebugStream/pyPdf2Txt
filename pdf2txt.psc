Algoritmo pdf_2_txt
	Definir input_path Como Caracter
	Definir ouput_path Como Caracter
	Dimension pdfs[3]
	
	Escribir "Ingresa la ruta de la carpeta de los PDFs"
	Leer input_path
	
	Escribir "Ingresa la ruta de la carpeta donde estarán los archivos de texto"
	Leer output_path
	
	pdfs[1] <- "laOdisea.pdf"
	pdfs[2] <- "CorazonDelator.pdf"
	pdfs[3] <- "FloresParaAlgernon.pdf"
	
	Para Cada pdf En pdfs Hacer
		Escribir "Convirtiendo: " + pdf
		
		Para i <- 1 Hasta 5 Hacer
			Escribir "Guardando Hoja Nro ", i
		FinPara
		
	FinPara
	
	
FinAlgoritmo

import PyPDF2

pdffile = open('PROGRAMMING_Clean_Code_by_Robert_C_Mart.pdf','rb')
read_the_pdf=PyPDF2.PdfFileReader(pdffile)
print(read_the_pdf.numPages)
single_page = read_the_pdf.getPage(45)
print(single_page.extractText())

for x in read_the_pdf.getPage():
    single_page = read_the_pdf.getPage(x)
    print(x)

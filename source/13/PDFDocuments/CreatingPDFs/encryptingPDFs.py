import PyPDF2

pdfFile = open("meetingminutes.pdf", "wb")
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWrite()

for pageNum in range(pdfReader.numPages):
    pdfWrite.addPage(pdfReader.getPage(pageNum))

pdfWriter.encrypt("swordfish")
resultPdf = open("encryptedminutes.pdf", "wb")
pdfWriter.write(resultPdf)
resultPdf.close()

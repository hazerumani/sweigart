import PyPDF2

pdfReader = PyPDF2.PdfFileReader(open("encrypted.pdf", "rb"))
print(pdfReader.isEncrypted)
# print(pdfReader.getPage(0))
pdfReader.decrypt("rosebud")
pageObj = pdfReader.getPage(0)
print(pageObj)

import PyPDF2

class Main(object):
    """The main class of application"""

    def __init__(self):
        self.pdfFileObj = open('examples/PythonCrashCourse.pdf', 'rb')
        self.pdfReader = PyPDF2.PdfFileReader(self.pdfFileObj)
        print(self.pdfReader.numPages)

    def get_text_from_page(self, number):
        self.pageObj = self.pdfReader.getPage(number)
        print(self.pageObj.extractText())

pdf = Main()
pdf.get_text_from_page(8)

import PyPDF2
from settings import Settings

class Main(object):
    """The main class of application"""

    def __init__(self):
        self.settings = Settings()

        self.file_name = self.settings.file_name
        self._read_file(self.file_name)
        self.num_pages = self.pdfReader.numPages

        self.text_to_search = self.settings.text_to_search

    def _get_text_from_page(self, number):
        self.pageObj = self.pdfReader.getPage(number)
        return self.pageObj.extractText()

    def _read_file(self, file_name):
        self.pdfFileObj = open(file_name, 'rb')
        self.pdfReader = PyPDF2.PdfFileReader(self.pdfFileObj)

    def counting_text_on_pages(self):
        for page in range(self.num_pages):
            text = self._get_text_from_page(page)
            number = text.count(self.text_to_search)
            if number:
                definition_part = self._get_definition_part(text)
                print(page + 1, " ", number, " ", definition_part)

    def _get_definition_part(self, text):
        start = text.find(self.text_to_search)
        return text[start + 5: start + 20]

pdf = Main()
pdf.counting_text_on_pages()

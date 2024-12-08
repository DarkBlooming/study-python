from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

class Scannable(ABC):
    @abstractmethod
    def scan_document(self):
        pass

class Copyable(ABC):
    @abstractmethod
    def copy_document(self):
        pass

class Printer(Printable):
    def print_document(self, document):
        print(f"Print the document: {document}")

class Scanner(Scannable):
    def scan_document(self):
        print("Document scanning is complete")

class MultiFunctionDevice(Printable, Scannable, Copyable):
    def print_document(self, document):
        print(f"Print the document: {document}")

    def scan_document(self):
        print("Document scanning is complete")

    def copy_document(self):
        print("Document copying is complete")

if __name__ == "__main__":
    printer = Printer()
    scanner = Scanner()
    mfd = MultiFunctionDevice()

    printer.print_document("File.pdf")
    scanner.scan_document()
    mfd.print_document("Report.docx")
    mfd.scan_document()
    mfd.copy_document()

from fpdf import FPDF

class PDFGenerator:
    def __init__(self):
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=12)

    def add_title(self, title):
        """Adiciona um título ao PDF."""
        self.pdf.set_font("Arial", 'B', size=16)
        self.pdf.cell(0, 10, title, ln=True, align='C')
        self.pdf.ln(10)

    def add_section(self, section_title, content):
        """Adiciona uma seção com título e conteúdo ao PDF."""
        self.pdf.set_font("Arial", 'B', size=14)
        self.pdf.cell(0, 10, section_title, ln=True)
        self.pdf.set_font("Arial", size=12)
        self.pdf.multi_cell(0, 10, content)
        self.pdf.ln(5)

    def save_pdf(self, filename):
        """Salva o PDF com o nome especificado."""
        self.pdf.output(filename)
        print(f"PDF '{filename}' gerado com sucesso!")


def main():
    print("Gerador de PDF em Python")
    filename = input("Digite o nome do arquivo para salvar (ex: documento.pdf): ")

    if not filename.lower().endswith('.pdf'):
        filename += '.pdf'

    generator = PDFGenerator()

    # Título do PDF
    title = input("Digite o título do seu documento: ")
    generator.add_title(title)

    while True:
        section_title = input("Digite o título da seção (ou 'sair' para finalizar): ")
        if section_title.lower() == 'sair':
            break
        content = input("Digite os dados que deseja adicionar à seção: ")
        generator.add_section(section_title, content)

    generator.save_pdf(filename)

if __name__ == "__main__":
    main()
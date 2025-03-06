from fpdf import FPDF


class PDF(FPDF):
    def __init__(self, filename, name):
        super().__init__()
        self.filename = filename
        self.name = name

    def create_shirt(self):
        self.add_page()

        self.set_font("Arial", "B", 45)
        self.set_text_color(0, 0, 0)

        self.cell(0, 55, "CS50 Shirtificate", align="C")

        self.image(self.filename, x=5, y=70, w=200)

        self.set_font("Arial", "B", size=25)
        self.set_text_color(255, 255, 255)
        self.set_xy(10, 130)
        text = f"{self.name} took CS50"
        self.cell(0, 10, text, align="C")


def main():
    name = input("Name: ")
    image_path = "./shirtificate.png"

    pdf = PDF(image_path, name)

    pdf.create_shirt()

    pdf.output("./shirtificate.pdf")


main()

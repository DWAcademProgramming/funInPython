from fpdf import FPDF

class Bill:
    """
    A sample billing application for roommates and their share of a bill
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period

class Roommate:
    """
    Creates a roommate object for the bill to go to
    """

    def __init__(self, name, time):
        self.name = name
        self.time = time

    def pays(self, bill, roomate2):
        weight = self.time / (self.time + roomate2.time)
        to_pay = bill.amount * weight
        return to_pay

class pdfReport:
    """
    Creates a PDF report
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, roommate1, roommate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Roommate Bill', border=1, align='C', ln=1)
        pdf.cell(w=100, h=40, txt='Period: ', border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)

        pdf.output("bill.pdf")


the_bill = Bill(amount=120, period= "May 2022")
john = Roommate(name="Max", time=28)
jen = Roommate(name="Jen", time=21)

pdf_report = PdfReport(filename="")
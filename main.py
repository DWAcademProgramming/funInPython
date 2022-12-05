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
        pass

the_bill = Bill(amount=120, period= "May 2022")
max = Roommate(name="Max", time=28)
jen = Roommate(name="Jen", time=21)
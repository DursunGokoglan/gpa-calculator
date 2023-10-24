from gpa_calculator import Calculator


class ChangeCalculator(Calculator):
    def __init__(self):
        super().__init__()
        self.dict = {}
        self.lectures = []
        self.credits = []
        self.letter_grades1 = []
        self.letter_grades2 = []
        self.letter_equivalents = {
            "a": 2,
            "b": 1.5,
            "c": 1,
            "d": 0.5,
            "f": 0
        }
        self.gpa_change = 0
        self.total_credits = 0

    def get_letter_grades1(self):
        for lecture in self.lectures:
            self.letter_grades1.append(input(f"Enter {lecture}'s first letter grade: "))

    def get_letter_grades2(self):
        for lecture in self.lectures:
            self.letter_grades2.append(input(f"Enter {lecture}'s last letter grade: "))

    def ask_total_credits(self):
        if len(self.lectures) != 0:
            self.total_credits += float(input("Enter total credits: "))

    def make_dict(self):
        self.dict = {lecture: {} for lecture in self.lectures}
        for index in range(len(self.lectures)):
            self.dict[self.lectures[index]].update({"credit": self.credits[index]})
            self.dict[self.lectures[index]].update({"letter_grade1": self.letter_grades1[index]})
            self.dict[self.lectures[index]].update({"letter_grade2": self.letter_grades2[index]})

    def calculate_difference(self):
        for lecture in self.lectures:
            lecture_numgrade1 = self.convert_letter_grades(self.dict[lecture]["letter_grade1"])
            lecture_numgrade2 = self.convert_letter_grades(self.dict[lecture]["letter_grade2"])
            self.gpa_change += (self.dict[lecture]["credit"] / self.total_credits) * (
                        lecture_numgrade2 - lecture_numgrade1)

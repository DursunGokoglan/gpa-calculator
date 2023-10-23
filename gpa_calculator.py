class Calculator:
    def __init__(self):
        self.dict = None
        self.lectures = []
        self.credits = []
        self.letter_grades = []
        self.letter_equivalents = {
            "a": 2,
            "b": 1.5,
            "c": 1,
            "d": 0.5,
            "f": 0
        }
        self.gpa = 0

    def get_lectures(self):
        lecture_count = int(input("Enter lecture count: "))
        for number in range(lecture_count):
            self.lectures.append(input("Enter lecture name: "))

    def get_credits(self):
        for lecture in self.lectures:
            self.credits.append(float(input(f"Enter {lecture}'s ects/akts: ")))

    def get_letter_grades(self):
        for lecture in self.lectures:
            self.letter_grades.append(input(f"Enter {lecture}'s letter grade: "))

    def make_dict(self):
        self.dict = {lecture: {} for lecture in self.lectures}
        for index in range(len(self.lectures)):
            self.dict[self.lectures[index]].update({"credit": self.credits[index]})
            self.dict[self.lectures[index]].update({"letter_grade": self.letter_grades[index]})

    def calculate(self):
        for lecture in self.lectures:
            lecture_numgrade = self.letter_equivalents[self.dict[lecture]["letter_grade"][0]] + self.letter_equivalents[self.dict[lecture]["letter_grade"][1]]
            self.gpa += lecture_numgrade * self.dict[lecture]["credit"] / sum(self.credits)

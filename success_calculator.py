from gpa_calculator import Calculator


class SuccessCalculator(Calculator):
    def __init__(self):
        super().__init__()
        self.dict = {}
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
        self.limgpa = 0
        self.total_credits = 0
        self.lecture_count = 0
        self.temp_total = 0

    def ask_essentials(self):
        self.limgpa = float(input("Enter limit gpa: "))
        self.total_credits = float(input("Enter total credits: "))
        self.lecture_count = int(input("Enter lecture count: "))

    def get_lecture_details(self):
        user_input = input("lecture's name, credit, letter_grade: ").split(", ")
        self.lectures.append(user_input[0])
        self.credits.append(float(user_input[1]))
        self.letter_grades.append(user_input[2])

    def make_dict(self):
        self.dict = {lecture: {} for lecture in self.lectures}
        for index in range(len(self.lectures)):
            self.dict[self.lectures[index]].update({"credit": self.credits[index]})
            self.dict[self.lectures[index]].update({"letter_grade": self.letter_grades[index]})

    def check_success(self):
        for lecture in self.lectures:
            numgrade = self.convert_letter_grades(self.dict[lecture]["letter_grade"])
            self.temp_total += numgrade * self.dict[lecture]["credit"] / self.total_credits

        if self.temp_total >= 1.8:
            return True
        else:
            self.temp_total = 0
            return False

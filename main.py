from gpa_calculator import Calculator
from gpa_change_calculator import ChangeCalculator

calculator = Calculator()
change_calculator = ChangeCalculator()

is_on = True

while is_on:
    user_input = input("g for gpa calc, c for gpa change calc, off to turn off: ")

    if user_input == "g":
        calculator.get_lectures()
        calculator.get_credits()
        calculator.get_letter_grades()
        calculator.make_dict()
        calculator.calculate()
        print(f"gpa: {calculator.gpa.__round__(2)}")

    elif user_input == "c":
        pass

    elif user_input == "off":
        print("turning off...")
        is_on = False

    else:
        print("please enter valid inputs!")

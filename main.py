from gpa_calculator import Calculator
from gpa_change_calculator import ChangeCalculator
from success_calculator import SuccessCalculator

calculator = Calculator()
change_calculator = ChangeCalculator()
success_calculator = SuccessCalculator()

is_on = True

while is_on:
    user_input = input("g for gpa calc, c for gpa change calc, s for success calc, off to turn off: ")

    if user_input == "g":
        calculator.get_lectures()
        calculator.get_credits()
        calculator.get_letter_grades()
        calculator.make_dict()
        calculator.calculate()
        print(f"gpa: {calculator.gpa.__round__(2)}")

    elif user_input == "c":
        change_calculator.get_lectures()
        change_calculator.get_credits()
        change_calculator.ask_total_credits()
        change_calculator.get_letter_grades1()
        change_calculator.get_letter_grades2()
        change_calculator.make_dict()
        change_calculator.calculate_difference()
        print(f"gpa_change: {change_calculator.gpa_change.__round__(2)}")

    elif user_input == "s":
        passed = False
        success_calculator.ask_essentials()
        while not passed:
            success_calculator.get_lecture_details()
            success_calculator.make_dict()
            passed = success_calculator.check_success()
            if len(success_calculator.lectures) == success_calculator.lecture_count:
                print("git gut")
                print("mate i felt tired so i didnt cover all, dont keep typing if youre displaying this message")

        print("you've passed")



    elif user_input == "off":
        print("turning off...")
        is_on = False

    else:
        print("please enter valid inputs!")

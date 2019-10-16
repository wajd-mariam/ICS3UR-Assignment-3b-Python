#!/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: September 2019
# This program determines whether the student is able to do the exam or not

import constants


def main():
    # getting input from the user
    classes_held = input("Enter the total number of classes held: ")
    attendance = input("Enter the total number of classes attended: ")

    # process / output
    try:
        integer_as_number1 = int(classes_held)
        integer_as_number2 = int(attendance)

    # calculating the average of classes attended by the user
        avg = (int(attendance) / int(classes_held)) * 100

        if avg == constants.ATTENDANCE:
            print("You can do the exam since your attendance is 75%!")

        elif avg > constants.ATTENDANCE:
            print("You can do the exam, attendance is {}%".format(round(avg)))

        else:
            print("You can't do the exam,attendance is {}%".format(round(avg)))
    except Exception:
        print("This was not a valid entry")
    finally:
        print("Good bye!")


if __name__ == "__main__":
    main()

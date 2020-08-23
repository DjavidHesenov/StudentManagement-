StudentCodeList = ["001", "002"]
StudentNameList = ["Cavid", "Elshad"]
StudentSurnameList = ["Hesenov", "Malikov"]
StudentMailList = ["hesenovdjavid@gmail.com", "malikov@gmail.com"]
StudentPhoneList = ["+994593457684", "+994593457681"]

def checkCode():
    StudentCode = input("Insert student code: ")
    if StudentCode in StudentCodeList:
        print("Such code already exists")
        checkCode()
    elif (len(StudentCode) == 3) and (StudentCode.isdigit()):
        StudentCodeList.append(StudentCode)
    else:
        print("Incorrect code. Code can consist of 3 integers only")
        checkCode()
def checkMail():
    StudentMail = input("Insert student mail: ")
    if "@" in StudentMail:
        StudentMailList.append(StudentMail)
    else:
        print("Mail must have a '@' sign. ")
        checkMail()
def checkPhone():
    StudentPhone = input("Insert student phone: ")
    if StudentPhone.startswith("+994") and len(StudentPhone) == 13:
        StudentPhoneList.append(StudentPhone)
    else:
        print("Phone must start with '+994' and can be 12 integers max")
        checkPhone()

def choice1():
    checkCode()

    StudentName = input("Insert student name: ")
    StudentNameList.append(StudentName)
    StudentSurname = input("Insert student surname: ")
    StudentSurnameList.append(StudentSurname)
    checkMail()
    checkPhone()


def choice2():
    CodeToChange = input("Insert code of student to change. ")
    if CodeToChange not in StudentCodeList:
        print("There's no student with such code.")
        choice2()
    elif CodeToChange in StudentCodeList:
        VariableToChange = input(
"""What you want to change? 
Press '1' to change Name
Press '2' to change Surname
Press '3' to change Mail
Press '4' to change Phone Number
""")
        IndexOfChangedStudent = StudentCodeList.index(CodeToChange)
        if VariableToChange == "1":
            NewName = input("Old name is '{}'. Insert new name. ".format(StudentNameList[IndexOfChangedStudent]))
            StudentNameList[IndexOfChangedStudent] = NewName
        elif VariableToChange == "2":
            NewSurname = input("Old surname is '{}'. Insert new surname. ".format(StudentSurnameList[IndexOfChangedStudent]))
            StudentSurnameList[IndexOfChangedStudent] = NewSurname
            print(StudentSurnameList)
        elif VariableToChange == "3":
            def checkNewMail():
                NewMail = input("Old mail is '{}'. Insert new mail. ".format(StudentMailList[IndexOfChangedStudent]))
                if '@' in NewMail:
                    StudentMailList[IndexOfChangedStudent] = NewMail
                    print(StudentMailList)
                else:
                    print("Mail must have a '@' sign. ")
                    checkNewMail()
            checkNewMail()
        elif VariableToChange == "4":
            def checkNewPhone():
                NewPhone = input("Old number is '{}'. Insert new number. ".format(StudentPhoneList[IndexOfChangedStudent]))
                if NewPhone.startswith("+994") and len(NewPhone) == 13:
                    StudentPhoneList[IndexOfChangedStudent] = NewPhone
                    print(StudentPhoneList)
                else:
                    print("Phone must start with '+994' and can be 12 integers max")
                    checkNewPhone()
            checkNewPhone()

def choice3():
    SearchedCodeToDelete = input("Insert Code: ")
    if SearchedCodeToDelete in StudentCodeList:
        IndexToDelete = StudentCodeList.index(SearchedCodeToDelete)
        StudentCodeList.pop(IndexToDelete)
        StudentNameList.pop(IndexToDelete)
        StudentSurnameList.pop(IndexToDelete)
        StudentMailList.pop(IndexToDelete)
        StudentPhoneList.pop(IndexToDelete)
        print("Student with code '{}' was deleted.".format(SearchedCodeToDelete))
    else:
        print("There's no student with such code")
        choice3()


def choice4():
    SearchedName = input("Insert Name: ")
    SearchedName = SearchedName.lower()
    SearchedName = SearchedName.capitalize()
    if SearchedName in StudentNameList:
        SearchedNameIndex = StudentNameList.index(SearchedName)
        print("Code:    ", StudentCodeList[SearchedNameIndex])
        print("Name:    ", StudentNameList[SearchedNameIndex])
        print("Surname: ", StudentSurnameList[SearchedNameIndex])
        print("Mail:    ", StudentMailList[SearchedNameIndex])
        print("Phone:   ", StudentPhoneList[SearchedNameIndex])
    else:
        print("There's no such student")
        choice4()

def ChoiceFunction ():
    choice = input("""What you want to do?
Press "1" to add new student.
Press "2" to change info about student based on student code.
Press "3" to delete info about student based on student code.
Press "4" to see info about student based on name.
Press "5" to see info about all students.
Press "6" to stop program.
    """)
    if choice == "1":
        choice1()
    elif choice == "2":
        choice2()
    elif choice == "3":
        choice3()
    elif choice == "4":
        choice4()
    elif choice == "5":
        print("Student Codes:        ",  StudentCodeList)
        print("Student Names:        ", StudentNameList)
        print("Student Surnames:     ", StudentSurnameList)
        print("Student Mails:        ", StudentMailList)
        print("Student Phone Numbers:", StudentPhoneList)
    elif choice == "6":
        return
    else:
        print("""
----------------------------------------------------------------------------------
Incorrect input. Use numbers from 1 to 5.
----------------------------------------------------------------------------------""")
        ChoiceFunction()



ChoiceFunction()




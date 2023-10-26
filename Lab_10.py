class student_details:
    def __init__(self):
        self.dicti = {}

    def create_student(self , name , course , division , roll , state , english , maths , statistics):
        temp = {
            "Name" : name , 
            "Course" : course , 
            "Division" : division , 
            "roll-no" : roll , 
            "state" : state,
            "English" : english,
            "Maths" : maths,
            "Statistics" : statistics
        }
        self.dicti[roll] = temp

    def search_student(self , roll):
        if roll in self.dicti:
            print(self.dicti[roll])

    def delete_student(self , roll):
        if roll in self.dicti:
            del self.dicti[roll]

    def edit_student(self , roll , col , val):
        if roll in self.dicti:
            self.dicti[roll][col] = val
            print("Changes saved successfully")

    def print_students(self):
        print(self.dicti)

    def eixt_student():
        exit()

pd = student_details()

while True:
    print("Welcome to a menu drven programme for student management.")
    print("Please choose any option from the below ")
    print("1. Create Student")
    print("2. Search Student")
    print("3. Delete Student")
    print("4. Print Students")
    print("5. Edit Student")
    print("6. Exit")

    choice = int(input("Enter the option from the above: "))

    if choice == 1:
        name = input("Enter the name of the student: ")
        course = input("Enter the course of the student: ")
        division = input("Enter the division of the student: ")
        roll = input("Enter the roll number of the student")
        state = input("Enter the state of the student: ")
        english = input("Enter the marks of the english: ")
        maths = input("Enter the marks of the maths: ")
        statistics = input("Enter the marks of the statistics: ")
        pd.create_student(name , course , division , roll , state  , english , maths , statistics)
        print("Student added successfully")

    if choice == 2:
        roll = input("Enter the roll number : ")
        pd.search_student(roll)

    if choice == 3:
        roll = input("Enter the roll number of the student: ")
        pd.delete_student(roll)
        print("Entry deleted successfully.")

    if choice == 4 :
        pd.print_students()
    
    if choice == 5 :
        roll = input("Enter the roll number of the student: ")
        col = input("Enter the field you want to edit: ")
        val = input("Enter the value you want to edit")
        pd.edit_student(roll , col , val)
        print("Value edited successfully.")

    if choice == 6:
        print("Thankyou. Visit again")
        break

class student:
    def __init__(self,name,clas,grade):
        self.name = name
        self.clas = clas
        self.grade = grade

    def display_info(self):
        print("Student information\nName :", self.name)
        print("Class:", self.clas)
        print("Grade:", self.grade)
    
    def updated_grade(self, new_grade):
        self.grade = new_grade
        print("Updated information:")
        student1.display_info()

    def is_passing(self):
        if self.grade>=60:
            return True
        else:
            return False
        
student1=student("Veenus", "5th", 47)
student1.display_info()
student1.updated_grade(80)

if student1.is_passing():
    print("Congratulations!",student1.name, "is pass.")
else:
    print(student1.name,"is fail.\nTry hard next time!")
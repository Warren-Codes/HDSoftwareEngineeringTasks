'''
Compulsory Task 1:
------------------
'''


class Course:
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"

    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    def location(self):
        print("Head office Location: Cape Town.")


class OOPCourse(Course):
    def __init__(self, description="OOP Fundamentals", trainer="Mr Anon A. Mouse"):
        self.description = description
        self.trainer = trainer

    def trainer_details(self):
        print(f"The course is {self.description} and the trainer for the course is {self.trainer}.")

    def show_course_id(self):
        print("The course ID is: #12345")


course_1 = OOPCourse()
course_1.trainer_details()
course_1.contact_details()
course_1.show_course_id()

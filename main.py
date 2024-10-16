from Student import Student
from Employee import Employee

student = Student("Mike", 30, "enginer", 1, 70)
# student.foo()

employee = Employee("John", 40, "Software Engineer", 45000)
people = [student, employee]
for person in people:
    person.printMyself()










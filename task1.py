#! python3
"""
(10 points) 
Create a class object for a student.
It should have the following properties
str name
str studentNumber
int grade
list courses - to corresepond with course names
list grade - to correspond with grades

It should have the following methods:
average()       - determines the mathematical average of all course grades
getHonorRoll()  - determines the average of the top 5 courses if there are at least 5 courses.
                  returns True if the average is 86 or higher (on the honor roll)
                  returns False if not on the honor roll
showCourses()   - prints a list of all courses
showGrade(int)  - takes 1 parameter, the index of the list
                - displays the course name and grade
getCourses(list)- Receives a list of courses and stores that in the class property
getGrades(list) - Receives a list of grades and stores that in the class property
constructor     - should require the student name, studentNumber and grade (in that order)
"""

class student:

    # properties should be listed first
    name = ""
    studentNumber = ""
    grade = 0
    courses = []
    grades = []


    def __init__(self,name,studentNumber,grade):
        # You will need to create your own input parameters for all methods
        self.name = name
        self.studentNumber = studentNumber
        self.grade = grade
        print(self.name + "'s student number is:" + self.studentNumber + "\n" + self.name + " is now in grade" + str(self.grade))
    def getCourses(self,courses):
        self.courses = courses
        return self.courses

    def showCourses(self):
        print("This is a list of courses that the student takes:")
        for i in self.courses:
            print(i)

    def getGrades(self,grades):
        self.grades = grades
        return self.grades

    def showGrades(self,index):
        print("The student's grade of " + self.courses[index] + " is:" + str(self.grades[index]))

    def average(self):
        a = 0
        for i in self.grades:
            a = a + i
        average = a/int(len(self.grades))
        print (self.name + "'s average grade is:" + str(average))
        return average

    def getHonorRoll(self):
        self.grades.sort()
        if len(self.grades) >= 5:
            x = (float(self.grades[-1]) + float(self.grades[-2]) + float(self.grades[-3]) + float(self.grades[-4]) + float(self.grades[-5]))/5
            if x >= 86:
                print("The student is on the Honor Roll")
                return True
            else:
                print("The student is not on the Honor Roll")
                return False

    def __del__(self):
        pass


def main():
    # This contains test data that will be used by the autograder.
    # do not modify this function

    st1 = student("Anita Bath","91334",11)
    st1.getCourses( ["English","Math","PE","Computers","History","Biology","Japanese"] )
    st1.getGrades( [91, 94, 87, 99, 82, 100, 73])
    st1.showCourses()
    st1.showGrades(1)
    st1.average()
    st1.getHonorRoll()

    st2 = student("Joe Lunchbox","12346", 11)
    st2.getCourses( ["English","Math","Physics","Computers","Geography","Chemistry","French"] )
    st2.getGrades( [71, 98, 93, 95, 68, 81, 71])




main()
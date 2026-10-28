import numpy as np
class StudentAnalyzer:
    def __init__(self,student_name,marks_list):
        self.student_name=student_name
        self.marks_list=np.array(marks_list)

    def get_average(self):
        return np.mean(self.marks_list)
    def get_highest(self):
        return np.max(self.marks_list)
    def get_lowest(self):
        return np.min(self.marks_list)
    def get_grade(self):
        avg_marks=np.mean(self.marks_list)
        if avg_marks>=90:
            return "A+"
        elif avg_marks>=80:
            return "A"
        elif avg_marks>=70:
            return "B"
        elif avg_marks>=60:
            return "C"
        else:
            return "F"
    def passed(self):
        avg_marks=np.mean(self.marks_list)
        if avg_marks>=40:
            return True
        else:
            return False
    def display(self):
        print(f"Name:{self.student_name}")
        print(f"Average:{self.get_average():.2f}")
        print(f"Highest:{self.get_highest()}")
        print(f"Lowest:{self.get_lowest()}")
        print(f"Grade:{self.get_grade()}")
        print(f"Passed:{self.passed()}")

s1 = StudentAnalyzer("Rahul",  [85, 78, 92, 88, 76])
s2 = StudentAnalyzer("Priya",  [92, 95, 98, 91, 94])
s3 = StudentAnalyzer("Amit",   [35, 42, 28, 50, 38])

s1.display()
s2.display()
s3.display()

from abc import ABC, abstractmethod


class AcademicTask(ABC):
    def __init__(self, title, max_points, is_graded=False):
        self.title = title
        self.max_points = max_points
        self.is_submitted = False
        self.is_graded = is_graded
        self.score = 0

    def submit_work(self):
        if self.is_graded:
            print(f"Task '{self.title}' has already been graded. Cannot resubmit.")
        elif self.is_submitted:
            print(f"Task '{self.title}' has already been submitted.")
        else:
            print(f"Submitting work for task '{self.title}'...")
            self.is_submitted = True

    @abstractmethod
    def grade_work(self, points):
        pass

    def get_details(self):
        if self.is_graded:
            status = f"Graded ({self.score}/{self.max_points})"
        elif self.is_submitted:
            status = "Submitted"
        else:
            status = "Pending"

        return f"Title: {self.title} | Max Points: {self.max_points} | Status: {status}"


class Homework(AcademicTask):
    def grade_work(self, points):
        if not self.is_submitted:
            print(f"Cannot grade '{self.title}' before it is submitted.")
            return
        if not (0 <= points <= self.max_points):
            raise ValueError(f"Points must be between 0 and {self.max_points}.")

        self.score = points
        self.is_graded = True
        print(f"Graded '{self.title}': {self.score}/{self.max_points}")

#this will serve as an example:
hw = Homework("Python ABCs", 100)
hw.submit_work()
hw.grade_work(95)
print(hw.get_details())

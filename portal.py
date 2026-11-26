class CoursePortal:
    def __init__(self, course_name):
        self.course_id = None
        self.course_name = course_name
        self.is_locked = False
    
    def lock_portal(self):
        self.is_locked = True
        print("Deadline passed. Portal is now locked.")


    def accept_submission(self, submission):
        if self.is_locked:
            print("Error: Deadline has passed. Submission rejected.")
        else:
            print(f"Submission accepted for {self.course_name}.")
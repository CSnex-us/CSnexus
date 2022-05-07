# The Session class denotes a specific offering of a Course. 
# Because Python uses class in a different context, we use
# the word session to describe what is usually referred to 
# as a class - a class of students. 

class Session():
    def __init__(self) -> None:
        self.id = ""
        self.course_id = ""
        self.period = 0
        self.instructor_Id = ""
        self.enrolmentsmax_class_size = 30
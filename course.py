# Course class corresponds to the abstract entity where a Course can 
# be taught in many classes - we use the term 'Session' to connotate 
#  a specific class.

# The Course class is an important entity in CSnexus as it is the domain 
# of the course content.

class Course():
    def __init__(self) -> None:
        self.id = ""
        self.title = ""
        self.weighted = False
        self.grades = []
        self.enrolments = ""


    
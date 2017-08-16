#Constructor of Class Course
class Course():
    def __init__(self,nameEntry,codeEntry):
        self.courseName = nameEntry
        self.courseCode = codeEntry
        self.campusList = []
        self.classRoomsList = []
        self.classScheduleList = []
        self.teacherList = []
        self.studentList = []
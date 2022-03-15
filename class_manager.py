# Class List, by Jackson Urquhart - 20 February 2022 @ 18:51

class constructor:
    def __init__(self, course, num_of_seats, term, mode, course_list):
        self.course = course
        self.num_of_seats = num_of_seats
        self.term = term
        self.mode = mode
        self.course_list = course_list
        
    def get_course(self):
        return(self.course)
    
    def get_term(self):
        return(self.term)
    
    def get_mode(self):
        return(self.mode)
    
    def get_num_of_seats(self):
        return(self.num_of_seats)
    
    def get_student(self, in_seat):
        self.in_seat=in_seat
        if self.in_seat in self.course_list:
            return(self.course_list[self.in_seat][1])
        else:
            return(None)
        
    def enroll_student(self, in_student_ID, in_student_name, in_seat):
        self.in_student_ID = in_student_ID
        self.in_student_name = in_student_name
        self.in_seat = in_seat
        
        if self.in_seat in self.course_list or self.in_seat > self.num_of_seats or 1 > self.num_of_seats:
            return(False)
        else:
            self.course_list[self.in_seat] = [self.in_student_ID, self.in_student_name]
            return(True)
        
# test vars
course = '1920'
num_of_seats = 52
term = 'Winter'
mode = True
course_list = {1: [1001, 'Harry Jones'], 2: [1002, 'Jeffrey'], 3: [1003, 'Bill Sue'], 4: [1004, 'MaryEllen '], 5: [1005, 'Matthew'], 6: [1006, 'Steven'], 7: [1007, 'Florinda'], 8: [1008, 'Alyssa '], 9: [1009, 'Rick'], 10: [1010, 'Rebecca'], 11: [1011, 'Hardath Peter'], 12: [1012, 'Jill'], 13: [1013, 'Jeremy'], 14: [1014, 'Anson '], 15: [1015, 'Janell'], 16: [1016, 'Tiffany'], 17: [1017, 'Kathryn '], 18: [1018, 'Farah'], 19: [1019, 'Marshall'], 20: [1020, 'Tina'], 21: [1021, 'Stacey'], 22: [1022, 'Francis'], 23: [1023, 'Marina'], 24: [1024, 'Rob'], 25: [1025, 'Laura'], 26: [1026, 'Michael'], 27: [1027, 'Steve'], 28: [1028, 'David '], 29: [1029, 'Courtney '], 30: [1030, 'Susan'], 31: [1031, 'Roberta '], 32: [1032, 'Thomas'], 33: [1033, 'Diane'], 34: [1034, 'RANDOLPH'], 35: [1035, 'Kristine'], 36: [1036, 'rachel'], 37: [1037, 'Tyler'], 38: [1038, 'Love'], 39: [1039, 'LOIS'], 40: [1040, 'Frank'], 41: [1041, 'Suzanne'], 42: [1042, 'Paul'], 43: [1043, 'Mark'], 44: [1044, 'Anna'], 45: [1045, 'Joe'], 46: [1046, 'William'], 47: [1047, 'Brian'], 48: [1048, 'Luca'], 49: [1049, 'Dennis'], 50: [1050, 'Michelle']}

# test object created
computer_science = constructor(course, num_of_seats, term, mode, course_list)

# test method call results
print(computer_science.get_course())
print(computer_science.get_term())
print(computer_science.get_mode())
print(computer_science.get_num_of_seats())
print(computer_science.get_student(1))
print(computer_science.enroll_student(1051, 'New Guy', 52))


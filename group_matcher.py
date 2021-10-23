class Student:
    all_students = []

    def __init__(self, time_list):
        # Time list is a dict of times as strings, each with T/F depending on available or not
        self.available_times = [k for k, v in time_list.items() if v]
        all_students.append(self)
        # TODO Read python csv docs


def random_groups(student_list, time_list, max_size=5):
    """Take in a list of students and another list of time strings, return a dict where each key is a time and val is a list of students who should meet during that time"""
    # TODO: Generate mock data and test.
    study_groups = {time: [] for time in time_list}
    for student in student_list:
        for available_time in student.available_times:
            if len(study_groups[available_time]) < max_size:
                study_groups[available_time].append(student)
    return study_groups

def candidate_groups(student_list, time_list, max_size):
    # More complex. Generates a list of such groups. Is this necessary?

def compatibility(student_list):
    """Between 0 and 1."""
    return 1

# NOTE: Filtering in advance based on things like experience might be faster? But also less reliable.

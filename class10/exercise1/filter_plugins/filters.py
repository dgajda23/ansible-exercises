def filter1(in_str):
    return in_str.upper()

def filter2(in_str):
    return in_str.lower()

def filter3(in_str):
    return in_str.capitalize()

class FilterModule(object):
    def filters(self):
        return {
            "filter1": filter1,
            "filter2": filter2,
            "filter3": filter3,
        }

class student:
    #now define different attribute , init fn to map out data type
    def __init__(self, name, id, course, score, pass_fail):
        self.name = name
        self.id = id
        self.course = course
        self.score = score
        self.pass_fail = pass_fail

    def on_honor_roll(self):
        if self.score >= 80:
            return True
        else:
            return False
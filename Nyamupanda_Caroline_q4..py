# Caroline NYAMUPANDA
# R00206878

class Musicians:
    def __init__(self, first_name, instrument, grade, description):
        self.first_name = first_name
        self.instrument = instrument
        self.grade = grade
        self.description

    def __str__(self):
        return f"{self.first_name} is playing a {self.instrument} at the level {self.grade}, which is {self.description}"

    def level(self):
        return self.grade == self.description

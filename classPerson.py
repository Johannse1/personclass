class Person():
    def __init__(self,full_name,eye_color,hair_color,job):
        self.name = full_name
        self.eyes = eye_color
        self.hair = hair_color
        self.job = job

    def description(self):
        print(f"Their name is {self.name}")
        print(f"They have {self.eyes} eyes")
        print(f"They have {self.hair} hair")
        print(f"And they work as a {self.job}")


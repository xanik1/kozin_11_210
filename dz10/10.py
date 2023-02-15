import random as r


class Student:
    def __init__(self, name, group, age, city, edu, programming_lang, job):
        self.name = name
        self.group = group
        self.age = age
        self.city = city
        self.edu = edu
        self.programming_lang = programming_lang
        self.job = job

    def __new__(cls, *args, **kwargs):
        print("New")
        return super(Student, cls).__new__(cls)

    def introduce(self):
        print(f"Hi, I am {self.name} from group {self.group}")

    def old(self):
        print(f"{self.name} is {self.age}")

    def location(self):
        print(f"{self.name} works as {self.job} in {self.city}")

    def obr(self):
        print(
            f"{self.name} has {self.edu} education {self.programming_lang} programming language"
        )

    @staticmethod
    def say_hi(name):
        print("Hi,", name)


groups = ["11-202", "11-204", "11-206", "11-208", "11-210"]
names = ["Aliya", "Nikita", "Kirill", "Bob", "Thomas"]
cities = [
    "Kazan",
    "Moscow",
    "St-Petersburg",
]
obr_level = ["general", "special", "higher", "second higher"]
pr_lngs = ["C++", "C#", "Python", "Java", "JavaScript"]
jobs = [
    "self-employed",
    "Data analyst",
    "Development manager",
    "Developer",
    "Engineer",
    "Frontend Developer",
    "Backend Developer",
]

students = []
for i in names:
    students.append(
        Student(
            i,
            r.choice(groups),
            r.randint(18, 25),
            r.choice(cities),
            r.choice(obr_level),
            r.choice(pr_lngs),
            r.choice(jobs),
        )
    )
for i in range(len(students)):
    students[i].introduce()
    students[i].old()
    students[i].location()
    students[i].obr()

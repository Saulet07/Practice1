class Base:
    def __init__(self, job, name, salary, bonus):
        self.job = job
        self.name = name
        self.salary = salary
        self.bonus = bonus
    def res(self):
        if self.job == "Manager":
            x = self.salary * (1 + self.bonus / 100)
        elif self.job == "Developer":
            x = self.salary + self.bonus * 500
        elif self.job == "Intern":
            x = self.salary
        else:
            x = self.salary
        print(f"Name: {self.name}, Total: {x:.2f}")

a = input().split()
job = a[0]
name = a[1]
salary = int(a[2])
if job == "Intern":
    bonus = 0
else:
    bonus = int(a[3])
Base(job, name, salary, bonus).res()

class Time:
    def __init__(self, time):
        self.time = time

    def __add__(self, othertime):
        return Number(self.time + self.othertime)

    def __repr__(self):
        return f"Number({self.time})"

    def show(self):
        print(self.time, ":", self.othertime)

t1 = Time(10,50)
t2 = Time(10,10)
print(t1 + t2)

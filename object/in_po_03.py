class Bird:
    def fly(self):
        return "새가 날고 있습니다."

class Penguin(Bird):
    def fly(self):
        return "펭귄은 날지 못합니다."

b = Bird()
p = Penguin()

print(b.fly())
print(p.fly())
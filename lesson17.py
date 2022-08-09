class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name



    def __repr__(self):
        return f"__repr__ method: {self.first_name} {self.last_name}"

user = User("Vasya", "Pypkin")
print(f"{repr(user)}")
# или лучше воспользоваться !r
print(f"{user!r}")

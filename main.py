from unicodedata import name


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks,score, change_name, change_age,add_track, get_score):
        pass
        self.name = str(name)
        self.age = int(age)
        self.tracks = tracks
        self.score = float(score)

        self.change_name =change_name
        self.change_age = change_age
        self.add_track = add_track
    
    def get_score(self):
        return self.score


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90, change_name=input("Enter new name: "), change_age=int(input("Enter new age: ")), add_track=input("Enter new track:"), get_score=())
print(Bob.name)
print(Bob.age)
print(Bob.tracks)
print(Bob.score)
print(Bob.change_name)
print(Bob.change_age)
print(Bob.add_track)
print(Bob.get_score())

# Expected methods

Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()



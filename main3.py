class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self,new_name):
        self.name = new_name

    def Change_age(self, new_age):
        self.age = new_age

    def Add_track(self, new_track):
        self.tracks.append(new_track)

    def get_score(self):
        print(self.score)
        

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.Change_age(34)
Bob.Add_track("UI/UX")
Bob.get_score()
print(Bob.tracks)

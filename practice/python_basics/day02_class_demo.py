from typing import List
class Student:
    def __init__(self, name: str, score: int):
        self.name = name
        self.score = score
    
    def is_passed(self) -> bool:
        return self.score >= 60
    
    def to_dict(self) -> dict:
        return {"name": self.name, "score": self.score}
    
    def __str__(self) -> str:
        return f"Student(name={self.name}, score={self.score})"
    
def main():
    s1 = Student("Alice", 90)
    s2 = Student("Bob", 55)

    print(s1)
    print(f"{s1.name},{s1.is_passed}")
    print(f"{s2.name},{s2.is_passed}") 

    student_list:List[Student] = [s1,s2]

    dict_list = [stu.to_dict() for stu in student_list]

    print(f"{dict_list}")

if __name__ == "__main__":
    main()
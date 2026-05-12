from dataclasses import dataclass,asdict

@dataclass
class StudentData:
    name: str
    score: int
    def is_passed(self) -> bool:
        return self.score >= 60
    
def main():
    s1 = StudentData("Charlie", 88)

    print(s1)
    print(f"{s1.is_passed()}")
    print(f"自动转字典：{asdict(s1)}")

if __name__ == "__main__":
    main()
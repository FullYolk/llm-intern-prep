import json
import os
from typing import List

BASE_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(BASE_DIR,"students.json")#自动识别操作系统路径

def load_students() -> List[dict]:
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_students(students: List[dict]):
    with open(DATA_FILE,"w",encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=2)
    return

def show_students(students: List[dict]):
    print("All students")
    for s in students:
        print(f"name:{s['name']}, score:{s['score']}")
    return

def add_student(students: List[dict],name: str, score: int):
    if find_student(students, name) is not None:
        return False
    s = {"name": name,"score": score}
    students.append(s)
    return True

def find_student(students: List[dict], name: str) -> dict | None:
    for s in students:
        if s["name"] == name:
            return s
    return None

def delete_student(students: List[dict], name: str) -> bool:
    for s in students:
        if s["name"] == name:
            students.pop(s)
            return True
    return False
    
def sort_students(students: List[dict]) -> List[dict]:
    return sorted(students, key=lambda x: (-x["score"], x["name"]))# 默认reverse = False(升序排列)

def get_average_score(students: List[dict]) -> float:
    if not students:
        return 0.0
    return sum(s["score"] for s in students) / len(students)

def update_student_score(students:List[dict], name:str, score:int) -> bool:
    student = find_student(students, name)
    if student is None:
        return False
    student["score"] = score
    return True

def main():
    # 1. 启动时先加载数据
    students = load_students()
    
    # 如果没数据，我们初始化两条
    if not students:
        add_student(students, "Alice", 90)
        add_student(students, "Bob", 75)
    
    show_students(students)
    
    print("\n[测试] 增加新学生 Charlie 88分")
    add_student(students, "Charlie", 88)
    
    print("\n[测试] 查找 Alice")
    alice = find_student(students, "Alice")
    print(f"找到了: {alice}")
    
    print("\n[测试] 降序打印")
    sorted_stus = sort_students(students)
    show_students(sorted_stus)
    
    print("\n[测试] 删除 Bob")
    delete_student(students, "Bob")
    show_students(students)
    # 2. 退出前保存数据
    save_students(students)
    print("\n数据已保存到 JSON 文件。你可以打开 students.json 看看！")
if __name__ == "__main__":
    main()
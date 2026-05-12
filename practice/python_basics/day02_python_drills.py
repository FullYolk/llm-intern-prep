from typing import List
import json
def delete_repetition(nums: List[int]) -> List[int]:
    return list(set(nums))
def count_words(text: str) -> dict:
    result = {}
    words = text.split()
    for word in words:
        result[word] = result.get(word, 0) + 1 ##get的第二个参数
    return result
def sort_scores(students: List[dict]) -> List[dict]:
    return sorted(students, key=lambda x: x["score"], reverse=True)##True为降序 False为升序
def get_passed(students: List[dict]) -> List[dict]:
    return [student for student in students if student["score"] >= 60]
def use_enumerate(fruits:List):
    hash_map = {}
    for i, word in enumerate(fruits):
        hash_map[i] = word
    print(hash_map)
    
    return
def use_zip(head:List,tail:List)->dict:
    return dict(zip(head,tail))
def write_json(data:dict):
    with open("day02_drill.json","w",encoding="utf-8") as f:
        json.dump(data,f,ensure_ascii=False,indent=2)
    print("json写入完成！")
    return
def read_json():
    with open("day02_drill.json","r",encoding="utf-8") as f:
        data = json.load(f)
    print(f"读取到的类型是：{type(data)}")
    print(f"读取到的内容是：{data}")
    return data
def main(): ##main函数由AI生成
    print("=== Test 1: 列表去重 ===")
    nums = [1, 2, 2, 3, 4, 4, 5]
    print(f"原列表: {nums}")
    print(f"去重后: {delete_repetition(nums)}\n")
    print("=== Test 2: 统计单词频率 ===")
    text = "apple banana apple orange banana apple"
    print(f"文本: {text}")
    print(f"统计结果: {count_words(text)}\n")
    print("=== Test 3 & 4: 学生成绩排序与筛选 ===")
    students = [
        {"name": "Alice", "score": 85},
        {"name": "Bob", "score": 55}, # 不及格
        {"name": "Charlie", "score": 92},
        {"name": "David", "score": 40}  # 不及格
    ]
    print(f"按成绩降序: {sort_scores(students)}")
    print(f"筛选及格者: {get_passed(students)}\n")
    print("=== Test 5: enumerate 遍历 ===")
    fruits = ["apple", "banana", "cherry"]
    use_enumerate(fruits)
    print() # 打印空行换行
    print("=== Test 6: zip 合并字典 ===")
    keys = ["id", "name", "role", "skill"]
    values = ["001", "Xiaoyi", "Agent", "Python"]
    my_dict = use_zip(keys, values)
    print(f"合并后的字典: {my_dict}\n")
    print("=== Test 7 & 8: JSON 持久化读写 ===")
    # 刚才生成的 my_dict 里包含了中文字符，正好测试 ensure_ascii=False
    write_json(my_dict)
    loaded_dict = read_json()



if __name__ == "__main__":
    main()



    
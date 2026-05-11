def getAverage(nums):
    if not nums:
        return 0
    return sum(nums)/len(nums)
def count_chars(s):
    result = {}
    for ch in s:
        result[ch] = result.get(ch, 0) + 1
    return result
def main():
    nums = [85,90,78,92,88]
    avg = getAverage(nums)
    print("average:",avg)
    text = "Hello Agent"
    char_count = count_chars(text)
    with open("day01_output.txt","w",encoding="utf-8") as f:
        f.write(f"average:{avg}\n")
        f.write(f"char_count:{char_count}\n")
if __name__ == "__main__":
    main()
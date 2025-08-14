from concurrent.futures import ThreadPoolExecutor


def mul_by_5(num : int, num2) : 
    print(num2)
    return 5 * num
nums = [1,2,3]
with ThreadPoolExecutor(max_workers=3) as execuator :
    results = execuator.map(mul_by_5, nums, [3,3,3])
print(list(results))
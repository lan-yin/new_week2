
# 要求一:函式與流程控制

def calculate(min, max, step):
# 請用你的程式補完這個函式的區塊
    result = 0
    if max > min :
        for i in range(min, max+1, step):
            result = result + i
    print(result) 

calculate(1, 3, 1) # 你的程式要能夠計算 1+2+3，最後印出 6 
calculate(4, 8, 2) # 你的程式要能夠計算 4+6+8，最後印出 18 
calculate(-1, 2, 2) # 你的程式要能夠計算 -1+1，最後印出 0



# # 要求二:Python 字典與列表、JavaScript 物件與陣列

def avg(data):
# 請用你的程式補完這個函式的區塊 
    sum = 0
    j = 0 
    for i in range(len(data["employees"])):
        if data["employees"][i]["manager"] == False:
            sum = sum + int(data["employees"][i]["salary"])
            # print(sum)
            j += 1
        else:
            continue
    print(sum/j) 


avg({
    "employees":[ 
        {
            "name":"John", 
            "salary":30000, 
            "manager":False
        }, 
        {
            "name":"Bob", 
            "salary":60000, 
            "manager":True
        },
        {
            "name":"Jenny", 
            "salary":50000, 
            "manager":False
        },
        {
            "name":"Tony", 
            "salary":40000, 
            "manager":False
        },
    ]
})

# 呼叫 avg 函式



# 要求三：完成以下函式，最後能印出程式中註解所描述的結果。

def func(a):
# 請用你的程式補完這個函式的區塊
    def mul(b, c):
        result = a + b * c
        print(result)
    return mul

func(2)(3, 4) # 你補完的函式能印出 2+(3*4) 的結果 14 
func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0 
func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15 
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果



# # 要求四:找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。

def maxProduct(nums):
# 請用你的程式補完這個函式的區塊 
    max = nums[0] * nums[1]
    for i in range(len(nums)):
        n1 = nums[i]
        for j in range(i+1, len(nums)):
            if n1 * nums[j] > max:
                max = n1 * nums[j]
            else:
                continue
    print(max)

maxProduct([5, 20, 2, 6]) # 得到 120 
maxProduct([10, -20, 0, 3]) # 得到 30 
maxProduct([10, -20, 0, -3]) # 得到 60 
maxProduct([-1, 2]) # 得到 -2 
maxProduct([-1, 0, 2]) # 得到 0 
maxProduct([5,-1, -2, 0]) # 得到 2 
maxProduct([-5, -2]) # 得到 10



# 要求五: Given an array of integers, show indices of the two numbers such that they add up to a specific target. You can assume that each input would have exactly one solution, and you can not use the same element twice.

def twoSum(nums, target):
# your code here
    for i in range(len(nums)):
        n1 = nums[i]
        for j in range(i+1, len(nums)):
            if n1 + nums[j] == target:
                return [i, j]
                break

result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9



# # 要求六 ( Optional ): 給定只會包含 0 或 1 兩種數字的列表 (Python) 或陣列 (JavaScript)，計算連續出現 0 的最大長度。

def maxZeros(nums):
    # 請用你的程式補完這個函式的區塊
    zeros = []
    zero = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            zero +=1
            if i == len(nums)-1:
                zeros.append(zero)
        elif nums[i] != 0:
            zeros.append(zero)
            zero = 0
    max = zeros[0]
    for i in range(len(zeros)):
        if max < zeros[i]:
            max = zeros[i]
        else:
            continue
    print(max)
 
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4 
maxZeros([1, 1, 1, 1, 1]) # 得到 0 
maxZeros([0, 0, 0, 1, 1]) # 得到 3


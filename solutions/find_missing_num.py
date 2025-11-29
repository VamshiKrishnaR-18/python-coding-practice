nums = [3,0,1,2]

n = len(nums)

res = n #3

for i in range(n):

    print(f"{res} ^ {i} ^ {nums[i]}")

    res = res ^ i ^ nums[i]
    print(res)


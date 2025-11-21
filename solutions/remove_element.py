# Remove Element (LeetCode 27)
def remove_element(nums, val):
    write = 0
    for read in range(len(nums)):
        if nums[read] != val:
            nums[write] = nums[read]
            write += 1
    return write  # new length

if __name__ == "__main__":
    arr = [3,2,2,3]
    new_len = remove_element(arr, 3)
    print(new_len, arr[:new_len])  # 2 [2,2]

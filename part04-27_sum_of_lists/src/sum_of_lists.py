# Write your solution here
def list_sum(nums1: list, nums2: list): 
    sumList = []

    for i in range(0, len(nums1), 1):
        sumList.append(nums1[i] + nums2[i])
    
    return sumList

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]

    print(list_sum(a, b))
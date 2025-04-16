# Problem Link: https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer

# Time Complexity: O(n)
# Space Complexity: O(1)

def maximumCount(nums):
    positive = 0    # Variable to count positve numbers
    negative = 0    # Variable to count negative numbers

    for n in nums:
        # increment value for negative variable.
        if n < 0:
            negative += 1
        # increment value for positive variable.
        if n > 0:
            positive += 1

    return max(positive, negative)  # return maximum count from both variables

def main():
    # Test - 1
    nums1 = [-2,-1,-1,1,2,3]
    print(f"output-1: {maximumCount(nums1)}")

    # Test - 2
    nums2 = [-3,-2,-1,0,0,1,2]
    print(f"output-2: {maximumCount(nums2)}")

    # Test - 3
    nums3 = [5,20,66,1314]
    print(f"output-3: {maximumCount(nums3)}")

if __name__ == "__main__":
    main()

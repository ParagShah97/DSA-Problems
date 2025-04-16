# Problem Link: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters

# Time Complexity: O(n)
# Space Complexity: O(1)

from collections import defaultdict

def numberOfSubstrings(s):
    output = 0
    left = 0                        # Initialize the left pointer for the sliding window
    ch_map = defaultdict(int)       # Create a dictionary to count the occurrences of each character within the sliding window

    # Iterate over the string with the right pointer to expand the window
    for right in range(len(s)):
        ch_map[s[right]] += 1       # In every iteration increment the count of the current character at the 'right' pointer

        # Iterate While the sliding window contains all three characters ('a', 'b', and 'c')
        while len(ch_map) == 3:
            # Add number of all substrings, here we can say every substrings from window to end of the string is valid.
            output += len(s) - right

            # Decrement the count of the char at left pointer to move window.
            ch_map[s[left]] -= 1

            # If count of that character is zero means we dont have that char in window so delete it from dictionary.
            if ch_map[s[left]] == 0:
                del ch_map[s[left]]

            left += 1

    return output

def main():
    # Test - 1
    s1 = "abcabc"
    print(f"output-1: {numberOfSubstrings(s1)}")

    # Test - 2
    s2 = "aaacb"
    print(f"output-2: {numberOfSubstrings(s2)}")

    # Test - 3
    s3 = "abc"
    print(f"output-3: {numberOfSubstrings(s3)}")

if __name__ == "__main__":
    main()

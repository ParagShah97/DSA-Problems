# Problem: https://leetcode.com/problems/roman-to-integer
# Time Complexity O(N)
# Space Complexity O(N)
class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Intuition:
        Here we can keep a dictionary for roman to integer value and sepcial cases for
        I,X,C and their respective next roman number in a set.
        Next will iterate over roman string. from i =0 to N.
        For condition see the inline comments.
        """

        i =0
        roman = {'I': 1, 'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000,}
        conercases = {'I': set(['V', 'X']),'X': set(['L', 'C']), 'C': set(['D', 'M'])}
        total = 0
        while i < len(s):
            # If the chars are different from special chars then just add to the total.
            if s[i] not in conercases:
                total += roman[s[i]]
                i +=1 
            else:
                # If char are special and their next element in set() val
                # then we have to decrement the currect value from the next value and
                # add overall to total.
                if i+1 < len(s) and s[i+1] in conercases[s[i]]:
                    total += roman[s[i+1]] - roman[s[i]]
                    i += 2
                else:
                    # Else we just add to total.
                    total += roman[s[i]]
                    i+=1

        return total
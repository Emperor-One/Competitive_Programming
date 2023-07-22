class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = []
        for char in s:
            if char.isalnum():
                new.append(char.lower())
        new_string = ''.join(new)
        i = len(new_string) - 1
        reversed_string = ""
        while i >= 0:
            reversed_string += new_string[i]
            i -= 1
        if reversed_string == new_string:
            return True
        return False
            

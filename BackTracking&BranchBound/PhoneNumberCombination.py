# -- coding:utf-8 --

#  Letter Combinations of a Phone Number (Medium)


#     1:O_O    2:abc     3:def
#     4:ghi    5:jkl     6:mno
#     7:pqrs   8:tuv     9:wxyz
#     *:+      0:blank   shift:#


# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].


Keys = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']



def letterCombinations(digits):
    combinations = []
    if digits is None or len(digits) == 0:
        return combinations

    doCombinations('',combinations,digits)
    return combinations


def doCombinations(prefix,combinations,digits):
    if len(prefix) == len(digits):
        combinations.append(prefix)
        return

    curDigits = int(digits[len(prefix)])
    letters = Keys[curDigits]
    for c in letters:
        prefix += c
        doCombinations(prefix,combinations,digits)
        prefix = prefix[:-1]



if __name__ == "__main__":
    digits = "23"
    print(letterCombinations(digits))




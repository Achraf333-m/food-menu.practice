palind = input("Enter a word and see if it's a palindrome or not!:")


def isPalindrome(palind):
    l = 0
    r = len(palind) - 1
    while l < r:
        if palind[l] == palind[r]:
            l += 1
            r -= 1
        else:
            print("This word is not a palindrome")
            break
        print("this word is a palindrome")
        break

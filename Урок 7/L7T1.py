word = input()

if (word.lower()[::1]) == (word.lower()[::-1]):
    print("Yes")
else:
    print("No")

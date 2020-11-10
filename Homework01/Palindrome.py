def JudgePalindrome(InputString):
    IS = []
    for i in range(0, int(len(InputString))):
        if InputString[i] != " ":
            IS.append(InputString[i])
    flag = True
    for i in range(0, int(len(IS) / 2)):
        if IS[i] == IS[len(IS) - i - 1]:
            flag = True
        else:
            flag = False
            break
    if flag:
        print("\"" + InputString + "\"" + " is a Palindrome")
    else:
        print("\"" + InputString + "\"" + " is not a Palindrome")

while True:
    InputString = input("Please enter a sentence or a word (Enter \"Quit\" to leave): ")
    if InputString == "Quit":
        break
    else:
        JudgePalindrome(InputString)

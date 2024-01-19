while True:
    try:
        s, t = input().split()
        checkSum = 0
        result = ""
        for i in range(len(t)):
            if t[i] == s[checkSum]:
                result += s[checkSum]
                checkSum += 1
                if result == s:
                    print("Yes")
                    break
        else:
            print("No")
    except EOFError:
        break
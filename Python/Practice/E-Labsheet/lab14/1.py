def count_char(word):
    dic = {}
    for i in word :
        if i.isalpha():
            i = i.lower()
            if i in dic :
                dic[i] += 1
            else :
                dic[i] = 1
    return dic

print(count_char('Hello, There'))
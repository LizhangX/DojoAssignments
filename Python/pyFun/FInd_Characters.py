

def FindCharacter(str1,str2):
    str3 = []
    for i in str1:
        if i.find(str2) == -1:
            continue
        else:
            str3.append(i)
    print str3

word_list = ['hello','world','my','name','is','Anna']
char = 'o'

FindCharacter(word_list, char)
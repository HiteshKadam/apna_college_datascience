#p1

def get_word(file,word):
    line_num = 0
    with open(f"{file}","r") as f:
        for i in f.readlines():
            if word in i :
                line_num +=1
                return line_num
        return f"{word} not present"

print(get_word("practice.txt","Python"))
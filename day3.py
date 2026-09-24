#Strings

word1 = "I love"
word2 = "python"

#concat
print(word1 +" "+ word2)

# Indexing
print(word2[2])

#Slicing
sentence = "I only study from apna college"
print(sentence[13:])

#String formating
a =5
b = 10
print(f"sum of {a} and {b} is 15")


#List
numbers = [12,2,3,345,363,463,412,13]

print(type(numbers))
print(numbers[0:len(numbers)])
numbers.append(0)
numbers.insert(1,10)
numbers.sort()
numbers.reverse()
print(numbers)

#Tuples

tup = (1,2,3,4,5,5,"abc",3.14)
print(type(tup))

print(tup[:3])

print(tup.index(5))

#Dictionary
info = {
    "name":"hitesh",
    "age":26,
    "score":97
}

print(type(info))
print(info["name"]) # error is thrown

info["name"] = 25
print(info["name"])

print(info.keys())
print(info.values())
print(info.items())

print(info.get("name")) #no error none is thrown
info.update({"city":"Mumbai"})
print(info)



# Set
num = {1,2,3,4,5,6,6}

empty_set = set()

print(type(empty_set))
num.add(9)

num.remove(1)
# num.clear()
num.pop()
print(num)


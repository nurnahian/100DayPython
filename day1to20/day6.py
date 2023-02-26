# List items are ordered, changeable, and allow duplicate values
listx = ["apple", "banana"]
print(type(listx))
# A tuple is a collection which is ordered and unchangeable.
tuplex = ("banana","apple")
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
setx = {2,1,3}

print(tuplex)
print(setx)

#  Dictionary is a collection which is ordered** and changeable. No duplicate members.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

thdict = dict(name="John",age=36,country="Norway")
print(thdict)


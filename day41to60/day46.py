import os
# print(dir(os))
# if not os.path.exists("data"):
#     os.mkdir("data")
#
# for i in range(0,100):
#     os.mkdir(f"data/Day{i+1}")

folder = os.listdir("data")
print(len(folder))
# print(folder)
for fol in folder:
    print(fol)
    print(os.listdir(f"data/{fol}"))

# print(os.getcwd())
os.chdir("/Users/Nahian/Desktop/Py")
print(os.getcwd())
# for i in folder:
#     print(i)
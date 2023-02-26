import os

folder = r''

count =1

for file_name in os.listdir(folder):
    source = folder+file_name

    destination = folder + "file_"+str(count) + ".txt"
    os.rename(source,destination)
    count = count+1


res = os.listdir(folder)
print(res)
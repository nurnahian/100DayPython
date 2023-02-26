for i in range(12):
    if i == 10:
        print("Skip")
        continue
    print("5 X",i+1, "=",5*(i+1))
print("Next For")
for i in range(12):
    if i == 10:
        break
    print("5 X",i+1, "=",5*(i+1))
print("Break Loop")
questions = [

    ["I have a green tree,To shade me from ____", "sun", "Dirt", "Cloth", "None of these", 1],
    ["I often sit under ____", "Rain", "Sun", "Tree", "None of these", 3],
    ["Grand father is father of your ____", "Father", "Sister", "Brother", "Non of these", 1]

]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]

money = 0

i = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"Question for TK: {levels[i]}")
    print(f"a. {question[1]}        b. {question[2]}")
    print(f"c. {question[3]}        b. {question[4]}")
    reply= int(input("Enter your answer (1-4) : "))
    if reply == 0:
        money = levels[i-1]
        break
    elif reply == question[-1]:
        print(f"Correct answer,you have won Rs{levels[i]}")
        if i == 4:
            money = 10000
        elif i == 9:
            money = 32000
    else:
        print("Wrong answer!")
        break
print(f"You are won TK {money}")

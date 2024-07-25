import random

cont = [1, 2, 3, 4]      
nums = []

com = random.randint(1, 4)
for i in range(com):
    nums.append(cont[i])

print("The computer has moved")
print(nums)

while nums[-1] != 21:
    if nums[-1] == 20:
        print("Congrats, you won!!")
        break

    x = int(input("How many numbers?: "))
    if x > 4 or x < 1:
        print("Please choose a number between 1 and 4")
        continue  
    
    for j in range(x):
        if nums[-1] == 21:
            break  

        z = int(input("Enter number: "))
        if z != nums[-1] + 1:
            print("Incorrect order. You need to enter numbers in sequence.")
            break  
        else:
            nums.append(z)
    
    if nums[-1] == 21:
        print("Congrats, you won!!")
        break

    dox = random.randint(1, 4)
    for k in range(dox):
        if nums[-1] == 21:
            break  

        nums.append(nums[-1] + 1)
    
    print("The computer has moved")
    print(nums)
    print("Your Turn")

if nums[-1] == 21:
    print("The computer won!!")

            




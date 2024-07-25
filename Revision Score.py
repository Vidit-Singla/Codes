topics= ['Mechanics','Engineering Drawing','Graphics,Engineering Drawing', 'Graphics Electrical Technology','Introduction to Manufacturing Processes']
n=len(topics)
rev_score=0
for i in range(n):
    print(topics[i])
    x=input("Did you finish this topic(Y/N)?: ")
    if x.capitalize()=="Y":
        rev_score+=1
    else:
        continue

percentage= rev_score/n
print("Your revision score is :",percentage*100,"%")
print("welcome to my computer quiz")
playing=input("do u want to play?")
if playing.lower() !="yes":
    quit()
print("okay! lets play:")
score=0

answer=input("what does cpu stands for?")
if answer.lower()=="central processing unit":
    print("correct!")
    score+=1
else:
    print("incorrect!")

answer=input("what does GPU stands for?")
if answer.lower()=="graphics processing unit":
    print("correct!")
    score+=1
else:
    print("incorrect!")

answer=input("what does ram stands for?")
if answer.lower()=="random access memory":
    print("correct!")
    score+=1
else:
    print("incorrect!")

answer=input("what does psu stands for?")
if answer.lower()=="power supply unit":
    print("correct!")
    score+=1
else:
    print("incorrect!")

print("you got"+str(score)+"question correct")
print("you got"+str((score/4)*100)+"%")
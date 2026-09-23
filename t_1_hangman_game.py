import random
print("welcone to hangman game")
# printing the rules of the game 
print("RULES\n1.THERE WILL BE A HIDDEN WORD AND YOU YOU HAVE TO GUESS THE WORD BY GUESSING ITS LETTER ONE BY ONE\n2.IF THE LETTER YOU GUESSED IS PRESENT IN THE WORD THEN THEN YOU CAN SEE ITS POSITION\n YOU WILL BE GIVEN ONLY 6 CHANCES SO BE CAREFULL\n GAME START")
# list of the all hidden words
l=["apple","banana","cherry","notebook","laptop"]

r=random.choice(l)
s=[ ]
k=0
o=0
for e in r:
    s.append(e)
print(f"the length of the word is {len(s)}")
while(o<6):
        for i in range(len(s)):
                count=0
                c=input("enter your choice:")
                for j in range(len(s)):
                    if(s[j]==c):
                        print("element is present in the given word at ",j+1,"place")
                        s[j]=0
                        count+=1
                        k+=1
                        break
                    else:
                        pass
                if(count==0):
                    print("element is not found")
                    print(f"you are lef with {6-(o+1)} chances")
                    o+=1
                if(len(s)==k):
                    o+=6
                    break
if(k==len(s)):
     print("congrats you won the game ")
else:
     print("you lose the game")
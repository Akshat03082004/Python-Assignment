            #ROCK PAPER AND SCISSORS#

import random

#g=random.choice(['rock','paper','scissor'])


print("Please enter your choice:")
print(" 1.ROCK \n",
      "2.PAPER \n",
      "3.SCISSOR \n",
      "4.EXIT")
#c=input("ENTER THE CHOICE: ")
while True:
    g=random.choice(['rock','paper','scissor'])
    c=input("ENTER THE CHOICE: ")
    if g=='rock' and c=='2':
        print("YOU WIN")
        

    elif g=='paper' and c=='3':
        print("YOU WIN")
        

    elif g=='scissor'and c=='1':
        print("YOU WIN")
        

    elif c=='exit':
        print("THANKYOU!!")
        break
    else:
        print("YOU LOST")
        
    

        

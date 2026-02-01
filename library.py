 import random
 play=True
 attempts=0
 num=random.randint(10,20)

 while play:
     guess=int(input("Guess the correct number between 10 and 20: "))
     attempts+=1
     if guess==num:
         print(f"Yay, you guessed the correct number in {attempts} attempts!")
         play=False
     else:
         print("Try Again")

import math
print(math.ceil(23.4))
print(math.floor(23.4))
print(math.lcm(4,8))
print(math.gcd(8,16))

print(math.factorial(60))

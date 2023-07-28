import random 
import math
data="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
lenth=len(data)

otp=""
for i in range (6):
    otp+=data[math.floor(random.random()*lenth)]
print("Your otp is ",otp)

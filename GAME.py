import random
list1 = ['python','java','php','C++','C#']
ans = random.choice(list1)
print("This is List Guess The Correct Word : ",list1)
count = 1 
while count <= 6:
  a = input("Enter Your Choice")
  if a == ans:
    print("Correct Answer")
    break
  else:
    print("Wrong Answer")
    count+=1
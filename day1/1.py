#/usr/bin/env python
age=30
num=3

while num>0:
  Age=int(input("Age:"))
  if Age == age:
      print("ok")
      break
  elif Age > age:
      print("older")
  else:
      print("yonger")
  num -= 1
  if num ==0:
      confire=input("can you three try again:")
      if confire !="N":
          num=3

# else:
#     print("you have tried too many times.")

'''
for i in range(3):
    Age = int(input("Age:"))
    if Age == age:
        print("ok")
        break
    elif Age > age:
        print("older")
    else:
        print("yonger")
else:
    print("you have tried too many times.")
'''
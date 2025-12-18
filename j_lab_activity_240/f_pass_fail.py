math = int(input("Enter Mathematics marks: "))
cs = int(input("Enter Computer Science marks: "))
nep = int(input("Enter Nepali marks: "))
eng = int(input("Enter English marks: "))
sci = int(input("Enter Science marks: "))

if math > 35 and cs > 35 and nep > 35 and eng > 35 and sci > 35:
    print("Your result is passed.")
else:
    print("Your result is failed.")

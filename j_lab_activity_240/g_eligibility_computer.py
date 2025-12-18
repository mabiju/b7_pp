math = int(input("Enter Mathematics marks: "))
cs = int(input("Enter Computer Science marks: "))
nep = int(input("Enter Nepali marks: "))
eng = int(input("Enter English marks: "))
sci = int(input("Enter Science marks: "))

if math > 80 or cs > 80 or nep > 80 or eng > 80 or sci > 80:
    print("You are eligible to study computer science.")
else:
    print("You are not eligible to study computer science.")

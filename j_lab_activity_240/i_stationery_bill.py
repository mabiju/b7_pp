pen = int(input("Enter quantity of pen: "))
notebook = int(input("Enter quantity of notebook: "))
pencil = int(input("Enter quantity of pencil: "))

gt = (pen * 50) + (notebook * 100) + (pencil * 10)

if gt > 5000:
    discount = gt * 0.05
else:
    discount = 0

nt = gt - discount

print("Gross Total:", gt)
print("Discount:", discount)
print("Net Total:", nt)

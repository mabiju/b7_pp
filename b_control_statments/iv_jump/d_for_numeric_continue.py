# Example of a for loop with a continue statement
for x in range(6):
    # prints numbers from 0 to 5, continues when x is 3, i.e. skips 3,  i.e. 0,1,2,4,5
    if x == 3:
        continue
    print(x)

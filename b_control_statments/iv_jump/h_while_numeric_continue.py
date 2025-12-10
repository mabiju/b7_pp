# Example of a while loop with a continue statement
i=0
while i<=6:
    # prints numbers from 0 to 6, continues when i is 3, i.e. skips 3, i.e. 0,1,2,4,5,6
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1
    

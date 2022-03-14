i = 1
while i <=10:
    if i==5:
        i = i+1
        continue
    
    print(i ,end=' ')
    i = i+1


print()

# break

for j in range(10):

    if j==5:
        break
    print(j,end=" ")

print()

# continue

for k in range(10):

    if k==4:
        continue
    print(k,end=" ")
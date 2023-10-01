num = []
for i in range(1500,2701):
    if(i %7 ==0 and i % 5 == 0):
        num.append(str(i))

print(','.join(num))
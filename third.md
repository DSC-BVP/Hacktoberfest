print("program to delete duplicate values in a list without using inbuilt function")
x=[1,2,1]
x.sort()
i = len(x) - 1
while i > 0:
    if x[i] == x[i - 1]:
        x.pop(i)
    i -= 1
print(x)

import Functions

# Combination

x = [1,2,3,4,5,6,7,8,9]

# Return value = i
y = [Functions.add3(i) for i in x]

y.append(65)

print(x)
print(y)

# using enumerate for list
# for index,value in enumerate(y):
#     Functions.add(value)





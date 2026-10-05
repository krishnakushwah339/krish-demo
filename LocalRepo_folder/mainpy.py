print("this is a NewRepo")

data = [10, 20, 30, 40, 50]
total  = 0
for i in range(len(data)):
    if i % 2 ==1:
        total = total + data[i]
   
print(total)


print('--'*20)

n = 6 
step = 0
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    step += 1
print("Total steps:", step)

print('--'*20)
count  = 0 
for i in range(1,4):
    for j in range(1,4):
        if (i*j) % 2 == 0:
            count += 1
print(count)

print('--'*20)

prod = 1
for i in range(1, 6):
    if i == 3:
        continue
    prod *= i
print(prod)

print('--'*20)

n = 1
steps = 0
while n <=100:
    n *= 2
    steps += 1
print("Total steps:", steps)
print('--'*20)
total = 0 
for i in range(2, 10, 3):
    total = total + i
print(total)

print('--'*20)

result = ''
for i in range(3):
    for j in range(i+1):
        result = result+'*'
print(len(result))

print("--"*20)

result = 0
for i in range(4):
    for j in range(i):
        result = result + 1
print(result)
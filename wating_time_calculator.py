import random
# n = int(input("Enter number of processes: "))
n=4

# gr = int(input("Generate random? (0 for yes / 1 for no): ")) == 0
gr = True

p = [None] * n # process names
at = [None] * n # arrival times
bt = [None] * n # burst times
pi = [None] * n # piorities

if gr:
    for i in range(n):
        bt[i] = random.randint(1, 20)

for i in range(n):
    p[i] = "P" + str(i)
    at[i] = i

print(p)
print(at)
print(bt)
import random
from collections import deque


gr = int(input("Generate random? (0 for yes / 1 for no): ")) == 0
if gr:
    n = int(input("Enter number of processes: "))
    bt= []
    for i in range(n):
        bt.append(random.randint(1, 20))
else: 
    bt = list(map(int, input("Enter brust times(ex. 14 5 6):").split()))
    n = len(bt)
    
choice = int(input("""Choose Scheduling Algorithm:
1. First Come First Serve(FCFS)
2. Round Robin(RR)
-other number to exit-
"""))

#______________ Testing ________________
# gr = True
# n=5
#___ Test dataset For FCFS ________________
# bt = [14, 6, 15, 1]
# bt = [6, 10, 25, 15, 14]
#___ Test dataset For BB ________________
# bt = [4, 8, 3, 11, 7]

p = [None] * n # process names
at = list(range(0, n)) # arrival times

pi = list(range(1, n+1)) # priorities
random.shuffle(pi)

for i in range(n):
    p[i] = "P" + str(i+1)

#_______________________ Print ______________________________
def print_process():
    print(f"{'process':<10} {'Arrival Time':<15} {'Burst Time(ms)':<15} {'Priority':<10}")
    for i in range(n):
        print(f"  {p[i]:<10} {at[i]:<15} {bt[i]:<15} {pi[i]:<10}")

#_______________________ FCFS _____________________________
def fcfs():
    wt = [None] * n
    grantt = 0

    for i in range(n):
        if i == 0: wt[0] = 0
        else: wt[i] = grantt - i
            
        grantt += bt[i]
    
    awt = sum(wt) / n
    return wt, awt

#_______________________ Round Robin(RR) with Time Quantum _____________________________
def rr():
    q = 4
    wt = [None] * n
    grantt = 0
    grantt_points = [0]
    complete = [None] * n
    count = [0] * n

    queue = deque(range(n))

    while queue:
        i = queue.popleft()
        if  bt[i] > q:
            count[i] += 1
            bt[i] -= q
            grantt += q

            grantt_points.append(grantt)
            queue.append(i)
            printChart(i, q)
        else:
            complete[i] = grantt
            grantt += bt[i]

            grantt_points.append(grantt)
            printChart(i, bt[i])
        
    printNumber(grantt_points)
    for i in range(n):
        wt[i] = complete[i] - i - (count[i] * q)
    
    awt = sum(wt) / n
    return wt, awt
#____________________________________________________
def printChart(index, value):
    # print("---------Grantt Chart---------")
    print(f"| {p[index]} ({value}) ", end="|")

def printNumber(points):
    print("\n", end="")
    print(" ".join(f"{point:<9}" for point in points))

#____________________________________________________

if choice == 1: wt, awt = fcfs()
elif choice == 2: wt, awt = rr()
else: exit()

print_process()
print(f"Waiting Times: {wt}")
print(f"Average Waiting Time: {awt:.2f} ms")
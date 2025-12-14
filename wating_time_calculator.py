import random
from collections import deque

#_______________________ Print ______________________________
def print_process(n, p, at, bt, pi):
    print(f"{'process':<10} {'Arrival Time':<15} {'Burst Time(ms)':<15} {'Priority':<10}")
    for i in range(n):
        print(f"  {p[i]:<10} {at[i]:<15} {bt[i]:<15} {pi[i]:<10}")

#_______________________ FCFS _____________________________
def fcfs(n, bt):
    wt = [None] * n
    grantt = 0
    grantt_points = [0]

    for i in range(n):
        if i == 0: wt[0] = 0
        else: wt[i] = grantt - i
            
        grantt += bt[i]
        printChart(i, bt[i])
        grantt_points.append(grantt)
    
    printNumber(grantt_points)
    awt = sum(wt) / n
    return wt, awt

#_______________________ Round Robin(RR) with Time Quantum _____________________________
def rr(n, bt):
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
    print(f"| {p[index]} ({value}) ", end="|")

def printNumber(points):
    print("\n", end="")
    print(" ".join(f"{point:<9}" for point in points))

#____________________________________________________

while True:
    try:
        gr = int(input("Generate random? (0 for yes / 1 for no): ")) == 0
        if gr:
            n = int(input("Enter number of processes: "))
            bt= []
            for i in range(n):
                bt.append(random.randint(1, 20))
        else: 
            bt = list(map(int, input("Enter brust times(ex. 14 6 15 1): ").split()))
            n = len(bt)
            
        choice = int(input("""Choose Scheduling Algorithm:
1. First Come First Serve(FCFS)
2. Round Robin(RR)
"""))

        #______________ Testing ________________
        #___ Test dataset For FCFS ________________
        # bt = [14, 6, 15, 1] # answer = 15.75
        # bt = [6, 10, 25, 15, 14] # answer = 21.8
        #___ Test dataset For BB ________________
        # bt = [4, 8, 3, 11, 7] # answer = 11.6

        p = [None] * n # process names
        at = list(range(0, n)) # arrival times

        pi = list(range(1, n+1)) # priorities
        random.shuffle(pi)

        for i in range(n):
            p[i] = "P" + str(i+1)

        print_process(n, p, at, bt, pi)

        if choice == 1: wt, awt = fcfs(n, bt)
        elif choice == 2: wt, awt = rr(n, bt)
        else: break

        print(f"Waiting Times: {wt}")
        print(f"Average Waiting Time: {awt:.2f} ms")

        cont = int(input("Do you want to continue? (0 for yes / other number for no): "))

        if cont != 0:
            break
    
    except ValueError: print("Invalid input, please try again.")

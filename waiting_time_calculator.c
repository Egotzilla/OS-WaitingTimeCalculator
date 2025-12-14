#include <stdio.h> 
/* importing standard input, output Library */
#include <stdlib.h>
/* importing standard library */
#include <time.h>
/* importing time library for random number generation */
#include <string.h> // for strdup

void shuffle(int *array, int n) {
    for (int i = n - 1; i > 0; i--) {
        int j = rand() % (i + 1);
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
}

static void print_process_table(int n, char *p[], int at[], int bt[], int pi[]) {
    printf("%-15s %-15s %-15s %-15s\n", "Process", "Arrival Time", "Burst Time", "Priority");
    for (int i = 0; i < n; i++) {
        printf("  %-9s\t%-9d\t%-9d\t%d\n", p[i], at[i], bt[i], pi[i]);
    }
}

static void printChart(int index, int value) {
    printf("| P%d (%d) |", index, value);
}

static void printNumber(int points[], int n) {
    printf("\n");
    printf("%-10d", 0);
    for (int i = 0; i < n; i++) {
        printf("%-10d", points[i]);
}
    printf("\n");

}

// __________________ Queue Functions _______________________
int front = 0;
int rear = 0;
int size = 0;
int max = 100;
int queue[100]; 

void enqueue(int value) { // add value to the queue, from behind
    if (size == max) { return;}
    queue[rear] = value;
    rear = (rear + 1) % max; // incase of adding value more than max size, this will loop back to start
    size++;
}

int dequeue() { // remove value from the queue, from front
    if (size == 0) { return -1;}
    int value = queue[front];
    front = (front + 1) % max;
    size--;
    return value;
}

void init_queue(int n) {
    front = 0;
    rear = 0;
    size = 0;
    for (int i = 0; i < n; i++) {
        enqueue(i);
    }
}


// ________________ Sum of array _______________________
int sum(int arr[], int n) {
    int total = 0;

    for (int i = 0; i < n; i++) {
        total += arr[i];
    }
    return total;
}

// _______________ FCFS _______________________
float burst_time(int n, int bt[]) {
    int wt[n];
    int grantt = 0;
    int grantt_points[n];

    for (int i = 0; i < n; i++) {
        if (i == 0) {wt[0] = 0;}
        else { wt[i] = grantt - i;}

        grantt += bt[i];
        printChart(i, bt[i]);
        grantt_points[i] = grantt;
    }

    printNumber(grantt_points, n);
    float awt = sum(wt, n) / (float)n;

    for (int i = 0; i < n; i++) {
        printf("%d ", wt[i]);
    }
    return awt;
}

// _______________ Round Robin(RR) with Time Quantum _______________________
float rr(int n, int bt[]) {
    int q = 4;
    int wt[n];
    int grantt = 0, gp_count = 0;
    int grantt_points[100]; 

    int completed[n], count[n];
    for (int i = 0; i < n; i++) { // set 0 as initial values for completed and count arrays
        count[i] = 0;
        completed[i] = 0;
    }

    init_queue(n);
    while (size > 0) {
        int i = dequeue();
        if (bt[i] > q) {
            count[i]++;
            bt[i] -= q;
            grantt += q;

            grantt_points[gp_count++] = grantt;
            enqueue(i);
            printChart(i, q);
        } else {
            completed[i] = grantt;
            grantt += bt[i];

            grantt_points[gp_count++] = grantt;
            printChart(i, bt[i]);
        }
    }

    printNumber(grantt_points, gp_count);
    for (int i = 0; i < n; i++) {
        wt[i] = completed[i] - i -(count[i] * q);
    }
    
    for (int i = 0; i < n; i++) {
        printf("%d ", wt[i]);
    }
    float awt = sum(wt, n) / (float)n;
    return awt;
}

int main() {
    /* int n = 4;
    // printf("Enter number of processes: ");
    // scanf("%d", &n);

    print_process_table(n, (char *[]){"P1", "P2", "P3", "P4"}, (int[]){0, 1, 2, 3}, (int[]){14, 6, 15, 1}, (int[]){1, 2, 3, 4});
    printf("%d\n", n);
    int bt[] = {14, 6, 15, 1};
    int bt2[] = {4, 8, 3, 11, 7};


    float awt = burst_time(n, bt);
    printf("\n%f", awt);

    float awt2 = rr(5, bt2);
    printf("\n%f", awt2);

    printf("\n"); */

    // ______________________ Interactive Mode _______________________
    while (1) {
        int gr;
        printf("Generate random? (0 True/1 False): ");
        scanf("%d", &gr);
        int n;
        printf("Enter number of processes: ");
        scanf("%d", &n);
        int bt[n];
        if (gr == 0) {
            srand(time(NULL)); // seed for random number generation 
            for (int i = 0; i < n; i++) {
                bt[i] = rand() % 20 + 1; // random burst time between 1 and 20. + 1 to avoid zero and reach 20 instead of 19
            }

        } else {
            printf("Enter brust times(ex. 14 6 15 1): ");
            for (int i = 0; i < n; i++) {
                scanf("%d", &bt[i]);
            }
        }

        int choice;
        printf("Choose Scheduling Algorithm:\n1. First Come First Serve(FCFS)\n2. Round Robin(RR)\n");
        scanf("%d", &choice);

        // _______________ Testing ________________
        // ___ Test dataset For FCFS ________________
        // int bt[] = {14, 6, 15, 1}; // answer = 15.75
        // int bt[] = {6, 10, 25, 15, 14}; // answer = 21.8
        // ___ Test dataset For BB ________________
        // int bt[] = {4, 8, 3, 11, 7}; // answer = 11.6

        char *p[n];
        int at[n];
        int pi[n];
        char pName[4];
        for (int i = 0; i < n; i++) {
            sprintf(pName, "P%d ", i + 1);
            p[i] = strdup(pName);
            at[i] = i;
            pi[i] = i + 1;
        }

        srand(time(NULL)); // seed for shuffling Priority
        shuffle(pi, n);

        // _____________________________
        print_process_table(n, p, at, bt, pi);

        float awt;
        if (choice == 1) {
            awt = burst_time(n, bt);
        } else if (choice == 2) {
            awt = rr(n, bt);
        } else {
            break;
        }

        printf("\nAverage Wating Time: %f\n", awt);
        int cont;
        printf("Do you want to continue? (0 Yes/1 No): ");
        scanf("%d", &cont);
        if (cont == 1) {
            break;
        }
    }
    
}

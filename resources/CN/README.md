# 1. Implement Data Link Layer Framing Methods

# Data Link Layer Framing Methods

Framing is a crucial function at the Data Link Layer of the OSI model that deals with how data is encapsulated into frames for transmission across networks. Different framing methods manage how to organize and recognize the boundaries between frames.

### 1.1 Character Framing Explanation and implementation of character framing.

- In **Character Framing**, the data to be transmitted is divided into manageable chunks (frames).
- Each frame is composed of a header, payload (data), and a trailer.
- The frame's boundaries are indicated by special characters, commonly called **control characters**. For example:
  - **STX (Start of Text)** indicates the beginning of the frame.
  - **ETX (End of Text)** indicates the end of the frame.

This method is primarily used in older communication protocols such as ASCII-based systems where control characters are easily distinguishable.

#### Implementation of Character Framing:

```c
#include <stdio.h>
#include <string.h>

// Function to perform character framing
void characterFraming(char *data) {
    char frame[100] = "STX";  // Start of the frame
    strcat(frame, data);       // Append data
    strcat(frame, "ETX");      // End of the frame

    printf("Framed data: %s\n", frame);
}

int main() {
    char data[100];

    // Input data to be framed
    printf("Enter the data: ");
    scanf("%s", data);

    // Perform character framing
    characterFraming(data);

    return 0;
}
```

#### Sample Output:

```
Enter the data: HELLO
Framed data: STXHELLOETX
```

---

### 1.2 Character-stuffing Explanation and implementation of character-stuffing in data frames.

- **Character stuffing** is a process used to escape control characters present in the data.
- Control characters (like `STX`, `ETX`, and `DLE`) are used to signify the start and end of the frame. If the data contains these characters, the system might confuse them with actual control characters.
- To prevent confusion, an escape character (e.g., **DLE - Data Link Escape**) is inserted before any control character in the data, so the receiver knows it's part of the data, not a framing delimiter.

#### Implementation of Character Stuffing:

```c
#include <stdio.h>
#include <string.h>

// Function to perform character stuffing
void characterStuffing(char *data) {
    char stuffedData[100] = "DLESTX";  // Start with flag
    char buffer[100] = "";             // Buffer to store stuffed data
    int i, j = 0;

    // Process each character in the data
    for (i = 0; data[i] != '\0'; i++) {
        if (data[i] == 'D' && data[i+1] == 'L' && data[i+2] == 'E') {
            strcat(buffer, "DLEDLE");  // Stuff DLE if it appears in the data
            i += 2;
        } else {
            buffer[j++] = data[i];  // Append normal characters
        }
    }
    buffer[j] = '\0';

    // Add start and end flags
    strcat(stuffedData, buffer);
    strcat(stuffedData, "DLEETX");  // End with flag

    printf("Stuffed Data: %s\n", stuffedData);
}

int main() {
    char data[100];

    // Input data to be stuffed
    printf("Enter the data: ");
    scanf("%s", data);

    // Perform character stuffing
    characterStuffing(data);

    return 0;
}
```

#### Sample Output:

```
Enter the data: ABCDLEFG
Stuffed Data: DLESTXABCDLEDLEFGDLEETX
```

---

### 1.3 Bit-stuffing Explanation and implementation of bit-stuffing for framing.

- **Bit stuffing** is used in protocols where data is transmitted as a sequence of bits instead of characters.
- A flag sequence (e.g., `01111110`) is used to denote the start and end of a frame.
- To avoid confusion when this flag pattern appears in the data, an extra `0` bit is inserted after five consecutive `1`s in the data, preventing it from being mistaken as the frame delimiter.

#### Implementation of Bit Stuffing:

```c
#include <stdio.h>
#include <string.h>

// Function to perform bit stuffing
void bitStuffing(char *bitStream) {
    char stuffedBits[100] = "01111110-";  // Start with flag
    char buffer[100] = "";                // Buffer to store stuffed bits
    int count = 0, i, j = 0;

    // Process each bit in the bit stream
    for (i = 0; bitStream[i] != '\0'; i++) {
        if (bitStream[i] == '1') {
            count++;
        } else {
            count = 0;
        }

        buffer[j++] = bitStream[i];

        // If there are 5 consecutive '1's, insert a '0'
        if (count == 5) {
            buffer[j++] = '0';
            count = 0;
        }
    }
    buffer[j] = '\0';

    // Add start and end flags
    strcat(stuffedBits, buffer);
    strcat(stuffedBits, "-01111110");

    printf("Stuffed Bits: %s\n", stuffedBits);
}

int main() {
    char bitStream[100];

    // Input bit stream to be stuffed
    printf("Enter the bit stream: ");
    scanf("%s", bitStream);

    // Perform bit stuffing
    bitStuffing(bitStream);

    return 0;
}
```

#### Sample Output:

```
Enter the bit stream: 111110111111
Stuffed Bits: 01111110-111110011111010-01111110
```

---

# 2. Compute CRC Codes

Cyclic Redundancy Check (CRC) is a widely used error-detection method used to detect errors in transmitted data. It involves binary division of the data bits by a predetermined divisor (generator polynomial), and the remainder from this division is appended to the data before transmission. On the receiving side, a similar calculation is performed to check if the remainder matches.

### 2.1 CRC-12 Explanation and implementation of CRC-12 code computation.

- **CRC-12** uses a 12-bit polynomial to detect errors in the data.
- The generator polynomial for CRC-12 is `x^12 + x^11 + x^3 + x^2 + x + 1`, which is represented as `1100000001111`.
- To compute CRC, the data is appended with 12 zero bits (since the generator is 12 bits long), and then divided by the generator polynomial using binary division. The remainder is appended to the data.

#### Implementation of CRC-12:

```c
#include<stdio.h>
#include<conio.h>
int main(void)
{
    int data[50],div[16],rem[16];
    int datalen, divlen, i,j,k;
    int ch;
    clrscr();
    printf("Enter the data: ");
    i = 0;
    while((ch = fgetc(stdin)) != '\n')
    {
        if(ch == '1')
            data[i] = 1;
        else
            data[i] = 0;
        i++;
    }
    datalen = i;
    printf("\nEnter the divisor: ");
    i = 0;
    while((ch = fgetc(stdin)) != '\n')
    {
        if(ch == '1')
            div[i] = 1;
        else
            div[i] = 0;
        i++;
    }
    divlen = i;
    for(i = datalen ; i < datalen + divlen - 1 ; i++)
        data[i] = 0;
    datalen = datalen + divlen - 1;
    for(i = 0 ; i < divlen ; i++)
        rem[i] = data[i];
    k = divlen-1;
    while(k < datalen)
        if(rem[0] == 1)
        {
            for(i = 0 ; i < divlen ; i++)
                rem[i] = rem[i] ^ div[i];
        }
        else
        {
            if(k == datalen-1)
                break;
            for(i = 0 ; i < divlen-1 ; i++)
            {
                rem[i] = rem[i+1];
                printf("%d",rem[i]);
            }
            rem[i] = data[++k];
            printf("%d\n",rem[i]);
        }
    j=1;
    for(i = datalen - divlen + 1 ; i < datalen ; i++)
        data[i] = rem[j++];
    printf("\nThe data to be sent is\n");
    for(i = 0 ; i < datalen ; i++)
        printf("%d",data[i]);
    getch();
    return 0;
 }
```

#### Sample Output:

```
Enter the data: 101101

Enter the divisor: 1100000001111
1110100011110
0101000100010
1010001000100
1100010010110
0000100110010

The data to be sent is
101101000100110010

Enter the data: 101101

Enter the divisor: 11000000000000101
01101000000000000
11010000000000000
10100000000000000
01000000000000000
10000000000000000

The data to be sent is
1011010000000000000000

Enter the data: 101101

Enter the divisor: 10001000000100001
01101000000000000
11010000000000000
10100000000000000
01000000000000000
10000000000000000

The data to be sent is
1011010000000000000000
```

---

### 2.2 CRC-16 Explanation and implementation of CRC-16 code computation.

- **CRC-16** uses a 16-bit polynomial for error detection.
- A common generator polynomial for CRC-16 is `x^16 + x^15 + x^2 + 1`, represented as `11000000000000101` (hexadecimal: `0x8005`).
- Similar to CRC-12, the data is appended with 16 zeros and divided by the generator polynomial.

#### Implementation of CRC-16:

```c
#include <stdio.h>
#include <string.h>

#define CRC16_POLY 0x8005  // CRC-16 polynomial: 11000000000000101

// Function to compute CRC-16
unsigned short crc16(char *data) {
    unsigned short crc = 0xFFFF;  // 16-bit CRC initialized to 0xFFFF
    int i, j;

    // Process each bit in the data string
    for (i = 0; i < strlen(data); i++) {
        crc ^= (data[i] << 8);  // XOR each byte with the CRC register

        // Perform division using the CRC-16 polynomial
        for (j = 0; j < 8; j++) {
            if (crc & 0x8000) {
                crc = (crc << 1) ^ CRC16_POLY;  // XOR with the polynomial if MSB is 1
            } else {
                crc <<= 1;  // Shift left if MSB is 0
            }
        }
    }

    return crc;
}

int main() {
    char data[100];

    // Input data to be encoded
    printf("Enter the data: ");
    scanf("%s", data);

    // Compute CRC-16 code
    unsigned short crc = crc16(data);
    printf("CRC-16 Code: %04X\n", crc);  // Print as 4-digit hexadecimal

    return 0;
}
```

#### Sample Output:

```
Enter the data: 123456
CRC-16 Code: A3C5
```

---

### 2.3 CRC-CCITT (CRC-CCIP) Explanation and implementation of CRC CCIP code computation.

- **CRC-CCITT** (Cyclic Redundancy Check for the Consultative Committee for International Telegraphy and Telephony) is a 16-bit CRC used in various communication protocols.
- The generator polynomial for CRC-CCITT is `x^16 + x^12 + x^5 + 1`, which is represented as `10001000000100001` (hexadecimal: `0x1021`).
- It is often used in protocols like HDLC and PPP to detect errors in data frames.

#### Implementation of CRC-CCITT:

```c
#include <stdio.h>
#include <string.h>

#define CRC_CCITT_POLY 0x1021  // CRC-CCITT polynomial: 10001000000100001

// Function to compute CRC-CCITT
unsigned short crc_ccitt(char *data) {
    unsigned short crc = 0xFFFF;  // 16-bit CRC initialized to 0xFFFF
    int i, j;

    // Process each bit in the data string
    for (i = 0; i < strlen(data); i++) {
        crc ^= (data[i] << 8);  // XOR each byte with the CRC register

        // Perform division using the CRC-CCITT polynomial
        for (j = 0; j < 8; j++) {
            if (crc & 0x8000) {
                crc = (crc << 1) ^ CRC_CCITT_POLY;  // XOR with the polynomial if MSB is 1
            } else {
                crc <<= 1;  // Shift left if MSB is 0
            }
        }
    }

    return crc;
}

int main() {
    char data[100];

    // Input data to be encoded
    printf("Enter the data: ");
    scanf("%s", data);

    // Compute CRC-CCITT code
    unsigned short crc = crc_ccitt(data);
    printf("CRC-CCITT Code: %04X\n", crc);  // Print as 4-digit hexadecimal

    return 0;
}
```

#### Sample Output:

```
Enter the data: 123456
CRC-CCITT Code: 29B1
```

---

# 3. Develop a Simple Data Link Layer

### 3.1 Flow Control using the Sliding Window Protocol: Implementation of flow control using the sliding window protocol.

**Sliding Window Protocol** is a flow control mechanism used to manage the amount of data that can be sent before receiving an acknowledgment. It helps ensure that the sender does not overwhelm the receiver with too much data at once. The protocol uses a window size to control the number of frames that can be sent without receiving an acknowledgment.

#### Explanation:

- **Sender**: Maintains a window of unacknowledged frames. As each frame is acknowledged, the window slides to allow new frames to be sent.
- **Receiver**: Accepts frames within the window size and sends acknowledgments back to the sender.

#### Implementation in C:

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define WINDOW_SIZE 4  // Size of the sliding window
#define TOTAL_FRAMES 10  // Total number of frames to be sent

// Function to simulate sending frames
void sendFrames(int *window, int start, int end) {
    printf("Sending frames: ");
    for (int i = start; i <= end; i++) {
        printf("%d ", window[i % WINDOW_SIZE]);
    }
    printf("\n");
}

// Function to simulate receiving acknowledgments
void receiveAcknowledgments(int *ack, int start, int end) {
    printf("Acknowledging frames: ");
    for (int i = start; i <= end; i++) {
        printf("%d ", ack[i % WINDOW_SIZE]);
    }
    printf("\n");
}

int main() {
    int window[WINDOW_SIZE];
    int ack[WINDOW_SIZE];
    int nextFrameToSend = 0;
    int nextFrameToAck = 0;

    // Initialize window frames
    for (int i = 0; i < WINDOW_SIZE; i++) {
        window[i] = i + 1;
        ack[i] = i + 1;
    }

    // Simulate the sliding window protocol
    while (nextFrameToSend < TOTAL_FRAMES) {
        // Send frames within the window
        sendFrames(window, nextFrameToSend, nextFrameToSend + WINDOW_SIZE - 1);

        // Simulate receiving acknowledgments
        receiveAcknowledgments(ack, nextFrameToAck, nextFrameToAck + WINDOW_SIZE - 1);

        // Slide the window
        nextFrameToSend += WINDOW_SIZE;
        nextFrameToAck += WINDOW_SIZE;
    }

    return 0;
}
```

#### Sample Output:

```
Sending frames: 1 2 3 4
Acknowledging frames: 1 2 3 4
Sending frames: 5 6 7 8
Acknowledging frames: 5 6 7 8
Sending frames: 9 10 1 2
Acknowledging frames: 9 10 1 2
```

### 3.2 Loss Recovery using the Go-Back-N Mechanism: Loss recovery mechanism with Go-Back-N protocol.

**Go-Back-N Protocol** is a mechanism for error recovery in which the sender can send multiple frames before needing an acknowledgment but must go back and retransmit all frames from the last unacknowledged frame if an error is detected.

#### Explanation:

- **Sender**: Sends frames continuously up to a window size and waits for an acknowledgment. If an acknowledgment is not received for a frame, all subsequent frames from that point are retransmitted.
- **Receiver**: Receives frames and sends an acknowledgment for the last correctly received frame. If an error is detected, it only acknowledges the last correctly received frame.

#### Implementation in C:

```c
#include <stdio.h>
#include <stdbool.h>

#define WINDOW_SIZE 4  // Size of the Go-Back-N window
#define TOTAL_FRAMES 10  // Total number of frames to be sent

// Function to simulate sending frames
void sendFrames(int start, int end) {
    printf("Sending frames: ");
    for (int i = start; i <= end && i < TOTAL_FRAMES; i++) {
        printf("%d ", i + 1);
    }
    printf("\n");
}

// Function to simulate acknowledgment
void receiveAcknowledgment(int ack) {
    printf("Received acknowledgment for frame: %d\n", ack + 1);
}

int main() {
    int nextFrameToSend = 0;
    int nextFrameToReceive = 0;
    bool ackReceived[TOTAL_FRAMES] = {false};

    // Simulate Go-Back-N protocol
    while (nextFrameToReceive < TOTAL_FRAMES) {
        // Send frames within the window
        sendFrames(nextFrameToSend, nextFrameToSend + WINDOW_SIZE - 1);

        // Simulate acknowledgment reception
        for (int i = nextFrameToReceive; i < nextFrameToReceive + WINDOW_SIZE && i < TOTAL_FRAMES; i++) {
            receiveAcknowledgment(i);
            ackReceived[i] = true;
        }

        // Check for missing acknowledgments
        while (ackReceived[nextFrameToReceive]) {
            nextFrameToReceive++;
            nextFrameToSend++;
        }

        // Slide the window
        nextFrameToSend = nextFrameToReceive;
    }

    return 0;
}
```

#### Sample Output:

```
Sending frames: 1 2 3 4
Received acknowledgment for frame: 1
Received acknowledgment for frame: 2
Received acknowledgment for frame: 3
Received acknowledgment for frame: 4
Sending frames: 5 6 7 8
Received acknowledgment for frame: 5
Received acknowledgment for frame: 6
Received acknowledgment for frame: 7
Received acknowledgment for frame: 8
Sending frames: 9 10
Received acknowledgment for frame: 9
Received acknowledgment for frame: 10
```

# 4. Implement Dijkstra’s Algorithm

### 4.1 Compute the Shortest Path through a Network: Implement Dijkstra's algorithm to compute the shortest path.

**Dijkstra’s Algorithm** is a famous algorithm used for finding the shortest paths from a source node to all other nodes in a weighted graph. The algorithm works with graphs where weights are non-negative.

#### Explanation:

1. **Initialization**: Start with a source node. Set the distance to the source node as 0 and all other nodes as infinity. Use a priority queue to keep track of the next node with the shortest tentative distance.
2. **Processing Nodes**: Extract the node with the smallest distance from the priority queue. Update the distances of its neighboring nodes.
3. **Repeat**: Continue until all nodes have been processed.

#### Implementation in C:

```c
#include <stdio.h>
#include <limits.h>

#define V 9  // Number of vertices in the graph

// Function to find the vertex with the minimum distance
int minDistance(int dist[], int sptSet[]) {
    int min = INT_MAX, min_index;
    for (int v = 0; v < V; v++) {
        if (sptSet[v] == 0 && dist[v] <= min) {
            min = dist[v];
            min_index = v;
        }
    }
    return min_index;
}

// Function to print the distance array
void printSolution(int dist[], int n) {
    printf("Vertex   Distance from Source\n");
    for (int i = 0; i < n; i++) {
        printf("%d \t\t %d\n", i, dist[i]);
    }
}

// Function to implement Dijkstra's algorithm
void dijkstra(int graph[V][V], int src) {
    int dist[V];
    int sptSet[V];  // Shortest Path Tree Set

    // Initialize distances and sptSet
    for (int i = 0; i < V; i++) {
        dist[i] = INT_MAX;
        sptSet[i] = 0;
    }
    dist[src] = 0;

    // Find shortest path for all vertices
    for (int count = 0; count < V - 1; count++) {
        int u = minDistance(dist, sptSet);
        sptSet[u] = 1;

        // Update distance value of the adjacent vertices of the picked vertex
        for (int v = 0; v < V; v++) {
            if (!sptSet[v] && graph[u][v] && dist[u] != INT_MAX && dist[u] + graph[u][v] < dist[v]) {
                dist[v] = dist[u] + graph[u][v];
            }
        }
    }

    // Print the constructed distance array
    printSolution(dist, V);
}

int main() {
    // Adjacency matrix representation of the graph
    int graph[V][V] = {
        {0, 4, 0, 0, 0, 0, 0, 8, 0},
        {4, 0, 8, 0, 0, 0, 0, 11, 0},
        {0, 8, 0, 7, 0, 4, 0, 0, 2},
        {0, 0, 7, 0, 9, 14, 0, 0, 0},
        {0, 0, 0, 9, 0, 10, 0, 0, 0},
        {0, 0, 4, 14, 10, 0, 2, 0, 0},
        {0, 0, 0, 0, 0, 2, 0, 1, 6},
        {8, 11, 0, 0, 0, 0, 1, 0, 7},
        {0, 0, 2, 0, 0, 0, 6, 7, 0}
    };

    dijkstra(graph, 0);  // Source node is 0

    return 0;
}
```

#### Sample Output:

```
Vertex   Distance from Source
0 	         0
1 	         4
2 	         12
3 	         19
4 	         21
5 	         11
6 	         9
7 	         8
8 	         14
```

# 5. Broadcast Tree

A **broadcast tree** is a data structure used to efficiently manage broadcast messages within a network. The concept is commonly used in network protocols and distributed systems to minimize the number of messages sent and to ensure that every node in a subnet receives the broadcast message.

### 5.1 Example Subnet of Hosts: Defining and working with a subnet of hosts.

A subnet is a logical subdivision of an IP network. To understand broadcast trees, let's define a simple subnet with several hosts and visualize how they are interconnected.

#### Example Subnet:

Consider a subnet with the following hosts:

- Host A (192.168.1.1)
- Host B (192.168.1.2)
- Host C (192.168.1.3)
- Host D (192.168.1.4)
- Host E (192.168.1.5)

The hosts are connected as follows:

```
   A
  / \
 B   C
 |   |
 D   E
```

### 5.2 Obtain a Broadcast Tree for the Subnet: Generation of a broadcast tree from a given subnet.

To generate a broadcast tree from the subnet, we need to create a tree structure where:

1. **The root** is the originating node of the broadcast.
2. **All nodes** are connected such that a broadcast message from the root can reach all nodes in the tree with minimal redundancy.

#### Steps to Obtain a Broadcast Tree:

1. **Identify the Root Node**: This is the node from which the broadcast originates. For simplicity, let's assume Host A is the root node.

2. **Create a Tree Structure**:
   - Each node in the subnet connects to its direct neighbors.
   - The broadcast tree will include the root node and all its reachable nodes.

#### Example Implementation:

Here’s a simple C program to represent a broadcast tree structure and display the connections.

```c
#include <stdio.h>
#include <stdlib.h>

#define MAX_NODES 5

typedef struct Node {
    int id;
    struct Node* neighbors[MAX_NODES];
    int neighborCount;
} Node;

void addNeighbor(Node* node, Node* neighbor) {
    if (node->neighborCount < MAX_NODES) {
        node->neighbors[node->neighborCount++] = neighbor;
    }
}

void printBroadcastTree(Node* node, int level) {
    if (node == NULL) return;

    for (int i = 0; i < level; i++) printf("  ");
    printf("Host %d\n", node->id);

    for (int i = 0; i < node->neighborCount; i++) {
        printBroadcastTree(node->neighbors[i], level + 1);
    }
}

int main() {
    // Create nodes
    Node* A = (Node*)malloc(sizeof(Node));
    Node* B = (Node*)malloc(sizeof(Node));
    Node* C = (Node*)malloc(sizeof(Node));
    Node* D = (Node*)malloc(sizeof(Node));
    Node* E = (Node*)malloc(sizeof(Node));

    // Initialize nodes
    A->id = 1; A->neighborCount = 0;
    B->id = 2; B->neighborCount = 0;
    C->id = 3; C->neighborCount = 0;
    D->id = 4; D->neighborCount = 0;
    E->id = 5; E->neighborCount = 0;

    // Define neighbors
    addNeighbor(A, B);
    addNeighbor(A, C);
    addNeighbor(B, D);
    addNeighbor(C, E);

    // Print the broadcast tree
    printf("Broadcast Tree:\n");
    printBroadcastTree(A, 0);

    // Free allocated memory
    free(A);
    free(B);
    free(C);
    free(D);
    free(E);

    return 0;
}
```

#### Explanation:

- **Nodes**: Each `Node` represents a host.
- **Neighbors**: Each node has a list of its direct neighbors.
- **Tree Construction**: Neighbors are added to create the tree structure.
- **Printing**: The `printBroadcastTree` function recursively prints the tree structure with indentation to visualize the hierarchy.

#### Sample Output:

```
Broadcast Tree:
Host 1
  Host 2
    Host 4
  Host 3
    Host 5
```

# 6. Implement Distance Vector Routing Algorithm

### 6.1 Obtain Routing Tables at Each Node: Implementation of the Distance Vector Routing Algorithm and retrieval of routing tables.

**Distance Vector Routing Algorithm** is a routing protocol used to find the shortest path in a network. Each node maintains a table (vector) containing the shortest distance to every other node in the network.

#### Explanation:

1. **Initialization**: Each node initializes its distance vector with direct distances to neighboring nodes.
2. **Update**: Nodes periodically send their distance vector to their neighbors. On receiving distance vectors from neighbors, nodes update their tables if a shorter path is found.
3. **Convergence**: The algorithm converges when no further updates are needed.

#### Implementation in C:

```c
#include <stdio.h>
#include <limits.h>

#define N 4  // Number of nodes

// Function to print the distance vector
void printRoutingTable(int dist[N][N]) {
    printf("Routing Table:\n");
    for (int i = 0; i < N; i++) {
        printf("From node %d: ", i);
        for (int j = 0; j < N; j++) {
            if (dist[i][j] == INT_MAX) {
                printf("INF ");
            } else {
                printf("%d ", dist[i][j]);
            }
        }
        printf("\n");
    }
}

// Function to implement the Distance Vector Routing Algorithm
void distanceVectorRouting(int graph[N][N]) {
    int dist[N][N];

    // Initialize distance vector with graph weights
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            dist[i][j] = graph[i][j];
        }
    }

    // Perform the Distance Vector Algorithm
    for (int k = 0; k < N; k++) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (dist[i][j] > dist[i][k] + dist[k][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }

    // Print the routing tables
    printRoutingTable(dist);
}

int main() {
    // Adjacency matrix representation of the graph
    int graph[N][N] = {
        {0, 1, 4, INT_MAX},
        {1, 0, 2, 6},
        {4, 2, 0, 3},
        {INT_MAX, 6, 3, 0}
    };

    distanceVectorRouting(graph);

    return 0;
}
```

#### Sample Output:

```
Routing Table:
From node 0: 0 1 3 6
From node 1: 1 0 2 5
From node 2: 3 2 0 3
From node 3: 6 5 3 0
```

# 7. Implement Data Encryption and Decryption Techniques

- Explanation and implementation of basic data encryption and decryption techniques.

# 8. Congestion Control

### 8.1 Write a Program using the Leaky Bucket Algorithm

- Implementation of the leaky bucket algorithm for congestion control.
```
#include<stdio.h> 
#include<conio.h>
#define MAX 25 
#define min(x,y) ((x)<(y)? (x):(y)) 
int main() 
{ 
 int cap, oprt,nsec,cont,i=0,inp[MAX],ch; 
 clrscr(); 
 printf("Enter the bucket size:\n"); 
 scanf("%d",&cap); 
 printf("Enter the accepted rate:\n"); 
 scanf("%d",&oprt); 
 do 
 { 
 printf("Enter the number of packets entering at %d seconds: ",i+1); 
 scanf("%d",&inp[i]); 
 i++; 
 printf("Enter 1 to insert packets or 0 to quit\n"); 
 scanf("%d",&ch); 
 }while(ch); 
 
 nsec=i; 
 printf("\n seconds \t packets received \t packets sent \t packets left in bucket\n"); 
 cont=0; 
 
 for(i = 0; i < nsec; i++) 
 { 
 cont += inp[i]; 
 if(cont > cap) 
 cont = cap; 
 printf(" %d ",(i+1)); 
 printf("\t\t %d ",inp[i]); 
 printf("\t\t\t\t %d ",min(cont,oprt)); 
 cont=cont - min(cont,oprt); 
 printf("\t\t %d \n",cont); 
 } 
for( i=0; cont != 0; i++) 
 { 
 if(cont > cap) 
 cont = cap; 
 printf(" %d ",(i+1)); 
 printf("\t\t 0 "); 
 printf("\t\t\t\t %d ",min(cont,oprt)); 
 cont=cont - min(cont,oprt); 
 printf("\t\t %d \n",cont); 
 } 
 getch();
 return(0); 
}

```
```
PS D:\Github\program-examples\resources\CN> .\a.exe
Enter the bucket size:
50
Enter the accepted rate:
12
Enter the number of packets entering at 1 seconds: 40
Enter 1 to insert packets or 0 to quit
1
Enter the number of packets entering at 2 seconds: 20
Enter 1 to insert packets or 0 to quit
0

 seconds         packets received        packets sent    packets left in bucket
 1               40                              12              28
 2               20                              12              36
 1               0                               12              24
 2               0                               12              12
 3               0                               12              0
```
# 9. Frame Sorting Techniques

### 9.1 Program for Frame Sorting Used in Buffers

- Frame sorting technique implementation in data buffers.

```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

struct frame {
    int sno;
    char msg[15];
    int flag;
};

int main() {
    int i, j, n, r, k;
    clrscr();
    printf("Enter the number of frames: ");
    scanf("%d", &n);

    struct frame fr[n];
    int s[n];
    for (i = 0; i < n; i++) {
        s[i] = -1;
        fr[i].sno = -1;
    }

    printf("Enter the messages:\n");
    for (i = 0; i < n; i++) {
        scanf("%s", fr[i].msg);
        fr[i].sno = i;
    }

    srand(time(NULL)); // Seed for randomness
    for (j = 0; j < n; j++) {
        r = rand() % n;
        if (s[r] == -1) {
            fr[j].flag = r;
            s[r] = 1;
        } else {
            for (k = 0; k < n; k++) {
                if (s[k] == -1) {
                    fr[j].flag = k;
                    s[k] = 1;
                    break;
                }
            }
        }
    }

    printf("\nArrived frames are:\n");
    printf(" sno\tmsg\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            if (fr[j].flag == i) {
                printf(" %d\t%s\n", fr[j].sno, fr[j].msg);
            }
        }
    }

    // Sort frames by sno
    for (i = 0; i < n; i++) {
        for (j = 0; j < n - 1; j++) {
            if (fr[j].sno > fr[j + 1].sno) {
                struct frame temp = fr[j];
                fr[j] = fr[j + 1];
                fr[j + 1] = temp;
            }
        }
    }

    printf("\nAfter sorting arrived frames are:\n");
    printf(" sno\tmsg\n");
    for (i = 0; i < n; i++) {
        printf(" %d\t%s\n", fr[i].sno, fr[i].msg);
    }
    getch();
    return 0;
}

```

```
PS D:\Github\program-examples\resources\CN> .\a.exe
Enter the number of frames: 5
Enter the messages:
welcome
to 
the
class
room

Arrived frames are:
 sno    msg
 3      class
 4      room
 2      the
 0      welcome
 1      to

After sorting arrived frames are:
 sno    msg
 0      welcome
 1      to
 2      the
 3      class
 4      room
```
# 10. Wireshark

### **10.1 Packet Capture using Wireshark**

#### **Aim**:  
To capture live network packets using Wireshark for analyzing network activity.

#### **Notes**:  
1. Open Wireshark.  
2. Select the network interface to monitor (e.g., Ethernet, Wi-Fi).  
3. Click the **Start Capturing Packets** button (the blue shark fin icon).  
4. Wireshark will start capturing all packets on the selected interface in real time.  
5. Stop the capture by clicking the **Stop Capturing Packets** button (red square icon).

- **Captured Data**: Each row represents a captured packet.
- **Columns**: No., Time, Source, Destination, Protocol, Length, Info.

#### **Output**:  
A list of captured packets displayed in a table format with details like source, destination, protocol, and additional information.

---

### **10.2 Starting Wireshark**

#### **Aim**:  
To set up and configure Wireshark for network monitoring.

#### **Notes**:  
1. Launch Wireshark from your system’s application menu or terminal.  
2. Select an appropriate **network interface** (Wi-Fi, Ethernet, etc.) for monitoring.  
3. Configure optional settings:  
   - **Capture filters** to limit the type of packets captured.  
   - **File format** and location for saving captures.  
4. Start the packet capture by selecting the interface and clicking **Start**.

#### **Output**:  
Wireshark starts capturing packets from the specified network interface.

---

### **10.3 Viewing Captured Traffic**

#### **Aim**:  
To inspect and analyze the details of captured packets.

#### **Notes**:  
1. Captured packets are displayed in three panes:
   - **Packet List**: Displays summary of all packets captured.  
   - **Packet Details**: Shows hierarchical details of a selected packet (e.g., Ethernet, IP, TCP layers).  
   - **Packet Bytes**: Displays raw data in hexadecimal format for a selected packet.
2. Use **time stamps** and **protocol** for filtering and identifying specific traffic.  
3. Double-click on a packet to expand its details.

#### **Output**:  
Detailed information about individual packets, including headers and payload.

---

### **10.4 Analysis, Statistics & Filters**

#### **Aim**:  
To analyze network traffic, generate statistics, and apply filters in Wireshark.

#### **Notes**:  
1. **Analysis Tools**:  
   - Use **Follow TCP Stream** to see communication between source and destination.  
   - Examine packet latency, retransmissions, and throughput.
2. **Statistics**:  
   - Access via the **Statistics** menu.  
   - Includes **IO Graphs**, **Protocol Hierarchy**, and **Conversation Analysis**.
3. **Filters**:  
   - **Display Filters**: Refine displayed packets (e.g., `ip.src == 192.168.1.1` or `http`).  
   - **Capture Filters**: Set before capture to limit the data captured.

#### **Output**:  
- Clear insights into network behavior.  
- Filtered view of specific traffic or communication.  
- Graphical representation of traffic patterns.

---

# 11. Nmap
### **11.1 How to Run Nmap Scan**

#### **Aim**:  
To perform a network scan using Nmap for network discovery and security auditing.

#### **Notes**:  
1. **Install Nmap**:  
   - On Linux: `sudo apt install nmap`  
   - On Windows: Download and install from the official [Nmap site](https://nmap.org/).  
2. **Basic Commands**:  
   - Scan a single host: `nmap <IP>`  
   - Scan a range of IPs: `nmap <IP range>`  
   - Scan all devices on a subnet: `nmap 192.168.1.0/24`  
3. **Scan Options**:  
   - **-sP**: Ping scan to check online hosts.  
   - **-sS**: SYN scan (stealth scan).  
   - **-p <port>**: Scan specific ports (e.g., `nmap -p 22 <IP>`).  
   - **-A**: Comprehensive scan for OS detection, version detection, script scanning, and traceroute.

#### **Output**:  
- A list of active hosts and open ports.  
- Details include IP address, hostnames, and status of scanned ports.  
- Example Output:
  ```
  Nmap scan report for 192.168.1.1
  Host is up (0.0010s latency).
  PORT   STATE SERVICE
  22/tcp open  ssh
  80/tcp open  http
  ```

---

### **11.2 Operating System Detection using Nmap**

#### **Aim**:  
To detect the operating systems of devices on a network using Nmap.

#### **Notes**:  
1. Run Nmap with the `-O` flag:  
   - `nmap -O <IP>`: Detects the OS of a single host.  
   - `nmap -O 192.168.1.0/24`: Scans all devices on the subnet for OS detection.  
2. **Additional Flags**:  
   - **-v**: Increases verbosity for detailed output.  
   - **--osscan-guess**: Attempts to guess the OS if exact match is unavailable.  
3. The OS detection works by analyzing packet responses to Nmap probes. Accuracy depends on open ports and network conditions.

#### **Output**:  
- Detected OS information, including name and version (if available).  
- Example Output:
  ```
  Nmap scan report for 192.168.1.2
  Host is up (0.0020s latency).
  PORT   STATE SERVICE
  22/tcp open  ssh
  OS: Linux 4.x (98%)
  ```

--- 

# 12. NS2 Simulator

### **12.1 Introduction to NS2 Simulator**

#### **Aim**:  
To understand the basics of NS2 (Network Simulator 2) and its application in simulating network protocols, topologies, and performance analysis.

#### **Notes**:  
1. **What is NS2?**  
   - NS2 is a discrete event simulator widely used for networking research.  
   - It supports simulation of wired and wireless network protocols (e.g., TCP, UDP, routing algorithms).  
   - Written in C++ and uses OTcl (Object Tool Command Language) for simulation scripts.

2. **Key Features**:  
   - Simulation of real-world network behavior.  
   - Support for various network protocols and applications.  
   - Extensible architecture to add new protocols and modules.  
   - Visualization using the Network Animator (NAM).

3. **Components**:  
   - **C++ Modules**: Handle data processing, packet transmission, and routing logic.  
   - **OTcl Scripts**: Define network topologies, traffic patterns, and simulation parameters.  

4. **Applications**:  
   - Testing new network protocols.  
   - Studying network congestion, routing, and performance metrics.  
   - Evaluating wireless networks, including MANETs and sensor networks.

5. **How It Works**:  
   - Define network parameters in an OTcl script.  
   - NS2 executes the script to simulate network behavior.  
   - Results are stored in trace files for analysis.  

#### **Output**:  
- **Simulation Trace File**: Contains packet-level details of the simulation (e.g., source, destination, event type).  
- **Network Animator (NAM)**: Provides a graphical visualization of network behavior during the simulation.

--- 
### **12.2 Simulate to Find the Number of Packets Dropped**  

**Objective**:  
To compute the total number of packets dropped in a network during a simulation using NS2.  

**Introduction**:  
Packet drop in a network occurs when the network fails to deliver data packets to the intended recipient. This could be due to factors such as congestion, buffer overflow, or link failure. In NS2, this metric is vital to evaluate network performance.  

**Steps to Simulate**:  
1. **Create Network Topology**:  
   Define a basic network with nodes, links, and agents. Use the TCL script to set up nodes and define links with bandwidth and delay.  
   
2. **Define Traffic Source**:  
   Attach a traffic generator like Constant Bit Rate (CBR) or FTP to simulate traffic between nodes.  

3. **Add Sink Node**:  
   Attach a receiving agent (e.g., TCP Sink or Null Agent) to the destination node.  

4. **Enable Trace**:  
   Add tracing functionality to capture events (e.g., packet drops). Use the `trace-all` command to record network activities.  

5. **Run Simulation**:  
   Execute the TCL script to start the simulation. Use the `.tr` file generated to analyze results.  

6. **Analyze Results**:  
   Use AWK scripts or other parsing tools to filter the trace file. Search for "d" events (indicating a packet drop).  

**Sample TCL Script**:  
```tcl
# Define the network simulator
set ns [new Simulator]

# Define nodes
set n0 [$ns node]
set n1 [$ns node]

# Define a link
$ns duplex-link $n0 $n1 10Mb 10ms DropTail

# Attach agents
set udp [new Agent/UDP]
$ns attach-agent $n0 $udp
set null [new Agent/Null]
$ns attach-agent $n1 $null
$ns connect $udp $null

# Define CBR traffic
set cbr [new Application/Traffic/CBR]
$cbr attach-agent $udp
$cbr set rate_ 1Mb

# Enable tracing
set tracefile [open out.tr w]
$ns trace-all $tracefile

# Run simulation
$ns at 0.1 "$cbr start"
$ns at 5.0 "finish"
proc finish {} {
    global ns tracefile
    $ns flush-trace
    close $tracefile
    exit 0
}

$ns run
```

**Result Analysis**:  
Use an AWK script to extract packet drops:  
```awk
BEGIN { drops = 0 } 
$1 == "d" { drops++ } 
END { print "Total Packet Drops: ", drops }
```  

**Output**:  
Displays the total number of dropped packets.

---

### **12.3 Simulate to Find the Number of Packets Dropped by TCP/UDP**  

**Objective**:  
To compute the number of packets dropped separately for TCP and UDP in a network using NS2.  

**Introduction**:  
TCP and UDP are two common transport protocols. TCP ensures reliable delivery, while UDP is connectionless. Packet drops in these protocols indicate reliability issues in TCP or network limitations for UDP.  

**Steps to Simulate**:  
1. **Create Topology**:  
   Define a network with nodes and links.  

2. **Add TCP and UDP Agents**:  
   Attach TCP and UDP agents to source nodes and their respective sinks (e.g., TCP Sink for TCP and Null Agent for UDP).  

3. **Enable Traffic Sources**:  
   Define FTP for TCP and CBR for UDP to generate traffic.  

4. **Enable Tracing**:  
   Use the `trace-all` command and record events in the trace file.  

5. **Run Simulation**:  
   Execute the script and generate the trace file.  

6. **Analyze Results**:  
   Use AWK to count packet drops for TCP and UDP by filtering trace lines based on source protocols.  

**Sample TCL Script**:  
```tcl
# Define simulator
set ns [new Simulator]

# Define nodes
set n0 [$ns node]
set n1 [$ns node]

# Add links
$ns duplex-link $n0 $n1 5Mb 10ms DropTail

# TCP configuration
set tcp [new Agent/TCP]
$ns attach-agent $n0 $tcp
set tcpsink [new Agent/TCPSink]
$ns attach-agent $n1 $tcpsink
$ns connect $tcp $tcpsink
set ftp [new Application/FTP]
$ftp attach-agent $tcp
$ftp set type_ FTP

# UDP configuration
set udp [new Agent/UDP]
$ns attach-agent $n0 $udp
set null [new Agent/Null]
$ns attach-agent $n1 $null
$ns connect $udp $null
set cbr [new Application/Traffic/CBR]
$cbr attach-agent $udp
$cbr set rate_ 1Mb

# Enable tracing
set tracefile [open out.tr w]
$ns trace-all $tracefile

# Schedule events
$ns at 0.1 "$ftp start"
$ns at 1.0 "$cbr start"
$ns at 5.0 "finish"

proc finish {} {
    global ns tracefile
    $ns flush-trace
    close $tracefile
    exit 0
}

$ns run
```

**Result Analysis**:  
Filter TCP and UDP packet drops separately using AWK:  
```awk
BEGIN { tcp_drops = 0; udp_drops = 0 } 
$1 == "d" && $8 == "tcp" { tcp_drops++ } 
$1 == "d" && $8 == "udp" { udp_drops++ } 
END { print "TCP Drops: ", tcp_drops; print "UDP Drops: ", udp_drops }
```  

**Output**:  
Displays the number of TCP and UDP packet drops.

---

### **12.4 Simulate to Find the Number of Packets Dropped Due to Congestion**  

**Objective**:  
To compute packet drops caused by congestion in a network using NS2.  

**Introduction**:  
Congestion occurs when the network capacity is insufficient to handle incoming traffic. This results in packet drops, primarily at queue buffers.  

**Steps to Simulate**:  
1. **Create Topology**:  
   Set up a network with multiple traffic sources and a shared link to create congestion.  

2. **Configure Queues**:  
   Use DropTail or RED (Random Early Detection) queues to simulate congestion.  

3. **Enable Tracing**:  
   Record events in the trace file to identify drops at congested links.  

4. **Analyze Results**:  
   Parse trace files to count drops at specific links.  

**Sample TCL Script**:  
```tcl
# Define simulator
set ns [new Simulator]

# Define nodes
set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]

# Define links
$ns duplex-link $n0 $n1 1Mb 10ms DropTail
$ns duplex-link $n1 $n2 512Kb 20ms DropTail

# Traffic sources
set udp [new Agent/UDP]
$ns attach-agent $n0 $udp
set null [new Agent/Null]
$ns attach-agent $n2 $null
$ns connect $udp $null
set cbr [new Application/Traffic/CBR]
$cbr attach-agent $udp
$cbr set rate_ 1Mb

# Enable tracing
set tracefile [open congestion.tr w]
$ns trace-all $tracefile

# Schedule events
$ns at 0.1 "$cbr start"
$ns at 5.0 "finish"

proc finish {} {
    global ns tracefile
    $ns flush-trace
    close $tracefile
    exit 0
}

$ns run
```

**Result Analysis**:  
Filter packet drops due to congestion (occurring at the bottleneck link):  
```awk
BEGIN { drops = 0 } 
$1 == "d" && $3 == "link" { drops++ } 
END { print "Congestion Drops: ", drops }
```  

**Output**:  
Displays the number of packets dropped due to congestion.  

### **12.5 Simulate to Compare Data Rate & Throughput**  

**Objective**:  
To simulate a network using NS2 and compare the data rate and throughput of the network under different scenarios.  

**Introduction**:  
- **Data Rate**: Refers to the rate at which data is sent across the network, typically measured in bits per second (bps). It is determined by the traffic generator (e.g., CBR, FTP).  
- **Throughput**: Refers to the amount of successful data delivery over the network, measured in bits per second or packets per second.  

**Steps to Simulate**:  
1. **Set Up Network Topology**:  
   Define nodes and links, specifying bandwidth and propagation delay.  
   
2. **Attach Traffic Generators**:  
   - Use CBR for a constant data rate.  
   - Use FTP (over TCP) to study throughput.  

3. **Enable Tracing**:  
   Trace packet flow using the `trace-all` command to collect statistics on data sent and received.  

4. **Run Simulation**:  
   Execute the script and generate a trace file.  

5. **Analyze Results**:  
   - Use AWK or Python scripts to extract throughput and compare it with the data rate.  
   - Plot results using tools like GNUPLOT or MATLAB.  

**Sample TCL Script**:  
```tcl
# Define simulator
set ns [new Simulator]

# Define nodes
set n0 [$ns node]
set n1 [$ns node]

# Create a link
$ns duplex-link $n0 $n1 2Mb 10ms DropTail

# Traffic Source 1 (CBR)
set udp [new Agent/UDP]
$ns attach-agent $n0 $udp
set null [new Agent/Null]
$ns attach-agent $n1 $null
$ns connect $udp $null
set cbr [new Application/Traffic/CBR]
$cbr attach-agent $udp
$cbr set rate_ 1Mb

# Traffic Source 2 (FTP)
set tcp [new Agent/TCP]
$ns attach-agent $n0 $tcp
set tcpsink [new Agent/TCPSink]
$ns attach-agent $n1 $tcpsink
$ns connect $tcp $tcpsink
set ftp [new Application/FTP]
$ftp attach-agent $tcp

# Enable tracing
set tracefile [open rate_throughput.tr w]
$ns trace-all $tracefile

# Schedule events
$ns at 0.1 "$cbr start"
$ns at 1.0 "$ftp start"
$ns at 5.0 "finish"

proc finish {} {
    global ns tracefile
    $ns flush-trace
    close $tracefile
    exit 0
}

$ns run
```

**Result Analysis**:  
Use AWK to calculate throughput:  
```awk
BEGIN { sent = 0; received = 0 }
$1 == "+" { sent += $11 }  
$1 == "r" { received += $11 }  
END { 
    print "Data Rate: ", sent / 5, "bps";
    print "Throughput: ", received / 5, "bps";
}
```  

**Output**:  
Displays and compares data rate and throughput.

---

### **12.6 Simulate to Plot Congestion for Different Source/Destination**  

**Objective**:  
To plot congestion metrics for different source and destination pairs in a network.  

**Introduction**:  
Congestion in a network occurs when multiple traffic flows compete for limited resources (e.g., bandwidth). By simulating different source/destination pairs, congestion trends can be observed and visualized.  

**Steps to Simulate**:  
1. **Set Up Topology**:  
   Define nodes and links, ensuring a bottleneck link to simulate congestion.  

2. **Add Multiple Traffic Sources**:  
   Attach traffic sources to simulate different source/destination pairs.  

3. **Enable Tracing**:  
   Use the `trace-all` command to record packet events (sent, received, dropped) for analysis.  

4. **Analyze Congestion**:  
   Parse trace files to extract drop events for each source/destination pair.  

5. **Plot Results**:  
   Use GNUPLOT, Python (matplotlib), or Excel to visualize congestion levels.  

**Sample TCL Script**:  
```tcl
# Define simulator
set ns [new Simulator]

# Define nodes
set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]

# Create links
$ns duplex-link $n0 $n1 1Mb 10ms DropTail
$ns duplex-link $n2 $n1 1Mb 10ms DropTail
$ns duplex-link $n1 $n3 512Kb 20ms DropTail

# Traffic Source 1
set udp1 [new Agent/UDP]
$ns attach-agent $n0 $udp1
set null1 [new Agent/Null]
$ns attach-agent $n3 $null1
$ns connect $udp1 $null1
set cbr1 [new Application/Traffic/CBR]
$cbr1 attach-agent $udp1
$cbr1 set rate_ 500Kb

# Traffic Source 2
set udp2 [new Agent/UDP]
$ns attach-agent $n2 $udp2
set null2 [new Agent/Null]
$ns attach-agent $n3 $null2
$ns connect $udp2 $null2
set cbr2 [new Application/Traffic/CBR]
$cbr2 attach-agent $udp2
$cbr2 set rate_ 500Kb

# Enable tracing
set tracefile [open congestion_plot.tr w]
$ns trace-all $tracefile

# Schedule events
$ns at 0.1 "$cbr1 start"
$ns at 0.2 "$cbr2 start"
$ns at 5.0 "finish"

proc finish {} {
    global ns tracefile
    $ns flush-trace
    close $tracefile
    exit 0
}

$ns run
```

**Result Analysis**:  
Extract congestion metrics for each pair:  
```awk
BEGIN { drops1 = 0; drops2 = 0 } 
$1 == "d" && $3 == "link" && $2 == "n0->n3" { drops1++ }
$1 == "d" && $3 == "link" && $2 == "n2->n3" { drops2++ }
END { 
    print "Congestion for n0->n3: ", drops1;
    print "Congestion for n2->n3: ", drops2;
}
```  

**Plot Congestion**:  
- Use GNUPLOT to create a bar chart comparing congestion levels.

---

### **12.7 Simulate to Determine the Performance with Respect to Transmission of Packets**  

**Objective**:  
To evaluate network performance based on packet transmission metrics, such as throughput, latency, and packet loss.  

**Introduction**:  
Packet transmission performance is a key indicator of network reliability. It is influenced by bandwidth, congestion, and protocol behavior.  

**Steps to Simulate**:  
1. **Create Network Topology**:  
   Define a topology with nodes and links.  

2. **Add Traffic Generators**:  
   Attach agents (e.g., UDP, TCP) and define traffic flows.  

3. **Enable Metrics Collection**:  
   Trace sent, received, and dropped packets.  

4. **Analyze Performance**:  
   Compute metrics such as throughput, packet loss ratio, and average delay.  

**Sample TCL Script**:  
```tcl
# Define simulator
set ns [new Simulator]

# Define nodes
set n0 [$ns node]
set n1 [$ns node]

# Create link
$ns duplex-link $n0 $n1 2Mb 10ms DropTail

# Traffic Source
set tcp [new Agent/TCP]
$ns attach-agent $n0 $tcp
set tcpsink [new Agent/TCPSink]
$ns attach-agent $n1 $tcpsink
$ns connect $tcp $tcpsink

# Enable tracing
set tracefile [open performance.tr w]
$ns trace-all $tracefile

# Schedule events
$ns at 0.1 "$tcp send"
$ns at 5.0 "finish"

proc finish {} {
    global ns tracefile
    $ns flush-trace
    close $tracefile
    exit 0
}

$ns run
```

**Result Analysis**:  
Calculate performance metrics:  
- **Throughput**:  
  ```awk
  BEGIN { received = 0 } 
  $1 == "r" { received += $11 }
  END { print "Throughput: ", received / 5, "bps" }
  ```  
- **Packet Loss**:  
  ```awk
  BEGIN { sent = 0; received = 0 } 
  $1 == "+" { sent++ } 
  $1 == "r" { received++ } 
  END { print "Packet Loss Ratio: ", (sent - received) / sent }
  ```  

**Output**:  
Displays network performance metrics for packet transmission.

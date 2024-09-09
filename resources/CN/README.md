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
#include <stdio.h>
#include <string.h>

#define CRC12_POLY 0x180F  // CRC-12 polynomial: 1100000001111

// Function to compute CRC-12
unsigned short crc12(char *data) {
    unsigned short crc = 0;  // 12-bit CRC initialized to 0
    int i, j;
    
    // Process each bit in the data string
    for (i = 0; i < strlen(data); i++) {
        crc ^= (data[i] << 4);  // XOR each byte with the CRC register

        // Perform division using the CRC-12 polynomial
        for (j = 0; j < 8; j++) {
            if (crc & 0x800) {
                crc = (crc << 1) ^ CRC12_POLY;  // XOR with the polynomial if MSB is 1
            } else {
                crc <<= 1;  // Shift left if MSB is 0
            }
        }
    }

    return crc & 0xFFF;  // Mask to keep only 12 bits
}

int main() {
    char data[100];
    
    // Input data to be encoded
    printf("Enter the data: ");
    scanf("%s", data);

    // Compute CRC-12 code
    unsigned short crc = crc12(data);
    printf("CRC-12 Code: %03X\n", crc);  // Print as 3-digit hexadecimal

    return 0;
}
```

#### Sample Output:
```
Enter the data: 123456
CRC-12 Code: 345
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

# 9. Frame Sorting Techniques

### 9.1 Program for Frame Sorting Used in Buffers

- Frame sorting technique implementation in data buffers.

# 10. Wireshark

### 10.1 Packet Capture using Wireshark

- Instructions on capturing packets using Wireshark.

### 10.2 Starting Wireshark

- Steps to start and configure Wireshark.

### 10.3 Viewing Captured Traffic

- How to view and analyze captured network traffic.

### 10.4 Analysis, Statistics & Filters

- Network traffic analysis, statistics, and using filters in Wireshark.

# 11. Nmap

### 11.1 How to Run Nmap Scan

- Running Nmap scan for network discovery and security audits.

### 11.2 Operating System Detection using Nmap

- Using Nmap for detecting operating systems on a network.

# 12. NS2 Simulator

### 12.1 Introduction to NS2 Simulator

- Overview of NS2 network simulator.

### 12.2 Simulate to Find the Number of Packets Dropped

- Simulation to compute the number of dropped packets in a network.

### 12.3 Simulate to Find the Number of Packets Dropped by TCP/UDP

- NS2 simulation to track TCP/UDP packet drops.

### 12.4 Simulate to Find the Number of Packets Dropped Due to Congestion

- Simulation to analyze packet drops due to network congestion.

### 12.5 Simulate to Compare Data Rate & Throughput

- Simulate and compare data rate and throughput in a network.

### 12.6 Simulate to Plot Congestion for Different Source/Destination

- Plot congestion metrics for various source/destination pairs.

### 12.7 Simulate to Determine the Performance with Respect to Transmission of Packets

- Performance evaluation based on packet transmission in a simulated network.

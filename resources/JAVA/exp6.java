class TicketBookingSystem {
    private int availableTickets = 10; // Total tickets available

    // Method to book tickets, synchronized to handle concurrency
    public synchronized void bookTickets(String passengerName, int ticketsToBook) {
        if (ticketsToBook > availableTickets) {
            System.out.println("Sorry, " + passengerName + ". Not enough tickets available.");
            return;
        }

        // Simulating some delay to mimic real-world booking process
        try {
            Thread.sleep(100); // Introducing a small delay
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        // Booking tickets
        System.out.println(ticketsToBook + " ticket(s) booked for " + passengerName);
        availableTickets -= ticketsToBook;
        System.out.println("Remaining tickets: " + availableTickets);
    }
}

class TicketBookingExample {
    public static void main(String[] args) {
        TicketBookingSystem ticketSystem = new TicketBookingSystem();

        // Creating multiple threads to book tickets
        Thread thread1 = new Thread(() -> ticketSystem.bookTickets("Alice", 3));
        Thread thread2 = new Thread(() -> ticketSystem.bookTickets("Bob", 5));
        Thread thread3 = new Thread(() -> ticketSystem.bookTickets("Harsh", 4));
        Thread thread4 = new Thread(() -> ticketSystem.bookTickets("Carol", 2));

        // Start all threads
        thread1.start();
        thread2.start();
        thread3.start();
        thread4.start();

        // Wait for all threads to complete
        try {
            thread1.join();
            thread2.join();
            thread3.join();
            thread4.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
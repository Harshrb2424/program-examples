class MovieTicket {
    private int ticketCount = 10; // Total number of tickets available

    public synchronized void bookTicket() {
        if (ticketCount > 0) {
            System.out.println("Booking ticket...");
            ticketCount--;
            System.out.println("Ticket booked successfully. Remaining tickets: " + ticketCount);
        } else {
            System.out.println("No tickets available.");
        }
    }
}

public class TicketBookingSystem {
    public static void main(String[] args) {
        MovieTicket movieTicket = new MovieTicket();
        Thread thread1 = new Thread(() -> movieTicket.bookTicket());
        Thread thread2 = new Thread(() -> movieTicket.bookTicket());

        thread1.start();
        thread2.start();
    }
}

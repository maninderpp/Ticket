# Ticket
https://github.com/maninderpp/Ticket/edit/main/README.md

Help-desk Ticket System
This program is a simple Help-desk Ticket System that allows users to create, view, respond to, and manage tickets. It is written in Python and uses a class called TicketData to manage ticket data.

How to Use
To use the program, simply run the main() function in the program. This will display a menu with options to create, view, respond to, and manage tickets.

Creating a Ticket
To create a ticket, select option 1 from the main menu and enter the requested information, including the staff ID, creator's name, email address, and problem description. The program will then generate a ticket number and add the ticket to the system.

Reopening a Ticket
If a ticket has been closed and needs to be reopened, select option 2 from the main menu and enter the ticket number. The program will then search for the ticket with the given number and, if found, reopen the ticket.

Responding to a Ticket
To respond to a ticket, select option 3 from the main menu and enter the ticket number. The program will then search for the ticket with the given number and, if found, prompt the user to enter a response. The ticket will then be marked as closed and removed from the list of open tickets.

Displaying Tickets
To display a list of all tickets, select option 4 from the main menu. To display details for a specific ticket, select option 5 and enter the ticket number.

Displaying Ticket Statistics
To display ticket statistics, select option 6 from the main menu.

Exiting the Program
To exit the program, select option 7 from the main menu.

Class TicketData
The TicketData class is used to manage ticket data. It has several class-level attributes to track the total number of tickets, open tickets, and all tickets. The class also has several methods, including a constructor to initialize ticket data, a static method to show ticket statistics, and several getter and setter methods to access and modify ticket data.


class TicketData:
    # Default values for response and status
    default_response = "Not Yet Provided"
    default_status = "Open"

    # Starting number for ticket_number
    starting_number = 2000

    # Counters to track the total number of tickets, open tickets and all tickets
    total_ticket = 0
    open_tickets = 0

    # Counters to track the total number of tickets, open tickets and all tickets
    tickets = []
    
    # Constructor to initialize the ticket data
    def __init__(self, staff_id, creator_name, email, description):
        
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.email = email
        self.description = description

        # Set default values for response and status
        self.response_to_ticket = TicketData.default_response
        self.status = TicketData.default_status        

        # Set the ticket_number by incrementing total_ticket by 1
        self.ticket_number = TicketData.total_ticket + TicketData.starting_number
        
        # Set the ticket_number by incrementing total_ticket by 1
        TicketData.open_tickets += 1
        TicketData.total_ticket += 1
        TicketData.tickets.append(self)

    # Static method to show ticket statistics
    @staticmethod
    def show_ticket_statistics():
        print("\nTotal Tickets Created: ", TicketData.total_ticket) 
        print("Total Tickets Resolved: ", TicketData.total_ticket - TicketData.open_tickets)
        print("Total Tickets To Solve: ", TicketData.open_tickets)

#Function to create a new ticket
def create_ticket():
    staff_id = input("Enter the Staff_ID: ")
    creator_name = input("Enter the Creator's Name: ")
    email = input("Enter Email address: ")
    description = input("Enter the Problem Description: ")

    # Create a new TicketData object and print the ticket number
    ticket = TicketData(staff_id, creator_name, email, description)
    print("Ticket Created Successfully with Ticket Number ", ticket.ticket_number)

#Function to reopen a closed ticket
def reopen_ticket():
    ticket_number = int(input("\nEnter the Ticket Number: "))
    # Loop through all the tickets and find the ticket with the given ticket number and status "Closed"
    for ticket in TicketData.tickets:
        if ticket.ticket_number == ticket_number and ticket.status == "Closed":
            # Set the status to "Reopen", update the counters and print a success message
            ticket.status ="Reopen"
            TicketData.open_tickets += 1
            print("Successfully Reopened!!")
            break

#Function to respond to a ticket
def respond_to_ticket():
    ticket_number = int(input("\nEnter the Ticket Number: "))
    # Loop through all the tickets and find the ticket with the given ticket number
    for ticket in TicketData.tickets:
        if ticket.ticket_number == ticket_number:
            if ticket.description.lower() == "password change":
                # If the ticket description is "password change", set the response and status accordingly
                ticket.response_to_ticket = "New Password : "+ ticket.staff_id[:2]+ticket.creator_name[:3]
                ticket.status = "Closed"
                TicketData.open_tickets -= 1
                print("The ticket is resolved automatically because of new password request")
            else:
                # If the ticket description is not "password change", get the response from the user and set the status accordingly
                response = input("Enter the Response: ")
                ticket.response_to_ticket = response
                ticket.status = "Closed"
                TicketData.open_tickets -= 1
                print("The ticket has been successfully updated with a response")
            break

#Function to display all the tickets
def display_all_tickets():
    for ticket in TicketData.tickets:
        print("\nTicket Number: ", ticket.ticket_number)
        print("Ticket Creator: ", ticket.creator_name)
        print("Staff ID: ", ticket.staff_id)
        print("Email Address: ", ticket.email)
        print("Description: ", ticket.description)
        print("Response: ", ticket.response_to_ticket)
        print("Ticket Status: ", ticket.status)

#Function to display a ticket details
def display_ticket_details():
    ticket_number = int(input("\nEnter the Ticket Number: "))
    for ticket in TicketData.tickets:
        if ticket.ticket_number == ticket_number:
            print("\nTicket Number: ", ticket.ticket_number)
            print("Ticket Creator: ", ticket.creator_name)
            print("Staff ID: ", ticket.staff_id)
            print("Email Address: ", ticket.email)
            print("Description: ", ticket.description)
            print("Response: ", ticket.response_to_ticket)
            print("Ticket Status: ", ticket.status)
            break

#Function to show ticket statistics
def display_ticket_stats():
  TicketData.show_ticket_statistics()

#Function to end program
def end_program():
  print("\nThank you for using our system 😊😊")

#Main() method creates an interface for the user to interact with the Help-desk Ticket System by choosing options from a menu
def main():
    while True:
        print("\n                    Welcome To the Help-desk Ticket System \n")
        print("Please choose an option from the list given below:-")
        print("1. Create a ticket")
        print("2. Reopen a ticket")
        print("3. Respond to a ticket")        
        print("4. Display all of the Tickets")
        print("5. Display details of a Ticket")
        print("6. Display Ticket Statistics")
        print("7. Exit\nEnter your choice: ")
        input_data  = int(input());

        if input_data == 1:
          create_ticket()

        elif input_data == 2:
          reopen_ticket()

        elif input_data == 3:
          respond_to_ticket()

        elif input_data == 4:
          display_all_tickets()

        elif input_data == 5:
          display_ticket_details()
          
        elif input_data == 6:
          display_ticket_stats()

        elif input_data == 7:
          end_program()
          exit()

        else:
            print("Invalid Choice. Please try again.") 


if __name__ == "__main__":
    main() 
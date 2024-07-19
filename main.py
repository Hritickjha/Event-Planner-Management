class Eventplanner:
    def __init__(self):
        self.events = []

    def add_event(self):
        event_name = input("Enter event name: ")
        event_date = input("Enter event date (YYYY-MM-DD): ")
        event_type = input("Enter event type (e.g, Meeting, Birthday, Conference):")

        self.events.append({"name":event_name,"date":event_date, "type":event_type})
        print("Event added successfully!")
        
    def view_events(self):
        if not self.events:
            print("No events available. ")
        else:
            print("upcoming Events:")
        for idx, event in enumerate(self.events, start=1):
            print(f"{idx}.{event['name']}({event['type']}) on {event['date']}")
    
    def delete_events(self):
        if not self.events:
            print("No events available to delete.")
        else:
            self.view_events()
            try:
                event_index = int(input("Enter the event number to delete: ")) - 1
                
                if 0 <= event_index < len(self.events):
                    
                    delete_event = self.events.pop (event_index)
                    print(f"Event'{delete_event['name']}' deleted successfully")
                else:
                    print("Invalid event number. Please try again.")
                
            except ValueError:
                print("Invalid input.Please enter a valid number.")
    
    def menu(self):
        while True:
            
            print("\nEvent planner Management System")
            print("1. Add Event")
            print("2. View Events")
            print("3. Delete Event")
            print("4. Exit")
            
            choice = input("Enter your choice: ")
                 
            if choice == "1":
                self.add_event()
            elif choice == "2":
                self.view_events()
            elif choice == "3":
                self.delete_events()
            elif choice == "4":
                print("Exiting the system GoodBye!")
                break
            else:
                print("Invalid choice.pleas enter a number between 1 and 4.")

if __name__ == "__main__":
    planner = Eventplanner() 
    planner.menu()              
                
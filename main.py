class Process:
    def __init__(self, p_id, name, start_time, priority):
        self.p_id = p_id
        self.name = name
        self.start_time = start_time
        self.priority = priority

    def __str__(self):
        return f"PID: {self.p_id}, Name: {self.name}, Start Time: {self.start_time}, Priority: {self.priority}"

def sort_processes_by_id(processes):
    return sorted(processes, key=lambda x: x.p_id)

def sort_processes_by_start_time(processes):
    return sorted(processes, key=lambda x: x.start_time)

def sort_processes_by_priority(processes):
    priorities = {'Low': 0, 'MID': 1, 'High': 2}
    return sorted(processes, key=lambda x: priorities[x.priority])

def main():
    processes = [
        Process("P1", "VSCode", 100, "MID"),
        Process("P23", "Eclipse", 234, "MID"),
        Process("P93", "Chrome", 189, "High"),
        Process("P42", "JDK",9, "High"),
        Process("P91", "CMD", 7, "High"),
        Process("P87", "NotePad", 23, "Low")
    ]

    while True:
        print("Menu:")
        print("1. Sort by Process ID")
        print("2. Sort by Start Time")
        print("3. Sort by Priority")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            sorted_processes = sort_processes_by_id(processes)
        elif choice == "2":
            sorted_processes = sort_processes_by_start_time(processes)
        elif choice == "3":
            sorted_processes = sort_processes_by_priority(processes)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please select a valid option.")
            continue

        print("Sorted Processes:")
        for process in sorted_processes:
            print(process)
        print()

if __name__ == "__main__":
    main()

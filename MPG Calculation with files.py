# File: SS_Lab_Week8A.py
# Date: 10/17/2025
#   A program to access a file and calculate mpg
#
# by: Sibi Seenivasan

FILENAME = "trips.txt"

def write_trips(trips):
    with open(FILENAME, "w") as file:
        file.write("Distance\tGallons\tMPG\n")
        for trip in trips:
            file.write(f"{trip[0]}\t{trip[1]}\t{trip[2]}\n")

def read_trips():
    trips = []
    # Using try-except to learn that
    try:
        with open(FILENAME, "r") as file:
            next(file)
            # Reading each line, split it, convert to float, and add to list
            for line in file:
                parts = line.split()
                if len(parts) >= 3:
                    miles = float(parts[0])
                    gallons = float(parts[1])
                    mpg = float(parts[2])
                    trips.append([miles, gallons, mpg])
    except:
        print(f"An error occurred reading the file")
        
    return trips

def list_trips(trips):
    print("Distance\tGallons\t\tMPG")
    for trip in trips:
        print(f"{trip[0]}\t\t{trip[1]}\t\t{trip[2]}")
    print()

def get_miles_driven():
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")       
    return miles_driven
          
def get_gallons_used():
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")
    return gallons_used
        
def main():
    # welcome message
    print("The Miles Per Gallon program")
    print()

    # Reading existing trips and display them
    trips = read_trips()
    list_trips(trips)

    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)
        print(f"Miles Per Gallon:\t{mpg}")
        
        # Adding new trip to list
        new_trip = [miles_driven, gallons_used, mpg]
        trips.append(new_trip)
        
        # Writing updated list back to file
        write_trips(trips)
        
        # Displaying updated list
        print()
        list_trips(trips)
        
        more = input("More entries? (y or n): ") 
    
    print("Bye!")

if __name__ == "__main__":
    main()
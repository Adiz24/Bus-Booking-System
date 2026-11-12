# BUS RESERVATION SYSTEM

FILE_NAME = "bookings.txt"

buses = {
    "B101": {"route": ("Pune", "Mumbai"), "time": "08:00 AM", "seats": 10, "fare": 450},
    "B102": {"route": ("Pune", "Nashik"), "time": "09:30 AM", "seats": 12, "fare": 350}
}

bookings = []
booking_number = 1001


class Passenger:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Booking:
    def __init__(self, booking_id, passenger, bus_id, seat, fare, status="CONFIRMED"):
        self.booking_id = booking_id
        self.passenger = passenger
        self.bus_id = bus_id
        self.seat = seat
        self.fare = fare
        self.status = status


def calculate_fare(fare, age):
    if age < 12:
        return fare * 0.5
    elif age >= 60:
        return fare * 0.7
    else:
        return fare


def save_data():
    with open(FILE_NAME, "w") as file:
        file.write(str(booking_number) + "\n")

        for b in bookings:
            file.write(
                b.booking_id + "|" + b.passenger.name + "|" +
                str(b.passenger.age) + "|" + b.bus_id + "|" +
                str(b.seat) + "|" + str(b.fare) + "|" +
                b.status + "\n"
            )


def load_data():
    global booking_number

    try:
        with open(FILE_NAME, "r") as file:
            booking_number = int(file.readline())

            for line in file:
                data = line.strip().split("|")

                if len(data) == 7:
                    passenger = Passenger(data[1], int(data[2]))
                    booking = Booking(
                        data[0], passenger, data[3], int(data[4]),
                        float(data[5]), data[6]
                    )
                    bookings.append(booking)

    except FileNotFoundError:
        pass
    except ValueError:
        print("Saved data is not correct.")


def display_menu():
    print("\n===== BUS RESERVATION SYSTEM =====")
    print("1. View Buses")
    print("2. View Available Seats")
    print("3. Book Ticket")
    print("4. Cancel Ticket")
    print("5. View Booking")
    print("6. Search Passenger / Booking")
    print("7. Exit")


def view_buses():
    print("\nBUS ID\tROUTE\tTIME\tFARE\tAVAILABLE")

    for bus_id, bus in buses.items():
        booked = set()

        for b in bookings:
            if b.bus_id == bus_id and b.status == "CONFIRMED":
                booked.add(b.seat)

        available = bus["seats"] - len(booked)
        route = bus["route"][0] + "-" + bus["route"][1]

        print(bus_id, route, bus["time"], "Rs.", bus["fare"], available)


def view_seats():
    bus_id = input("Enter Bus ID: ").upper()

    if bus_id not in buses:
        print("Invalid Bus ID.")
        return

    booked = []

    for b in bookings:
        if b.bus_id == bus_id and b.status == "CONFIRMED":
            booked.append(b.seat)

    available = []

    print("\nSeats for", bus_id)
    for seat in range(1, buses[bus_id]["seats"] + 1):
        if seat in booked:
            print("[XX]", end=" ")
        else:
            print("[" + str(seat).zfill(2) + "]", end=" ")
            available.append(seat)

        if seat % 2 == 0:
            print()

    print("\nAvailable seats:", available)


def book_ticket():
    global booking_number

    name = input("Enter passenger name: ").strip().title()

    try:
        age = int(input("Enter age: "))
        if age <= 0:
            print("Age must be greater than zero.")
            return
    except ValueError:
        print("Enter age as a number.")
        return

    bus_id = input("Enter Bus ID: ").upper()

    if bus_id not in buses:
        print("Bus not found.")
        return

    try:
        seat = int(input("Enter seat number: "))
    except ValueError:
        print("Seat must be a number.")
        return

    if seat < 1 or seat > buses[bus_id]["seats"]:
        print("Invalid seat number.")
        return

    for b in bookings:
        if b.bus_id == bus_id and b.seat == seat and b.status == "CONFIRMED":
            print("This seat is already booked.")
            return

    passenger = Passenger(name, age)
    fare = calculate_fare(buses[bus_id]["fare"], age)
    booking_id = "ST" + str(booking_number)
    booking_number += 1

    booking = Booking(booking_id, passenger, bus_id, seat, fare)
    bookings.append(booking)
    save_data()

    print("\nBooking successful!")
    print("Booking ID:", booking_id)
    print("Passenger:", name)
    print("Bus:", bus_id)
    print("Seat:", seat)
    print("Fare: Rs.", fare)


def find_booking(booking_id):
    for b in bookings:
        if b.booking_id == booking_id:
            return b
    return None


def show_booking(b):
    route = buses[b.bus_id]["route"]

    print("\n===== BOOKING DETAILS =====")
    print("Booking ID:", b.booking_id)
    print("Passenger:", b.passenger.name)
    print("Age:", b.passenger.age)
    print("Bus:", b.bus_id)
    print("Route:", route[0], "to", route[1])
    print("Seat:", b.seat)
    print("Fare: Rs.", b.fare)
    print("Status:", b.status)


def cancel_ticket():
    booking_id = input("Enter Booking ID: ").upper()
    b = find_booking(booking_id)

    if b is None:
        print("Booking not found.")
    elif b.status == "CANCELLED":
        print("This ticket is already cancelled.")
    else:
        answer = input("Are you sure you want to cancel? (yes/no): ").lower()

        if answer == "yes":
            b.status = "CANCELLED"
            save_data()
            print("Ticket cancelled. Seat is now available.")
        else:
            print("Cancellation stopped.")


def view_booking():
    booking_id = input("Enter Booking ID: ").upper()
    b = find_booking(booking_id)

    if b is None:
        print("Booking not found.")
    else:
        show_booking(b)


def search_booking():
    search = input("Enter passenger name or Booking ID: ").lower()
    found = False

    for b in bookings:
        if search in b.passenger.name.lower() or search in b.booking_id.lower():
            show_booking(b)
            found = True

    if found == False:
        print("No booking found.")


def main():
    load_data()

    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if choice == 1:
            view_buses()
        elif choice == 2:
            view_seats()
        elif choice == 3:
            book_ticket()
        elif choice == 4:
            cancel_ticket()
        elif choice == 5:
            view_booking()
        elif choice == 6:
            search_booking()
        elif choice == 7:
            save_data()
            print("Thank you for using the Bus Reservation System.")
            break
        else:
            print("Invalid choice.")


main()


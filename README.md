# 🚌 Bus Reservation System

A console-based Bus Reservation System developed using **Python**. This project allows users to view available buses, check seat availability, book tickets, cancel reservations, and search booking details.

## 📌 Features

- 🚌 **View Buses:** Display available buses, routes, timings, and ticket fares.
- 💺 **Seat Availability:** Check booked and available seats.
- 🎫 **Book Tickets:** Reserve seats by entering passenger details.
- 💰 **Fare Calculation:** Automatically calculate ticket fares based on passenger age.
  - Children below 12 years get a 50% discount.
  - Senior citizens (60 years and above) get a 30% discount.
- ❌ **Cancel Tickets:** Cancel existing reservations and release seats.
- 📋 **View Booking:** Display complete booking details using a booking ID.
- 🔍 **Search Booking:** Search bookings using passenger names or booking IDs.
- 💾 **Data Persistence:** Save and load booking information using a text file.

## 🛠️ Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- File Handling
- Lists, Dictionaries, and Sets
- Functions and Conditional Statements
- Exception Handling

## 🚌 Available Bus Routes

| Bus ID | Route | Departure | Fare |
|---|---|---|---|
| B101 | Pune – Mumbai | 08:00 AM | ₹450 |
| B102 | Pune – Nashik | 09:30 AM | ₹350 |

## 📂 Project Structure

```text
Bus-Reservation-System/
│
├── Bus_Booking_System.py
├── README.md
└── bookings.txt (created automatically)
```

## 🚀 How to Run the Project

**Step 1:** Clone the repository.

```bash
git clone https://github.com/Adiz24/Bus-Reservation-System.git
```

**Step 2:** Navigate to the project directory.

```bash
cd Bus-Reservation-System
```

**Step 3:** Run the Python file.

```bash
python Bus_Booking_System.py
```

**Step 4:** Follow the menu displayed in the terminal to use the system.

## 📚 Concepts Practiced

- Classes and Objects
- Constructors (`__init__`)
- Functions and Modular Programming
- File Handling (`open`, `read`, `write`)
- Exception Handling (`try-except`)
- Data Structures (List, Dictionary, Set)
- Data Validation and Conditional Logic

## 🔮 Future Improvements

- Add a Graphical User Interface (GUI).
- Integrate a database such as MySQL.
- Add more bus routes and schedules.
- Implement online payment functionality.
- Add an admin panel for bus management.

## 👨‍💻 Author

**Aditya Gupta**

- GitHub: [Adiz24](https://github.com/Adiz24)

---

⭐ If you find this project useful, feel free to star the repository!

import hashlib

# rail operations and revenue management
users_db = {}
reservations = []
available_trains = {
    "101": {"route": "Mumbai - Delhi", "seats": 5, "fare": 1200},
    "102": {"route": "Delhi - Kolkata", "seats": 3, "fare": 1500},
    "103": {"route": "Chennai - Bengaluru", "seats": 4, "fare": 800}
}
train_status = {
    "101": "On Time",
    "102": "Delayed",
    "103": "On Time"
}

seat_types = {
    "AC": 1.5,       # 50% extra fare
    "3AC": 1.2,      # 20% extra fare
    "SLEEPER": 1.0   # Base fare
}

# user_registration
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user():
    username = input("Enter username: ")
    if username in users_db:
        print("❌ Username already exists!")
        return None
    password = input("Enter password: ")
    name = input("Enter full name: ")
    email = input("Enter email: ")
    users_db[username] = {
        "password": hash_password(password),
        "name": name,
        "email": email
    }
    print("✅ Registration successful!")
    return username

# login info
def login_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users_db and users_db[username]["password"] == hash_password(password):
        print(f"✅ Welcome, {users_db[username]['name']}!")
        return username
    else:
        print("❌ Invalid username or password")
        return None

# reservation and ticketing
def view_trains():
    for no, info in available_trains.items():
        print(f"{no}: {info['route']} | Seats: {info['seats']} | Fare: ₹{info['fare']} (Base)")

def select_seat_type():
    print("\nAvailable Seat Types:")
    for i, (stype, multiplier) in enumerate(seat_types.items(), start=1):
        print(f"{i}. {stype} - Fare x{multiplier}")
    choice = input("Choose seat type (1-3): ")
    seat_type_list = list(seat_types.keys())
    if choice.isdigit() and 1 <= int(choice) <= len(seat_type_list):
        return seat_type_list[int(choice)-1]
    else:
        print("❌ Invalid choice, defaulting to Sleeper.")
        return "SLEEPER"

def book_ticket(username):
    view_trains()
    train_no = input("Enter train number to book: ")
    if train_no not in available_trains:
        print("❌ Train not found")
        return
    if available_trains[train_no]["seats"] <= 0:
        print("❌ No seats available")
        return

    passenger_name = input("Enter passenger name: ")
    seat_type = select_seat_type()
    base_fare = available_trains[train_no]["fare"]
    final_fare = int(base_fare * seat_types[seat_type])

    available_trains[train_no]["seats"] -= 1  # Reduce seat count when booked

    ticket = {
        "train": train_no,
        "passenger": passenger_name,
        "seat_type": seat_type,
        "fare": final_fare
    }
    reservations.append(ticket)
    print(f"✅ Ticket booked: {ticket}")

def get_train_status():
    train_no = input("Enter train number: ")
    print("📢 Status:", train_status.get(train_no, "Status not available"))

def update_train_status():
    train_no = input("Enter train number: ")
    if train_no not in train_status:
        print("❌ Train not found")
        return
    status = input("Enter new status: ")
    train_status[train_no] = status
    print(f"✅ Train {train_no} status updated to {status}")

def generate_revenue_report():
    total = sum(ticket["fare"] for ticket in reservations)
    print(f"💰 Total Revenue: ₹{total:,}")

# multi channel distribution
print("=== 🚄 Railway Reservation System ===")

# Register
print("\n-- Registration --")
register_user()

# Login
print("\n-- Login --")
user = login_user()
if not user:
    print("❌ Exiting due to failed login.")
    exit()

# View trains
print("\n-- Available Trains --")
view_trains()

# Book ticket       
print("\n-- Ticket Booking --")
book_ticket(user)

# Check Train Status
print("\n-- Train Status Check --")
get_train_status()

# Update Train Status
print("\n-- Update Train Status --")
update_train_status()

# Revenue Report
print("\n-- Revenue Report --")
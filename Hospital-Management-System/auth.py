from storage import load_data, save_data

USERS_FILE = "data/users.json"


def load_users():
    return load_data(USERS_FILE)


def save_users(users):
    save_data(USERS_FILE, users)


def register():
    print("\n===== REGISTER =====")

    username = input("Enter username: ").strip()

    if not username:
        print("Username cannot be empty!")
        return

    password = input("Enter password: ").strip()

    if not password:
        print("Password cannot be empty!")
        return

    users = load_users()

    for user in users:
        if user["username"] == username:
            print("Username already exists!")
            return

    role = input("Enter role (admin/doctor/receptionist): ").strip().lower()

    if role not in ["admin", "doctor", "receptionist"]:
        print("Invalid role!")
        return

    new_user = {
        "username": username,
        "password": password,
        "role": role
    }

    users.append(new_user)
    save_users(users)

    print("Registration successful!")


def login():
    print("\n===== LOGIN =====")

    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if not username or not password:
        print("Username and password cannot be empty!")
        return None

    users = load_users()

    for user in users:
        if user["username"] == username and user["password"] == password:
            print("Login successful!")
            print("Role:", user["role"])
            return user

    print("Invalid username or password!")
    return None
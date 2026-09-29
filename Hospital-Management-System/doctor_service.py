from storage import load_data, save_data
from exceptions import DoctorNotFoundError


def validate_input(value, field_name):
    if not value.strip():
        print(field_name, "cannot be empty!")
        return False

    return True


DOCTORS_FILE = "data/doctors.json"


def load_doctors():
    return load_data(DOCTORS_FILE)


def save_doctors(doctors):
    save_data(DOCTORS_FILE, doctors)


def add_doctor():
    print("\n===== ADD DOCTOR =====")

    doctor_id = input("Enter doctor ID: ")

    if not validate_input(doctor_id, "Doctor ID"):
        return

    name = input("Enter doctor name: ")

    if not validate_input(name, "Doctor Name"):
        return
    specialty = input("Enter specialty: ")

    if not validate_input(specialty, "Specialty"):
        return
    phone = input("Enter phone: ")

    if not phone.isdigit():
        print("Phone must contain numbers only!")
        return

    doctors = load_doctors()

    for doctor in doctors:
        if doctor["doctor_id"] == doctor_id:
            print("Doctor ID already exists!")
            return

    new_doctor = {
        "doctor_id": doctor_id,
        "name": name,
        "specialty": specialty,
        "phone": phone
    }

    doctors.append(new_doctor)
    save_doctors(doctors)

    print("Doctor added successfully!")


def view_doctors():
    print("\n===== DOCTOR LIST =====")

    doctors = load_doctors()

    if not doctors:
        print("No doctors found.")
        return

    for doctor in doctors:
        print("----------------------------")
        print("ID:", doctor["doctor_id"])
        print("Name:", doctor["name"])
        print("Specialty:", doctor["specialty"])
        print("Phone:", doctor["phone"])


def search_doctor():
    print("\n===== SEARCH DOCTOR =====")

    doctor_id = input("Enter doctor ID: ")

    doctors = load_doctors()

    for doctor in doctors:
        if doctor["doctor_id"] == doctor_id:
            print("\nDoctor found!")
            print("ID:", doctor["doctor_id"])
            print("Name:", doctor["name"])
            print("Specialty:", doctor["specialty"])
            print("Phone:", doctor["phone"])
            return

    raise DoctorNotFoundError("Doctor not found.")

def update_doctor():
    print("\n===== UPDATE DOCTOR =====")

    doctor_id = input("Enter doctor ID: ")

    doctors = load_doctors()

    for doctor in doctors:
        if doctor["doctor_id"] == doctor_id:
            doctor["name"] = input("Enter new name: ")
            doctor["specialty"] = input("Enter new specialty: ")
            doctor["phone"] = input("Enter new phone: ")

            save_doctors(doctors)

            print("Doctor updated successfully!")
            return

    raise DoctorNotFoundError("Doctor not found.")

def delete_doctor():
    print("\n===== DELETE DOCTOR =====")

    doctor_id = input("Enter doctor ID: ")

    doctors = load_doctors()

    for doctor in doctors:
        if doctor["doctor_id"] == doctor_id:
            doctors.remove(doctor)
            save_doctors(doctors)

            print("Doctor deleted successfully!")
            return

    raise DoctorNotFoundError("Doctor not found.")
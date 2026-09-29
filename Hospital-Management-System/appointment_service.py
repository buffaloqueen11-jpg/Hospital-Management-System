from storage import load_data, save_data
from exceptions import AppointmentNotFoundError
def validate_input(value, field_name):
    if not value.strip():
        print(field_name, "cannot be empty!")
        return False

    return True

APPOINTMENTS_FILE = "data/appointments.json"


def load_appointments():
    return load_data(APPOINTMENTS_FILE)


def save_appointments(appointments):
    save_data(APPOINTMENTS_FILE, appointments)

def add_appointment():
    print("\n===== ADD APPOINTMENT =====")

    appointment_id = input("Enter appointment ID: ")

    if not validate_input(appointment_id, "Appointment ID"):
        return
    patient_id = input("Enter patient ID: ")

    if not validate_input(patient_id, "Patient ID"):
        return

    doctor_id = input("Enter doctor ID: ")

    if not validate_input(doctor_id, "Doctor ID"):
        return
    date = input("Enter date: ")

    if not validate_input(date, "Date"):
        return

    time = input("Enter time: ")

    if not validate_input(time, "Time"):
        return
    appointments = load_appointments()

    for appointment in appointments:
        if appointment["appointment_id"] == appointment_id:
            print("Appointment ID already exists!")
            return

    new_appointment = {
        "appointment_id": appointment_id,
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "date": date,
        "time": time
    }

    appointments.append(new_appointment)
    save_appointments(appointments)

    print("Appointment added successfully!")


def view_appointments():
    print("\n===== APPOINTMENT LIST =====")

    appointments = load_appointments()

    if not appointments:
        print("No appointments found.")
        return

    for appointment in appointments:
        print("----------------------------")
        print("Appointment ID:", appointment["appointment_id"])
        print("Patient ID:", appointment["patient_id"])
        print("Doctor ID:", appointment["doctor_id"])
        print("Date:", appointment["date"])
        print("Time:", appointment["time"])


def search_appointment():
    print("\n===== SEARCH APPOINTMENT =====")

    appointment_id = input("Enter appointment ID: ")

    appointments = load_appointments()

    for appointment in appointments:
        if appointment["appointment_id"] == appointment_id:
            print("\nAppointment found!")
            print("Appointment ID:", appointment["appointment_id"])
            print("Patient ID:", appointment["patient_id"])
            print("Doctor ID:", appointment["doctor_id"])
            print("Date:", appointment["date"])
            print("Time:", appointment["time"])
            return

    raise AppointmentNotFoundError("Appointment not found.")


def update_appointment():
    print("\n===== UPDATE APPOINTMENT =====")

    appointment_id = input("Enter appointment ID: ")

    appointments = load_appointments()

    for appointment in appointments:
        if appointment["appointment_id"] == appointment_id:
            appointment["patient_id"] = input("Enter new patient ID: ")
            appointment["doctor_id"] = input("Enter new doctor ID: ")
            appointment["date"] = input("Enter new date: ")
            appointment["time"] = input("Enter new time: ")

            save_appointments(appointments)

            print("Appointment updated successfully!")
            return

    raise AppointmentNotFoundError("Appointment not found.")


def delete_appointment():
    print("\n===== DELETE APPOINTMENT =====")

    appointment_id = input("Enter appointment ID: ")

    appointments = load_appointments()

    for appointment in appointments:
        if appointment["appointment_id"] == appointment_id:
            appointments.remove(appointment)
            save_appointments(appointments)

            print("Appointment deleted successfully!")
            return

    raise AppointmentNotFoundError("Appointment not found.")
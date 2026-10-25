from storage import load_data, save_data
from exceptions import AppointmentNotFoundError

PATIENTS_FILE = "data/patients.json"
DOCTORS_FILE = "data/doctors.json"
APPOINTMENTS_FILE = "data/appointments.json"


def validate_input(value, field_name):
    if not value.strip():
        print(field_name, "cannot be empty!")
        return False

    return True


def load_appointments():
    return load_data(APPOINTMENTS_FILE)


def save_appointments(appointments):
    save_data(APPOINTMENTS_FILE, appointments)


def patient_exists(patient_id):
    patients = load_data(PATIENTS_FILE)

    for patient in patients:
        if patient["patient_id"] == patient_id:
            return True

    return False


def doctor_exists(doctor_id):
    doctors = load_data(DOCTORS_FILE)

    for doctor in doctors:
        if doctor["doctor_id"] == doctor_id:
            return True

    return False


def add_appointment():
    print("\n===== ADD APPOINTMENT =====")

    appointment_id = input("Enter appointment ID: ").strip()

    if not validate_input(appointment_id, "Appointment ID"):
        return

    patient_id = input("Enter patient ID: ").strip()

    if not validate_input(patient_id, "Patient ID"):
        return

    if not patient_exists(patient_id):
        print("Patient not found!")
        return

    doctor_id = input("Enter doctor ID: ").strip()

    if not validate_input(doctor_id, "Doctor ID"):
        return

    if not doctor_exists(doctor_id):
        print("Doctor not found!")
        return

    date = input("Enter date: ").strip()

    if not validate_input(date, "Date"):
        return

    time = input("Enter time: ").strip()

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

    appointment_id = input("Enter appointment ID: ").strip()

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

    appointment_id = input("Enter appointment ID: ").strip()

    if not validate_input(appointment_id, "Appointment ID"):
        return

    appointments = load_appointments()

    for appointment in appointments:
        if appointment["appointment_id"] == appointment_id:

            patient_id = input("Enter new patient ID: ").strip()

            if not validate_input(patient_id, "Patient ID"):
                return

            if not patient_exists(patient_id):
                print("Patient not found!")
                return

            doctor_id = input("Enter new doctor ID: ").strip()

            if not validate_input(doctor_id, "Doctor ID"):
                return

            if not doctor_exists(doctor_id):
                print("Doctor not found!")
                return

            date = input("Enter new date: ").strip()

            if not validate_input(date, "Date"):
                return

            time = input("Enter new time: ").strip()

            if not validate_input(time, "Time"):
                return

            appointment["patient_id"] = patient_id
            appointment["doctor_id"] = doctor_id
            appointment["date"] = date
            appointment["time"] = time

            save_appointments(appointments)

            print("Appointment updated successfully!")
            return

    raise AppointmentNotFoundError("Appointment not found.")
def delete_appointment():
    print("\n===== DELETE APPOINTMENT =====")

    appointment_id = input("Enter appointment ID: ").strip()

    if not validate_input(appointment_id, "Appointment ID"):
        return

    appointments = load_appointments()

    for appointment in appointments:
        if appointment["appointment_id"] == appointment_id:
            appointments.remove(appointment)
            save_appointments(appointments)

            print("Appointment deleted successfully!")
            return

    raise AppointmentNotFoundError("Appointment not found.")
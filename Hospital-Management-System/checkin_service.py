from storage import load_data, save_data
from exceptions import AppointmentNotFoundError

APPOINTMENTS_FILE = "data/appointments.json"


def load_appointments():
    return load_data(APPOINTMENTS_FILE)


def save_appointments(appointments):
    save_data(APPOINTMENTS_FILE, appointments)

def check_in():
    print("\n===== PATIENT CHECK-IN =====")

    appointment_id = input("Enter appointment ID: ")

    appointments = load_appointments()

    for appointment in appointments:
        if appointment["appointment_id"] == appointment_id:
            appointment["status"] = "Checked-in"
            save_appointments(appointments)

            print("Check-in successful!")
            return

    raise AppointmentNotFoundError("Appointment not found.")

def check_out():
    print("\n===== PATIENT CHECK-OUT =====")

    appointment_id = input("Enter appointment ID: ")

    appointments = load_appointments()

    for appointment in appointments:
        if appointment["appointment_id"] == appointment_id:
            appointment["status"] = "Checked-out"
            save_appointments(appointments)
            print("Check-out successful!")
            return

    raise AppointmentNotFoundError("Appointment not found.")
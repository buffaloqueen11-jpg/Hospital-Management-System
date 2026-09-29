from storage import load_data


APPOINTMENTS_FILE = "data/appointments.json"


def load_appointments():
    return load_data(APPOINTMENTS_FILE)


def view_appointment_history():
    print("\n===== APPOINTMENT HISTORY =====")

    appointments = load_appointments()

    if not appointments:
        print("No appointment history found.")
        return

    for appointment in appointments:
        print("----------------------------")
        print("Appointment ID:", appointment["appointment_id"])
        print("Patient ID:", appointment["patient_id"])
        print("Doctor ID:", appointment["doctor_id"])
        print("Date:", appointment["date"])
        print("Time:", appointment["time"])
        print("Status:", appointment.get("status", "Scheduled"))    
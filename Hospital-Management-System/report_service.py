from storage import load_data

PATIENTS_FILE = "data/patients.json"
DOCTORS_FILE = "data/doctors.json"
APPOINTMENTS_FILE = "data/appointments.json"
PAYMENTS_FILE = "data/payments.json"


def show_report():
    print("\n===== HOSPITAL REPORT =====")

    patients = load_data(PATIENTS_FILE)
    doctors = load_data(DOCTORS_FILE)
    appointments = load_data(APPOINTMENTS_FILE)
    payments = load_data(PAYMENTS_FILE)

    total_patients = len(patients)
    total_doctors = len(doctors)
    total_appointments = len(appointments)
    total_payments = len(payments)

    total_amount = 0

    for payment in payments:
        try:
            amount = float(payment.get("amount", 0) or 0)
            total_amount += amount
        except (ValueError, TypeError):
            print(
                "Warning: Invalid amount in payment",
                payment.get("payment_id", "Unknown")
            )

    print("Total Patients:", total_patients)
    print("Total Doctors:", total_doctors)
    print("Total Appointments:", total_appointments)
    print("Total Payments:", total_payments)
    print("Total Payment Amount:", total_amount)


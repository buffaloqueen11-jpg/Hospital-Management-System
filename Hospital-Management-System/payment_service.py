from storage import load_data, save_data
from exceptions import PaymentNotFoundError

def validate_input(value, field_name):
    if not value.strip():
        print(field_name, "cannot be empty!")
        return False

    return True

PAYMENTS_FILE = "data/payments.json"


def load_payments():
    return load_data(PAYMENTS_FILE)


def save_payments(payments):
    save_data(PAYMENTS_FILE, payments)

def add_payment():
    print("\n===== ADD PAYMENT =====")

    payment_id = input("Enter payment ID: ")

    if not validate_input(payment_id, "Payment ID"):
        return
    patient_id = input("Enter patient ID: ")

    if not validate_input(patient_id, "Patient ID"):
        return

    amount = input("Enter amount: ")

    if not amount.strip():
        print("Amount cannot be empty!")
        return

    try:
        amount = float(amount)
    except ValueError:
        print("Amount must be a number!")
        return

    if amount <= 0:
        print("Amount must be greater than 0!")
        return
    payment_date = input("Enter payment date: ")

    if not validate_input(payment_date, "Payment Date"):
        return
    status = input("Enter status (Paid/Pending): ")

    if status not in ["Paid", "Pending"]:
        print("Status must be Paid or Pending!")
        return

    payments = load_payments()

    for payment in payments:
        if payment["payment_id"] == payment_id:
            print("Payment ID already exists!")
            return

    new_payment = {
        "payment_id": payment_id,
        "patient_id": patient_id,
        "amount": amount,
        "payment_date": payment_date,
        "status": status
    }

    payments.append(new_payment)
    save_payments(payments)

    print("Payment added successfully!")


def view_payments():
    print("\n===== PAYMENT LIST =====")

    payments = load_payments()

    if not payments:
        print("No payments found.")
        return

    for payment in payments:
        print("----------------------------")
        print("Payment ID:", payment["payment_id"])
        print("Patient ID:", payment["patient_id"])
        print("Amount:", payment["amount"])
        print("Payment Date:", payment["payment_date"])
        print("Status:", payment["status"])


def search_payment():
    print("\n===== SEARCH PAYMENT =====")

    payment_id = input("Enter payment ID: ")

    payments = load_payments()

    for payment in payments:
        if payment["payment_id"] == payment_id:
            print("\nPayment found!")
            print("Payment ID:", payment["payment_id"])
            print("Patient ID:", payment["patient_id"])
            print("Amount:", payment["amount"])
            print("Payment Date:", payment["payment_date"])
            print("Status:", payment["status"])
            return

    raise PaymentNotFoundError("Payment not found.")

def update_payment():
    print("\n===== UPDATE PAYMENT =====")

    payment_id = input("Enter payment ID: ")

    payments = load_payments()

    for payment in payments:
        if payment["payment_id"] == payment_id:
            payment["patient_id"] = input("Enter new patient ID: ")
            payment["amount"] = input("Enter new amount: ")
            payment["payment_date"] = input("Enter new payment date: ")
            payment["status"] = input("Enter new status (Paid/Pending): ")

            save_payments(payments)

            print("Payment updated successfully!")
            return

    raise PaymentNotFoundError("Payment not found.")


def delete_payment():
    print("\n===== DELETE PAYMENT =====")

    payment_id = input("Enter payment ID: ")

    payments = load_payments()

    for payment in payments:
        if payment["payment_id"] == payment_id:
            payments.remove(payment)
            save_payments(payments)

            print("Payment deleted successfully!")
            return

    raise PaymentNotFoundError("Payment not found.")
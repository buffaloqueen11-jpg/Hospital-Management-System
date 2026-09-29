from storage import load_data, save_data
from exceptions import MedicalRecordNotFoundError

def validate_input(value, field_name):
    if not value.strip():
        print(field_name, "cannot be empty!")
        return False

    return True


MEDICAL_RECORDS_FILE = "data/medical_records.json"


def load_medical_records():
    return load_data(MEDICAL_RECORDS_FILE)


def save_medical_records(records):
    save_data(MEDICAL_RECORDS_FILE, records)


def add_medical_record():
    print("\n===== ADD MEDICAL RECORD =====")

    record_id = input("Enter record ID: ")

    if not validate_input(record_id, "Record ID"):
        return

    patient_id = input("Enter patient ID: ")

    if not validate_input(patient_id, "Patient ID"):
        return
    doctor_id = input("Enter doctor ID: ")

    if not validate_input(doctor_id, "Doctor ID"):   
        return
    date = input("Enter date: ")
    symptoms = input("Enter symptoms: ")
    diagnosis = input("Enter diagnosis: ")
    treatment = input("Enter treatment: ")
    notes = input("Enter notes: ")

    records = load_medical_records()

    for record in records:
        if record["record_id"] == record_id:
            print("Record ID already exists!")
            return

    new_record = {
        "record_id": record_id,
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "date": date,
        "symptoms": symptoms,
        "diagnosis": diagnosis,
        "treatment": treatment,
        "notes": notes
    }

    records.append(new_record)
    save_medical_records(records)

    print("Medical record added successfully!")


def view_medical_records():
    print("\n===== MEDICAL RECORD LIST =====")

    records = load_medical_records()

    if not records:
        print("No medical records found.")
        return

    for record in records:
        print("----------------------------")
        print("Record ID:", record["record_id"])
        print("Patient ID:", record["patient_id"])
        print("Doctor ID:", record["doctor_id"])
        print("Date:", record["date"])
        print("Symptoms:", record["symptoms"])
        print("Diagnosis:", record["diagnosis"])
        print("Treatment:", record["treatment"])
        print("Notes:", record["notes"])

def update_medical_record():
    print("\n===== UPDATE MEDICAL RECORD =====")

    record_id = input("Enter record ID: ")

    records = load_medical_records()

    for record in records:
        if record["record_id"] == record_id:

            record["patient_id"] = input("Enter new patient ID: ")
            record["doctor_id"] = input("Enter new doctor ID: ")
            record["date"] = input("Enter new date: ")
            record["symptoms"] = input("Enter new symptoms: ")
            record["diagnosis"] = input("Enter new diagnosis: ")
            record["treatment"] = input("Enter new treatment: ")
            record["notes"] = input("Enter new notes: ")

            save_medical_records(records)

            print("Medical record updated successfully!")
            return

    raise MedicalRecordNotFoundError("Medical record not found.")  

def delete_medical_record():
    print("\n===== DELETE MEDICAL RECORD =====")

    record_id = input("Enter record ID: ")

    records = load_medical_records()

    for record in records:
        if record["record_id"] == record_id:
            records.remove(record)
            save_medical_records(records)

            print("Medical record deleted successfully!")
            return

    raise MedicalRecordNotFoundError("Medical record not found.")
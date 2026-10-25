from storage import load_data, save_data
from exceptions import PrescriptionNotFoundError

PATIENTS_FILE = "data/patients.json"
DOCTORS_FILE = "data/doctors.json"

def validate_input(value, field_name):
    if not value.strip():
        print(field_name, "cannot be empty!")
        return False

    return True


PRESCRIPTIONS_FILE = "data/prescriptions.json"


def load_prescriptions():
    return load_data(PRESCRIPTIONS_FILE)

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

def save_prescriptions(prescriptions):
    save_data(PRESCRIPTIONS_FILE, prescriptions)

def add_prescription():
    print("\n===== ADD PRESCRIPTION =====")

    prescription_id = input("Enter prescription ID: ")
    if not validate_input(prescription_id, "Prescription ID"):
        return
    patient_id = input("Enter patient ID: ")
    if not validate_input(patient_id, "Patient ID"): 
        return    
    doctor_id = input("Enter doctor ID: ")
    if not validate_input(doctor_id, "Doctor ID"):
        return
    
    if not patient_exists(patient_id):
        print("Patient not found!")
        return

    if not doctor_exists(doctor_id):
        print("Doctor not found!")
        return

    medicine = input("Enter medicine: ")
    if not validate_input(medicine, "Medicine"):
        return
    
    dosage = input("Enter dosage: ")
    if not validate_input(dosage, "Dosage"):
        return
    duration = input("Enter duration: ")
    if not validate_input(duration, "Duration"):
        return
    instructions = input("Enter instructions: ")
    if not validate_input(instructions, "Instructions"):
        return
    
    prescriptions = load_prescriptions()

    for prescription in prescriptions:
        if prescription["prescription_id"] == prescription_id:
            print("Prescription ID already exists!")
            return

    new_prescription = {
        "prescription_id": prescription_id,
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "medicine": medicine,
        "dosage": dosage,
        "duration": duration,
        "instructions": instructions
    }

    prescriptions.append(new_prescription)
    save_prescriptions(prescriptions)

    print("Prescription added successfully!")


def view_prescriptions():
    print("\n===== PRESCRIPTION LIST =====")

    prescriptions = load_prescriptions()

    if not prescriptions:
        print("No prescriptions found.")
        return

    for prescription in prescriptions:
        print("----------------------------")
        print("Prescription ID:", prescription["prescription_id"])
        print("Patient ID:", prescription["patient_id"])
        print("Doctor ID:", prescription["doctor_id"])
        print("Medicine:", prescription["medicine"])
        print("Dosage:", prescription["dosage"])
        print("Duration:", prescription["duration"])
        print("Instructions:", prescription["instructions"])

def update_prescription():
    print("\n===== UPDATE PRESCRIPTION =====")

    prescription_id = input("Enter prescription ID: ")

    if not validate_input(prescription_id, "Prescription ID"):
        return
    
    prescriptions = load_prescriptions()

    for prescription in prescriptions:
        if prescription["prescription_id"] == prescription_id:
            
            new_patient_id = input("Enter new patient ID: ")

            if not validate_input(new_patient_id, "Patient ID"):
                return

            if not patient_exists(new_patient_id):
                print("Patient not found!")
                return

            prescription["patient_id"] = new_patient_id

            new_doctor_id = input("Enter new doctor ID: ")

            if not validate_input(new_doctor_id, "Doctor ID"):
                return

            if not doctor_exists(new_doctor_id):
                print("Doctor not found!")
                return

            prescription["doctor_id"] = new_doctor_id
            
            new_medicine = input("Enter new medicine: ")

            if not validate_input(new_medicine, "Medicine"):
                return

            prescription["medicine"] = new_medicine

            new_dosage = input("Enter new dosage: ")

            if not validate_input(new_dosage, "Dosage"):
                return

            prescription["dosage"] = new_dosage

            new_duration = input("Enter new duration: ")

            if not validate_input(new_duration, "Duration"):
                return

            prescription["duration"] = new_duration

            new_instructions = input("Enter new instructions: ")

            if not validate_input(new_instructions, "Instructions"):
                return

            prescription["instructions"] = new_instructions

            save_prescriptions(prescriptions)

            print("Prescription updated successfully!")
            return

    raise PrescriptionNotFoundError("Prescription not found.")

def delete_prescription():
    print("\n===== DELETE PRESCRIPTION =====")

    prescription_id = input("Enter prescription ID: ")

    if not validate_input(prescription_id, "Prescription ID"):
        return
 
    prescriptions = load_prescriptions()

    for prescription in prescriptions:
        if prescription["prescription_id"] == prescription_id:
            prescriptions.remove(prescription)
            save_prescriptions(prescriptions)

            print("Prescription deleted successfully!")
            return
        
    raise PrescriptionNotFoundError("Prescription not found.")
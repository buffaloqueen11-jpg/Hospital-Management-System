from storage import load_data, save_data
from exceptions import PatientNotFoundError

def validate_input(value, field_name):
    if not value.strip():
        print(field_name, "cannot be empty!")
        return False

    return True


PATIENTS_FILE = "data/patients.json"


def load_patients():
    return load_data(PATIENTS_FILE)


def save_patients(patients):
    save_data(PATIENTS_FILE, patients)


def add_patient():
    print("\n===== ADD PATIENT =====")

    patient_id = input("Enter patient ID: ")

    if not validate_input(patient_id, "Patient ID"):
        return

    name = input("Enter patient name: ")

    if not validate_input(name, "Patient Name"):
        return

    age = input("Enter age: ")

    if not age.isdigit():
        print("Age must be a number!")
        return
    
    gender = input("Enter gender: ")

    if gender not in ["Male", "Female"]:
        print("Gender must be Male or Female!")
        return
    phone = input("Enter phone: ")

    if not phone.isdigit():
        print("Phone must contain numbers only!")
        return

    patients = load_patients()

    for patient in patients:
        if patient["patient_id"] == patient_id:
            print("Patient ID already exists!")
            return

    new_patient = {
        "patient_id": patient_id,
        "name": name,
        "age": age,
        "gender": gender,
        "phone": phone
    }

    patients.append(new_patient)
    save_patients(patients)

    print("Patient added successfully!")


def view_patients():
    print("\n===== PATIENT LIST =====")

    patients = load_patients()

    if not patients:
        print("No patients found.")
        return

    for patient in patients:
        print("----------------------------")
        print("ID:", patient["patient_id"])
        print("Name:", patient["name"])
        print("Age:", patient["age"])
        print("Gender:", patient["gender"])
        print("Phone:", patient["phone"])


def search_patient():
    print("\n===== SEARCH PATIENT =====")

    search_id = input("Enter patient ID: ")

    patients = load_patients()

    for patient in patients:
        if patient["patient_id"] == search_id:
            print("\nPatient found!")
            print("ID:", patient["patient_id"])
            print("Name:", patient["name"])
            print("Age:", patient["age"])
            print("Gender:", patient["gender"])
            print("Phone:", patient["phone"])
            return

    raise PatientNotFoundError("Patient not found.")

def update_patient():
    print("\n===== UPDATE PATIENT =====")

    patient_id = input("Enter patient ID: ")

    patients = load_patients()

    for patient in patients:
        if patient["patient_id"] == patient_id:
            patient["name"] = input("Enter new name: ")
            patient["age"] = input("Enter new age: ")
            patient["gender"] = input("Enter new gender: ")
            patient["phone"] = input("Enter new phone: ")

            save_patients(patients)

            print("Patient updated successfully!")
            return

    raise PatientNotFoundError("Patient not found.")

def delete_patient():
    print("\n===== DELETE PATIENT =====")

    patient_id = input("Enter patient ID: ")

    patients = load_patients()

    for patient in patients:
        if patient["patient_id"] == patient_id:
            patients.remove(patient)
            save_patients(patients)

            print("Patient deleted successfully!")
            return

    raise PatientNotFoundError("Patient not found.")
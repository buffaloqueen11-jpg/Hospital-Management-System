from auth import register, login

from patient_service import (
    add_patient,
    view_patients,
    search_patient,
    update_patient,
    delete_patient
)

from doctor_service import (
    add_doctor,
    view_doctors,
    search_doctor,
    update_doctor,
    delete_doctor
)

from appointment_service import (
    add_appointment,
    view_appointments,
    search_appointment,
    update_appointment,
    delete_appointment
)

from payment_service import (
    add_payment,
    view_payments,
    search_payment,
    update_payment,
    delete_payment
)

from report_service import show_report

from checkin_service import check_in, check_out

from medical_record_service import (
    add_medical_record,
    view_medical_records,
    update_medical_record,
    delete_medical_record
)

from prescription_service import (
    add_prescription,
    view_prescriptions,
    update_prescription,
    delete_prescription
)

from appointment_history_service import view_appointment_history

from exceptions import (
    PatientNotFoundError,
    DoctorNotFoundError,
    AppointmentNotFoundError,
    MedicalRecordNotFoundError,
    PrescriptionNotFoundError,
    PaymentNotFoundError
)

def main():
    while True:
        print("\n==============================")
        print("  HOSPITAL MANAGEMENT SYSTEM")
        print("==============================")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            register()

        elif choice == "2":
            user = login()

            if user:
                if user["role"] == "admin":
                    while True:
                        print("\n===== ADMIN MENU =====")
                        print("1. Patient Management")
                        print("2. Doctor Management")
                        print("3. Appointment Management")
                        print("4. Payment Management")
                        print("5. Check-in / Check-out")
                        print("6. Medical Records")
                        print("7. Prescriptions")
                        print("8. Appointment History")
                        print("9. Reports")
                        print("10. Logout")

                        admin_choice = input("Choose an option: ")

                        if admin_choice == "1":
                            while True:
                                print("\n===== PATIENT MANAGEMENT =====")
                                print("1. Add Patient")
                                print("2. View Patients")
                                print("3. Search Patient")
                                print("4. Update Patient")
                                print("5. Delete Patient")
                                print("6. Back")

                                patient_choice = input("Choose an option: ")

                                if patient_choice == "1":
                                    add_patient()

                                elif patient_choice == "2":
                                    view_patients()

                                elif patient_choice == "3":
                                    search_patient()

                                elif patient_choice == "4":
                                    update_patient()

                                elif patient_choice == "5":
                                    try:
                                        delete_patient()
                                    except PatientNotFoundError as e:
                                        print(e)          

                                elif patient_choice == "6":
                                    break

                                else:
                                    print("Invalid choice!")

                        elif admin_choice == "2":
                            while True:
                                print("\n===== DOCTOR MANAGEMENT =====")
                                print("1. Add Doctor")
                                print("2. View Doctors")
                                print("3. Search Doctor")
                                print("4. Update Doctor")
                                print("5. Delete Doctor")
                                print("6. Back")

                                doctor_choice = input("Choose an option: ")

                                if doctor_choice == "1":
                                    add_doctor()

                                elif doctor_choice == "2":
                                    view_doctors()

                                elif doctor_choice == "3":
                                    search_doctor()

                                elif doctor_choice == "4":
                                    update_doctor()

                                elif doctor_choice == "5":
                                    try:
                                        delete_doctor()
                                    except DoctorNotFoundError as e:
                                        print(e)

                                elif doctor_choice == "6":
                                    break

                                else:
                                    print("Invalid choice!")

                        elif admin_choice == "3":
                            while True:
                                print("\n===== APPOINTMENT MANAGEMENT =====")
                                print("1. Add Appointment")
                                print("2. View Appointments")
                                print("3. Search Appointment")
                                print("4. Update Appointment")
                                print("5. Delete Appointment")
                                print("6. Back")

                                appointment_choice = input("Choose an option: ")

                                if appointment_choice == "1":
                                    add_appointment()

                                elif appointment_choice == "2":
                                    view_appointments()

                                elif appointment_choice == "3":
                                    search_appointment()

                                elif appointment_choice == "4":
                                    update_appointment()

                                elif appointment_choice == "5":
                                    try:
                                        delete_appointment()
                                    except AppointmentNotFoundError as e:
                                        print(e)
                                elif appointment_choice == "6":
                                    break

                                else:
                                    print("Invalid choice!")

                        elif admin_choice == "4":
                            while True:
                                print("\n===== PAYMENT MANAGEMENT =====")
                                print("1. Add Payment")
                                print("2. View Payments")
                                print("3. Search Payment")
                                print("4. Update Payment")
                                print("5. Delete Payment")
                                print("6. Back")

                                payment_choice = input("Choose an option: ")

                                if payment_choice == "1":
                                    add_payment()

                                elif payment_choice == "2":
                                    view_payments()

                                elif payment_choice == "3":
                                    try:
                                        search_payment()
                                    except PaymentNotFoundError as e:
                                        print(e)

                                elif payment_choice == "4":
                                    try:
                                        update_payment()
                                    except PaymentNotFoundError as e:
                                        print(e)

                                elif payment_choice == "5":
                                    try:
                                        delete_payment()
                                    except PaymentNotFoundError as e:
                                        print(e)

                                elif payment_choice == "6":
                                    break

                                else:
                                    print("Invalid choice!") 

                        elif admin_choice == "5":
                           while True:
                                print("\n===== CHECK-IN / CHECK-OUT =====")
                                print("1. Check-in")
                                print("2. Check-out")
                                print("3. Back")

                                check_choice = input("Choose an option: ")

                                if check_choice == "1":
                                    try:
                                        check_in()
                                    except AppointmentNotFoundError as e:
                                        print(e)
                                
                                elif check_choice == "2":
                                        try:
                                            check_out()
                                        except AppointmentNotFoundError as e:
                                            print(e)      

                                elif check_choice == "3":
                                   break

                                else:
                                   print("Invalid choice!")     

                        elif admin_choice == "6":
                            while True:
                                print("\n===== MEDICAL RECORDS =====")
                                print("1. Add Medical Record")
                                print("2. View Medical Records")
                                print("3. Update Medical Record")
                                print("4. Delete Medical Record")
                                print("5. Back")

                                record_choice = input("Choose an option: ")

                                if record_choice == "1":
                                    add_medical_record()

                                elif record_choice == "2":
                                    view_medical_records()

                                elif record_choice == "3":
                                    update_medical_record()

                                elif record_choice == "4":
                                    try:
                                        delete_medical_record()
                                    except MedicalRecordNotFoundError as e:
                                        print(e)                            

                                elif record_choice == "5":
                                    break

                                else:
                                    print("Invalid choice!")

                        elif admin_choice == "7":
                            while True:
                                print("\n===== PRESCRIPTIONS =====")
                                print("1. Add Prescription")
                                print("2. View Prescriptions")
                                print("3. Update Prescription")
                                print("4. Delete Prescription")
                                print("5. Back")

                                prescription_choice = input("Choose an option: ")

                                if prescription_choice == "1":
                                    add_prescription()

                                elif prescription_choice == "2":
                                    view_prescriptions()

                                elif prescription_choice == "3":
                                    
                                    try:
                                        update_prescription()
                                    except PrescriptionNotFoundError as e:
                                        print(e)           

                                elif prescription_choice == "4":
                                    try:
                                        delete_prescription()
                                    except PrescriptionNotFoundError as e:
                                        print(e)                                       
                     
                                elif prescription_choice == "5":
                                    break

                                else:
                                    print("Invalid choice!")  

                        elif admin_choice == "8":
                            view_appointment_history()

                        elif admin_choice == "9":
                            show_report()

                        elif admin_choice == "10":
                           print("Logout successful!")
                           break
                elif user["role"] == "doctor":
                   while True:
                        print("===== DOCTOR MENU =====")
                        print("1. View Patients")
                        print("2. View Appointments")
                        print("3. View Medical Records")
                        print("4. View Prescriptions")
                        print("5. Logout")
                        doctor_choice = input("Choose an option: ")

                        if doctor_choice == "1":
                            view_patients()

                        elif doctor_choice == "2":
                            view_appointments()

                        elif doctor_choice == "3":
                            view_medical_records()

                        elif doctor_choice == "4":
                            view_prescriptions()

                        elif doctor_choice == "5":
                            print("Logout successfully!")
                            break

                        else:
                            print("Invalid choice!")

                elif user["role"] == "receptionist":
                    while True:
                            print("\n===== RECEPTIONIST MENU =====")
                            print("1. Patient Management")
                            print("2. Appointment Management")
                            print("3. Payment Management")
                            print("4. Logout")

                            receptionist_choice = input("Choose an option: ")

                            if receptionist_choice == "1":
                                while True:
                                    print("\n===== PATIENT MANAGEMENT =====")
                                    print("1. Add Patient")
                                    print("2. View Patients")
                                    print("3. Search Patient")
                                    print("4. Update Patient")
                                    print("5. Delete Patient")
                                    print("6. Back")

                                    patient_choice = input("Choose an option: ")

                                    if patient_choice == "1":
                                        add_patient()

                                    elif patient_choice == "2":
                                        view_patients()

                                    elif patient_choice == "3":
                                        search_patient()

                                    elif patient_choice == "4":
                                        update_patient()

                                    elif patient_choice == "5":
                                        try:
                                            delete_patient()
                                        except PatientNotFoundError as e:
                                            print(e)
                                    
                                    elif patient_choice == "6":
                                        break
                                    else:
                                        print("Invalid choice!")
 
                            elif receptionist_choice == "2":
                                while True:
                                    print("\n===== APPOINTMENT MANAGEMENT =====")
                                    print("1. Add Appointment")
                                    print("2. View Appointments")
                                    print("3. Search Appointment")
                                    print("4. Update Appointment")
                                    print("5. Delete Appointment")
                                    print("6. Back")

                                    appointment_choice = input("Choose an option: ")

                                    if appointment_choice == "1":
                                        add_appointment()

                                    elif appointment_choice == "2":
                                        view_appointments()

                                    elif appointment_choice == "3":
                                        try:
                                            search_appointment()
                                        except AppointmentNotFoundError as e:
                                            print(e)

                                    elif appointment_choice == "4":
                                        try:
                                            update_appointment()
                                        except AppointmentNotFoundError as e:
                                            print(e)

                                    elif appointment_choice == "5":
                                        try:
                                            delete_appointment()
                                        except AppointmentNotFoundError as e:
                                            print(e)

                                    elif appointment_choice == "6":
                                        break

                                    else:
                                        print("Invalid choice!")

                            elif receptionist_choice == "3":
                                while True:
                                    print("\n===== PAYMENT MANAGEMENT =====")
                                    print("1. Add Payment")
                                    print("2. View Payments")
                                    print("3. Search Payment")
                                    print("4. Update Payment")
                                    print("5. Delete Payment")
                                    print("6. Back")

                                    payment_choice = input("Choose an option: ")

                                    if payment_choice == "1":
                                        add_payment()

                                    elif payment_choice == "2":
                                        view_payments()

                                    elif payment_choice == "3":
                                        try:
                                            search_payment()
                                        except PaymentNotFoundError as e:
                                            print(e)

                                    elif payment_choice == "4":
                                        try: 
                                            update_payment()
                                        except PaymentNotFoundError as e: 
                                            print(e)

                                    elif payment_choice == "5":
                                        try:
                                            delete_payment()
                                        except PaymentNotFoundError as e:
                                            print(e)

                                    elif payment_choice == "6":
                                        break

                                    else:
                                        print("Invalid choice!")

                            elif receptionist_choice == "4":
                                print("Logout successful!")
                                break

        elif choice == "3":
            print("Thank you for using Hospital Management System.")
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()


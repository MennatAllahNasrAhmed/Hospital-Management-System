from Hospital_Magement_System.hospital import Hospital
from Hospital_Magement_System.department import Department
from Hospital_Magement_System.patient import Patient
from Hospital_Magement_System.staff import Staff

def display_menu():
    print("\n" + "="*35)
    print("  Hospital Management System  ")
    print("="*35)
    print("1. Add Department")
    print("2. Add Patient to Department")
    print("3. Add Staff to Department")
    print("4. View All Departments")
    print("5. View Patient Record")
    print("6. View Staff Information")
    print("7. Exit")
    print("="*35)

def main():
    hospital_name = input("Enter Hospital Name: ")
    hospital_loc = input("Enter Hospital Location: ")
    hospital = Hospital(hospital_name, hospital_loc)

    while True:
        display_menu()
        choice = input("Select an option (1-7): ").strip()

        if choice == '1':
            dept_name = input("Enter Department Name: ")
            dept = Department(dept_name)
            hospital.add_department(dept)

        elif choice == '2':
            dept_name = input("Enter Department Name to add patient into: ")
            dept = hospital.find_department(dept_name)
            
            if dept:
                p_name = input("Enter Patient Name: ")
                p_age = int(input("Enter Patient Age: "))
                p_record = input("Enter Medical Record: ")

                patient = Patient(p_name, p_age, p_record)
                dept.add_patient(patient)
            else:
                print(f"Department '{dept_name}' not found!")

        elif choice == '3':
            dept_name = input("Enter Department Name to add staff into: ")
            dept = hospital.find_department(dept_name)
            
            if dept:
                s_name = input("Enter Staff Name: ")
                s_age = int(input("Enter Staff Age: "))
                s_pos = input("Enter Position: ")

                staff = Staff(s_name, s_age, s_pos)
                dept.add_staff(staff)
            else:
                print(f"Department '{dept_name}' not found!")

        elif choice == '4':
            depts = hospital.view_departments()
            if depts:
                print("\nHospital Departments:")
                for d in depts:
                    print(f"- {d}")
            else:
                print("No departments found.")

        elif choice == '5':
            if not hospital.departments:
                print("No departments found.")
                continue

            for dept in hospital.departments:
                print(f"\nDepartment: {dept.name}")
                if not dept.patients:
                    print("  No patients found.")
                for patient in dept.patients:
                    print(f"  - {patient.view_record()}")

        elif choice == '6':
            if not hospital.departments:
                print("No departments found.")
                continue

            for dept in hospital.departments:
                print(f"\nDepartment: {dept.name}")
                if not dept.staff:
                    print("  No staff found.")
                for staff in dept.staff:
                    print(f"  - {staff.view_info()}")

        elif choice == '7':
            print("\nExiting System. Goodbye!")
            break

        else:
            print("\nInvalid choice! Please select 1 to 7.")

if __name__ == "__main__":
    main()
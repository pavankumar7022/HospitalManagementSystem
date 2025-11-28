
# Simple Hospital Management System
# ------------------------------

patients = []
doctors = []
appointments = []

# Add Patient
def add_patient():
    pid = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    age = input("Enter Age: ")
    problem = input("Enter Problem: ")

    patient = {"id": pid, "name": name, "age": age, "problem": problem}
    patients.append(patient)
    print("Patient added successfully!\n")

# Add Doctor
def add_doctor():
    did = input("Enter Doctor ID: ")
    name = input("Enter Doctor Name: ")
    spec = input("Enter Specialization: ")

    doctor = {"id": did, "name": name, "spec": spec}
    doctors.append(doctor)
    print("Doctor added successfully!\n")

# Book Appointment
def book_appointment():
    pid = input("Enter Patient ID: ")
    did = input("Enter Doctor ID: ")
    date = input("Enter Appointment Date (DD-MM-YYYY): ")

    appointment = {"patient_id": pid, "doctor_id": did, "date": date}
    appointments.append(appointment)
    print("Appointment booked successfully!\n")

# View all Patients
def view_patients():
    print("\n--- All Patients ---")
    for p in patients:
        print(p)
    print()

# View all Doctors
def view_doctors():
    print("\n--- All Doctors ---")
    for d in doctors:
        print(d)
    print()

# View all Appointments
def view_appointments():
    print("\n--- All Appointments ---")
    for a in appointments:
        print(a)
    print()

# MENU
while True:
    print("""
===============================
   Hospital Management System
===============================
1. Add Patient
2. Add Doctor
3. Book Appointment
4. View Patients
5. View Doctors
6. View Appointments
7. Exit
""")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_patient()
    elif choice == "2":
        add_doctor()
    elif choice == "3":
        book_appointment()
    elif choice == "4":
        view_patients()
    elif choice == "5":
        view_doctors()
    elif choice == "6":
        view_appointments()
    elif choice == "7":
        print("Thank you!")
        break
    else:

        print("Invalid choice! Try again.\n")

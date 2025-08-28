
# Base Class: Person
# -------------------------
class Person:
    def __init__(self, name, age, gender):
        self.name = name          # Attribute for person's name
        self.age = age            # Attribute for age
        self.gender = gender      # Attribute for gender

    def display_details(self):
        """Displays basic details of a person"""
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")


# -------------------------
# Derived Class: Patient
# Inherits from Person
# -------------------------
class Patient(Person):
    def __init__(self, name, age, gender, patient_id, disease):
        # Call parent constructor
        super().__init__(name, age, gender)
        self.patient_id = patient_id    # Unique ID for patient
        self.disease = disease          # Disease diagnosed

    # Method overriding (Polymorphism)
    def display_details(self):
        """Displays patient details"""
        super().display_details()   # Call parent method
        print(f"Patient ID: {self.patient_id}, Disease: {self.disease}")


# -------------------------
# Derived Class: Doctor
# Inherits from Person
# -------------------------
class Doctor(Person):
    def __init__(self, name, age, gender, specialization):
        # Call parent constructor
        super().__init__(name, age, gender)
        self.specialization = specialization  # Doctor's specialization

    # Method overriding
    def display_details(self):
        """Displays doctor details"""
        super().display_details()
        print(f"Specialization: {self.specialization}")


# -------------------------
# Hospital Class
# Manages patients & doctors
# -------------------------
class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = []   # List to store Patient objects
        self.doctors = []    # List to store Doctor objects

    def add_patient(self, patient):
        """Add a patient to the hospital"""
        self.patients.append(patient)
        print(f"✅ Patient {patient.name} added successfully!")

    def add_doctor(self, doctor):
        """Add a doctor to the hospital"""
        self.doctors.append(doctor)
        print(f"✅ Doctor {doctor.name} added successfully!")

    def show_patients(self):
        """Display all patients"""
        if not self.patients:
            print("⚠ No patients found.")
        else:
            print("\n--- Patient List ---")
            for patient in self.patients:
                patient.display_details()
                print("-" * 20)

    def show_doctors(self):
        """Display all doctors"""
        if not self.doctors:
            print("⚠ No doctors found.")
        else:
            print("\n--- Doctor List ---")
            for doctor in self.doctors:
                doctor.display_details()
                print("-" * 20)


# -------------------------
# Main Program (Menu Driven)
# -------------------------
def main():
    hospital = Hospital("City Care Hospital")

    while True:
        # Menu loop
        print("\n==== Hospital Management Menu ====")
        print("1. Add Patient")
        print("2. Add Doctor")
        print("3. Show Patients")
        print("4. Show Doctors")
        print("5. Exit")

        choice = input("Enter your choice: ")

        # Add Patient
        if choice == "1":
            name = input("Enter patient name: ")
            age = int(input("Enter patient age: "))
            gender = input("Enter gender: ")
            patient_id = input("Enter patient ID: ")
            disease = input("Enter disease: ")
            p = Patient(name, age, gender, patient_id, disease)
            hospital.add_patient(p)

        # Add Doctor
        elif choice == "2":
            name = input("Enter doctor name: ")
            age = int(input("Enter doctor age: "))
            gender = input("Enter gender: ")
            specialization = input("Enter specialization: ")
            d = Doctor(name, age, gender, specialization)
            hospital.add_doctor(d)

        # Show Patients
        elif choice == "3":
            hospital.show_patients()

        # Show Doctors
        elif choice == "4":
            hospital.show_doctors()

        # Exit Program
        elif choice == "5":
            print("🚪 Exiting... Thank you for using the system!")
            break

        else:
            print("❌ Invalid choice! Please try again.")


# -------------------------
# Run Program
# -------------------------
if __name__ == "__main__":
    main()








while True:
    students = {}

    print("Student Management System")
    while True:
        menu_name = input("\n1. Add student\n2. Find student\n3. delete\n4. Exit\nChoose: ")

        match menu_name:

            case "1":
                id = input("Kode meli: ")
                name = input("Esmeto bego: ")
                age = int(input("Senet: "))
                score = float(input("Nomrat: "))
                address = input("Adreseto vared kon: ")

                students[id] = {
                    "name": name,
                    "age": age,
                    "score": score,
                    "address": address
                }

                print("Student added successfully!")
                print(students)
                break

            case "2":
                id = input("Kode meli ro vared kon: ")

                student = students.get(id)

                if student:
                    print("\nStudent found:")
                    print("Name:", student["name"])
                    print("Age:", student["age"])
                    print("Score:", student["score"])
                    print("Address:", student["address"])
                    break
                else:
                    print("Student not found!")
                    break
            
            case "3":
                id = input("Kode meli ro bazan: ")
                student = students.pop(id)
                print ("student delete")
                break
            
            case "4":
                print("bye bye .")
                break
    break



# if , else
# loop 
# list 
# tuple
# dict 
#match case 
# str 
                
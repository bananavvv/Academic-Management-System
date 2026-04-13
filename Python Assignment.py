#---SYSTEM MAIN MENU---
def __main__(file_paths): #dictionary of file paths as the parameter instead of individual variables
    # encapsulate the function (before was usigng global variables)
    # file paths now defined within the block so no global variables
    while True:
        print("\n----Welcome to the Academic Management System----")
        print("Please choose your user access below:")
        print("1. Admin\n2. Student\n3. Teacher\n4. Staff\n5. Exit")
        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid Input. Please enter a number between 1 and 5.")
            continue
        if choice == 1:
            admin_menu(file_paths)
        elif choice == 2:
            student_menu(file_paths) # Pass file_paths dictionary
        elif choice == 3:
            teacher_menu(file_paths) # Pass file_paths dictionary
        elif choice == 4:
            staff_menu(file_paths)
            print("Staff Menu")
        elif choice == 5:
            print("Exiting the Academic Management System.")
            break  # Exits the main menu loop
        else:
            print("Invalid choice in main menu.  Please try again.")

#---ADMIN LOGIN---
def admin_login(file_paths, admin_username):
    #Logs in an admin user.
    admin_username = input("Enter username: ")
    admin_password = input("Enter password: ")
    USER_FILE = file_paths["USER_FILE"]
    try:  # Admin id, username, and password are stored in users.txt
        with open(USER_FILE, "r") as file:  # opens the file in read mode to see if it matches
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    stored_admin_username, stored_admin_password, stored_admin_role = parts
                    if (admin_username == "admin" and
                            admin_password == "admin123" and
                            stored_admin_username == "admin" and
                            stored_admin_password == "admin123"): #Fixed: it checks from users.txt and if its == admin
                        print("Login successful!")
                        return admin_username  # Return the username on successful login.
                        # Return the stored_admin_username instead of admin_username to handle possible variations in capitalization or spacing.
            print("Login Failed! Invalid Credentials.")  # Moved outside the loop
            return None
    except FileNotFoundError:
        print("No user accounts found.")
        return None
    except Exception as e:
        print(f'An Error Occurred, Please Try Again: {e}')  # file cant open due to incorrect format

#-----------------------------------------------------------------------------------------------------------------------

#----USER ACCOUNT CREATION----
def create_user_account(file_paths, admin_username):
    #Creates a user account based on the selected role and saves data to files.
    if admin_username is None:
        print("You must be logged in to update user information.")
        return
    USER_FILE = file_paths["USER_FILE"]
    STUDENT_FILE = file_paths["STUDENT_FILE"]
    TEACHER_FILE = file_paths["TEACHER_FILE"]
    STAFF_FILE = file_paths["STAFF_FILE"]
    while True:
        print("\n---User Account Creation---")
        print("---Select user role for account creation---")
        print("1. Student")
        print("2. Teacher")
        print("3. Staff")
        print("4. Exit")
        try:
            admin_choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid Input. Please enter a number between 1 and 4.")
            continue
        if admin_choice not in [1, 2, 3, 4]:
            print("Invalid Input. Please enter a number between 1 and 4.")
            continue
        username = input("Enter username: ")
        password = input("Enter password: ")
        role_code = 0
        role_code = ""
        if admin_choice == 1:  # Student
            student_id = generate_student_id_admin(file_paths)
            role_code = 1
            role_code = "student"
            try:
                with open(STUDENT_FILE, "a") as file:
                    file.write(f'{student_id},{username},{password},,,_\n')
                with open(USER_FILE, "a") as file:
                    file.write(f'{username},{password},{role_code}\n')
                print("Student account successfully created!")
                break # Exit the loop after successful creation
            except Exception as e:
                print(f'An Error Occurred creating student account: {e}')
                continue #restart account creation process if error occurs
        elif admin_choice == 2:  # Teacher
            teacher_id = generate_teacher_id_admin(file_paths)
            role_code = 2
            role_code = "teacher"
            try:
                with open(TEACHER_FILE, "a") as file:
                    file.write(f'{teacher_id},{username},{password}\n')
                with open(USER_FILE, "a") as file:
                    file.write(f'{username},{password},{role_code}\n')
                print("Teacher account successfully created!")
                break # Exit the loop after successful creation
            except Exception as e:
                print(f'An Error Occurred creating teacher account: {e}')
                continue #restart account creation process if error occurs
        elif admin_choice == 3:  # Staff
            staff_id = generate_staff_id_admin(file_paths)
            role_code = 3
            role_code = "staff"
            try:
                with open(STAFF_FILE, "a") as file:
                    file.write(f'{staff_id},{username},{password}\n')
                with open(USER_FILE, "a") as file:
                    file.write(f'{username},{password},{role_code}\n')
                print("Staff account successfully created!")
                break # Exit the loop after successful creation
            except Exception as e:
                print(f'An Error Occurred creating staff account: {e}')
                continue #restart account creation process if error occurs

        elif admin_choice == 4: #Exit
            print("Returning back to Admin Menu")
            break

#-----------------------------------------------------------------------------------------------------------------------

#----GENERATING STUDENT ID----
def generate_student_id_admin(file_paths):
    #Generates a unique student ID (S01, S02, etc.).
    STUDENT_FILE = file_paths["STUDENT_FILE"]
    try:
        with open(STUDENT_FILE, "r") as file:
            lines = file.readlines()
            if not lines:
                return "S01"  # Start with S01 if the file is empty
            last_line = lines[-1].strip()
            last_student_id = last_line.split(",")[0]
            last_id_number = int(last_student_id[1:])
            new_id_number = last_id_number + 1
            new_student_id = f"S{new_id_number:02}"
            return new_student_id
    except FileNotFoundError:
        return "S01"  # Start with S01 if the file doesn't exist
    except Exception:
        return "S01"  # Start with S01 in case of error

#-----------------------------------------------------------------------------------------------------------------------

#----GENERATE TEACHER ID----
def generate_teacher_id_admin(file_paths):
    #Generates a unique teacher ID (T01, T02, etc.).
    TEACHER_FILE = file_paths["TEACHER_FILE"]
    try:
        with open(TEACHER_FILE, "r") as file:
            lines = file.readlines()
            if not lines:
                return "T01"  # Start with T01 if the file is empty

            last_line = lines[-1].strip()
            last_teacher_id = last_line.split(",")[0]
            last_id_number = int(last_teacher_id[1:])
            new_id_number = last_id_number + 1
            new_teacher_id = f"T{new_id_number:02}"
            return new_teacher_id
    except FileNotFoundError:
        return "T01"  # Start with T01 if the file doesn't exist
    except Exception:
        return "T01"  # Start with T01 in case of error

#-----------------------------------------------------------------------------------------------------------------------

# ----GENERATE STAFF ID----
def generate_staff_id_admin(file_paths):
#Generates a unique staff ID (ST01, ST02, etc.).
    STAFF_FILE = file_paths["STAFF_FILE"]
    try:
        with open(STAFF_FILE, "r") as file:
            lines = file.readlines()
            if not lines:
                return "ST01"  # Start with ST01 if the file is empty

            last_line = lines[-1].strip()
            last_staff_id = last_line.split(",")[0]
            last_id_number = int(last_staff_id[2:])  # Changed to [2:] to account for "ST"
            new_id_number = last_id_number + 1
            new_staff_id = f"ST{new_id_number:02}"
            return new_staff_id
    except FileNotFoundError:
        return "ST01"  # Start with ST01 if the file doesn't exist
    except Exception:
        return "ST01"  # Start with ST01 in case of error
#-----------------------------------------------------------------------------------------------------------------------

# ----DELETING USER ACCOUNTS----
def delete_user_account(file_paths, admin_username):
    if admin_username is None:
        print("You must be logged in to update user information.")
        return

    USER_FILE = file_paths["USER_FILE"]
    STUDENT_FILE = file_paths["STUDENT_FILE"]
    STAFF_FILE = file_paths["STAFF_FILE"]
    TEACHER_FILE = file_paths["TEACHER_FILE"]

    while True:
        print("\n---User Account Deletion---")
        print("---Select user role for account deletion---")
        print("1. Student")
        print("2. Teacher")
        print("3. Staff")
        print("4. Exit")
        try:
            admin_choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid Input. Please enter a number between 1 and 4.")
            continue
        if admin_choice not in [1, 2, 3, 4]:
            print("Invalid Input. Please enter a number between 1 and 4.")
            continue

        if admin_choice == 1:

            print("Delete Student Account.")

            student_username = input("Enter student account username that you would like to delete: ")

            try:
                with open(STUDENT_FILE, "r") as file:
                    students = file.readlines()
                with open(STUDENT_FILE, "w") as file:
                    found = False
                    for student in students:
                        if student.split(",")[1] != student_username:  # Compare username as student identifier
                            file.write(student)  # Rewrite the file except for the deleted username
                        else:
                            found = True  # shows if the user account is valid
                    if not found:
                        print("student username could not be verified with what's on the user file.")
                    print(
                        f"Student '{student_username}' removed successfully!" if found else f"Student '{student_username}' not found.")
            except FileNotFoundError:
                print("Student File not found!")
            except Exception as e:
                print(f"Student file not found: {e}")

            # Remove user from the user file

            try:
                with open(USER_FILE, "r") as file:
                    users = file.readlines()
                with open(USER_FILE, "w") as file:
                    found = False  # verifies if the user to be deleted actually exists
                    for user in users:
                        if user.split(",")[0] != student_username:  # verifies with username
                            file.write(user)  # rewrites the documents
                        else:
                            found = True  # shows it did work
                    if not found:
                        print("the username is not what the Admin specified. Deletion cancelled!")
                    print(
                        f"User '{student_username}' removed successfully!" if found else f"User '{student_username}' not found.")
                break
            except FileNotFoundError:
                print("User file does not exist!")
            except Exception as e:
                print(f"An error occurred while deleting the file {e}")
        # Delete the user account from each file

        if admin_choice == 2:
            print("Delete Teacher Account.")

            teacher_username = input("Enter teacher account username that you would like to delete: ")

            try:
                with open(TEACHER_FILE, "r") as file:
                    teachers = file.readlines()
                with open(TEACHER_FILE, "w") as file:
                    found = False
                    for teacher in teachers:
                        if teacher.split(",")[1] != teacher_username:  # Compare username as teacher identifier
                            file.write(teacher)  # Rewrite the file except for the deleted username
                        else:
                            found = True  # shows if the user account is valid
                    if not found:
                        print("Teacher username could not be verified with what's on the user file.")
                    print(
                        f"Teacher '{teacher_username}' removed successfully!" if found else f"Teacher '{teacher_username}' not found.")
            except FileNotFoundError:
                print("Teacher File not found!")
            except Exception as e:
                print(f"Teacher file not found: {e}")

            # Remove user from the user file
            try:
                with open(USER_FILE, "r") as file:
                    users = file.readlines()
                with open(USER_FILE, "w") as file:
                    found = False  # verifies if the user to be deleted actually exists
                    for user in users:
                        if user.split(",")[0] != teacher_username:  # verifies with username
                            file.write(user)  # rewrites the documents
                        else:
                            found = True  # shows it did work
                    if not found:
                        print("The username is not what the Admin specified. Deletion cancelled!")
                    print(
                        f"User '{teacher_username}' removed successfully!" if found else f"User '{teacher_username}' not found.")
                break
            except FileNotFoundError:
                print("User file does not exist!")
            except Exception as e:
                print(f"An error occurred while deleting the file {e}")

        if admin_choice == 3:
            print("Delete Staff Account.")

            staff_username = input("Enter staff account username that you would like to delete: ")

            try:
                with open(STAFF_FILE, "r") as file:
                    staffs = file.readlines()
                with open(STAFF_FILE, "w") as file:
                    found = False
                    for staff in staffs:
                        if staff.split(",")[1] != staff_username:  # Compare username as staff identifier
                            file.write(staff)  # Rewrite the file except for the deleted username
                        else:
                            found = True  # shows if the user account is valid
                    if not found:
                        print("Staff username could not be verified with what's on the user file.")
                    print(
                        f"Staff '{staff_username}' removed successfully!" if found else f"Staff '{staff_username}' not found.")
            except FileNotFoundError:
                print("Staff File not found!")
            except Exception as e:
                print(f"Staff file not found: {e}")

            # Remove user from the user file
            try:
                with open(USER_FILE, "r") as file:
                    users = file.readlines()
                with open(USER_FILE, "w") as file:
                    found = False  # verifies if the user to be deleted actually exists
                    for user in users:
                        if user.split(",")[0] != staff_username:  # verifies with username
                            file.write(user)  # rewrites the documents
                        else:
                            found = True  # shows it did work
                    if not found:
                        print("The username is not what the Admin specified. Deletion cancelled!")
                    print(
                        f"User '{staff_username}' removed successfully!" if found else f"User '{staff_username}' not found.")
                break
            except FileNotFoundError:
                print("User file does not exist!")
            except Exception as e:
                print(f"An error occurred while deleting the file {e}")

        elif admin_choice == 4: #Exit
            print("Returning back to Admin Menu")
            break

#-----------------------------------------------------------------------------------------------------------------------

#----EDITING USER INFO----
def edit_user_info_admin(file_paths, admin_username):
    if admin_username is None:
        print("You must be logged in to update user information.")
        return
    USER_FILE = file_paths["USER_FILE"]
    STUDENT_FILE = file_paths["STUDENT_FILE"]
    TEACHER_FILE = file_paths["TEACHER_FILE"]
    STAFF_FILE = file_paths["STAFF_FILE"]

    while True:
        print("\n----Update User Information----")
        print("Select the User type you would like to update:")
        print("1. Student")
        print("2. Teacher")
        print("3. Staff")
        print("4. Exit")

        try:
            admin_choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid Input. Please enter a number between 1 and 4.")
            continue

        if admin_choice not in [1, 2, 3, 4]:
            print("Invalid Input. Please enter a number between 1 and 4.")
            continue
        file_to_update = None
        id_field = None  # Field to search for the username (differs by file)
        if admin_choice == 1:
            print("---Updating Student File---")
            file_to_update = STUDENT_FILE
            id_field = 1  # Username is the second field (index 1)
        elif admin_choice == 2:
            print("---Updating Teacher File---")
            file_to_update = TEACHER_FILE
            id_field = 1  # Assuming username is the second field
        elif admin_choice == 3:
            print("---Updating Staff File---")
            file_to_update = STAFF_FILE
            id_field = 1  # Assuming username is the second field
        elif admin_choice == 4: #Exit
            print("Returning back to Admin Menu")
            break

        if file_to_update is None:
            print("Invalid choice. No file selected for update.")
            continue
        old_username = input("Enter the username of the user to update: ")
        new_username = input("Enter the new username (leave blank to keep the same): ")
        new_password = input("Enter the new password (leave blank to keep the same): ")
        try:
            # --- Update the specific file (student, teacher, or staff) ---
            with open(file_to_update, "r") as file:
                lines = file.readlines()
            updated_lines = []
            user_found = False
            for line in lines:
                parts = line.strip().split(",")
                if len(parts) > id_field and parts[id_field] == old_username:  # Check if the username matches
                    user_found = True
                    if new_username:
                        parts[id_field] = new_username # Update the username in the specific field
                    if new_password:
                        parts[2] = new_password  # Update the password
                    updated_line = ",".join(parts) + "\n"
                    updated_lines.append(updated_line)
                    # Optionally, update other fields here (e.g., name, contact info) based on user input

                else:
                    updated_lines.append(line)  # Keep the original line
            if not user_found:
                print(f"User with username '{old_username}' not found in {file_to_update}")
                continue  # Restart the loop if the user isn't found
            with open(file_to_update, "w") as file:
                file.writelines(updated_lines)
            # --- Update the USER_FILE ---
            with open(USER_FILE, "r") as file:
                user_lines = file.readlines()
            updated_user_lines = []
            user_found = False
            for line in user_lines:
                parts = line.strip().split(",")
                if len(parts) == 3 and parts[0] == old_username:  # Only process lines with username, password, role
                    user_found = True
                    if new_username:
                        parts[0] = new_username
                    if new_password:
                        parts[1] = new_password  # Update the password
                    updated_line = ",".join(parts) + "\n"
                    updated_user_lines.append(updated_line)
                else:
                    updated_user_lines.append(line)
            if not user_found:
                print(f"User with username '{old_username}' not found in {USER_FILE}")
                continue

            with open(USER_FILE, "w") as file:
                file.writelines(updated_user_lines)

            print(f"Files '{USER_FILE}' and '{file_to_update}' updated successfully!")
            break  # Exit the loop after successful update

        except FileNotFoundError:
            print(f"Error: File '{file_to_update}' or '{USER_FILE}' not found.")
            continue
        except Exception as e:
            print(f"An error occurred: {e}")
            continue
#-----------------------------------------------------------------------------------------------------------------------

def updating_student_records(file_paths, admin_username):
    if admin_username is None:
        print("You must be logged in to update user information.")
        return
    STUDENT_FILE = file_paths["STUDENT_FILE"]
    username = input("Enter student account username that you would like to edit: ")
    print("----Update Personal Information----")
    new_contact_num = input("Enter your new contact number (leave blank if no changes): ")
    new_emergency_num = input("Enter your new emergency contact number (leave blank if no changes): ")
    new_address =  input("Enter your new address (leave blank if no changes): ")
    try: #Updating students.txt
        with open(STUDENT_FILE, "r") as file:
            lines = file.readlines()
        with open(STUDENT_FILE, "w") as file:
            for line in lines:
                parts = line.strip().split(",")
                if len(parts) == 6: #Check if there is 6 parts
                    student_id, student_username, student_pass, contact_num, emergency_contact_num, address = parts
                    if student_username == username: #identify the correct student
                        if new_contact_num:
                            contact_num = new_contact_num
                        if new_emergency_num:
                            emergency_contact_num = new_emergency_num
                        if new_address:
                            address = new_address
                        #Writes the updated information back into students.txt file
                        file.write(f'{student_id},{student_username},{student_pass},{contact_num},{emergency_contact_num},{address}\n')
                        print("Personal information updated successfully!")
                        #username = student_username #change username if updated -> Removed to make sure the changes are done AFTER all files have been updated.
                    else:
                        file.write(line)
                else: #Added else
                    file.write(line)
    except FileNotFoundError:
        print(f"{STUDENT_FILE} not found.")
    except Exception as e:
        print(f"An Error Occurred: {e}")

#-----------------------------------------------------------------------------------------------------------------------
# VIEWING STUDENT RECORDS
def viewing_student_records(file_paths, admin_username):
    #Views student grades from a file, but only if the admin is logged in.
    GRADE_FILE = file_paths["GRADES_FILE"]
    if admin_username is None:
        print("You must be logged in to view student grades.")
        return
    student_id = input("Enter the student's id to check grades: ")
    print(f"\n----Grades for {student_id}----")
    try:
        with open(GRADE_FILE, "r") as file:
            grades_found = False
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 4:  # Validate that the line has 4 parts
                    student_username_from_file, course, grade, instructor = parts
                    if student_username_from_file == student_id:  # Use the input username
                        print(f"Course: {course}, Grade: {grade}, Instructor: {instructor}")
                        grades_found = True
            if not grades_found:  # Check after the loop if no grades were found
                print(f"No grades found for student: {student_id}.")
    except FileNotFoundError:
        print("Grades file not found.")
    except Exception as e:
        print(f"Error reading grades file: {e}")

#-----------------------------------------------------------------------------------------------------------------------

#GENERATE COURSE ID FOR ADMIN
def generate_course_id_admin(file_paths):
#Generates a unique course ID (C01, C02, etc.).
    COURSE_FILE = file_paths["COURSE_FILE"]
    try:
        with open(COURSE_FILE, "r") as file:
            lines = file.readlines()
            if not lines:
                return "C01"  # Start with C01 if the file is empty

            last_line = lines[-1].strip()
            last_course_id = last_line.split(",")[0]
            last_id_number = int(last_course_id[2:])  # Changed to [2:] to account for "C"
            new_id_number = last_id_number + 1
            new_course_id = f"C{new_id_number:02}"
            return new_course_id
    except FileNotFoundError:
        return "C01"  # Start with C01 if the file doesn't exist
    except Exception:
        return "C01"  # Start with C01 in case of error

#-----------------------------------------------------------------------------------------------------------------------

#MANAGING COURSE OFFERING
def manage_course_offering(file_paths, admin_username):
    #Views course offering from a file, but only if the admin is logged in.
    if admin_username is None:
        print("You must be logged in to managing course offering.")
        return

    COURSE_FILE = file_paths["COURSE_FILE"]
    COURSE_PRICE_FILE = file_paths["COURSE_PRICE_FILE"]

    while True:
        print("\nManage Course Offering")
        print("1. Create Course Offering")
        print("2. Update Course Offering")
        print("3. Delete Course Offering")
        print("4. Exit")
        try:
            admin_choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid Input. Please enter a number between 1 and 4.")
            continue

        if admin_choice not in [1, 2, 3, 4]:
            print("Invalid Input. Please enter a number between 1 and 4.")
            continue

        if admin_choice == 1:
            print("---Create Course Offering---")

            course_id = generate_course_id_admin(file_paths)
            course_name = input("Enter the Course name: ")
            course_description = input("Enter the Course description: ")
            lecturer_name = input("Enter the Lecturer name: ")
            course_price = input("Enter the Course price in RM : ")


            try:
                with open(COURSE_FILE, "a") as file:
                    file.write(f'{course_id},{course_name},{course_description},{lecturer_name}\n')
                print("Successfully added a course!")
                with open(COURSE_PRICE_FILE, "a") as file:
                    file.write(f'{course_id},{course_name},RM {course_price}\n')
                break  # Exit the loop after successful creation
            except Exception as e:
                print(f'An Error Occurred adding a course: {e}')
                continue #restart account creation process if error occurs

        elif admin_choice == 2:

            course_id = input("Enter course ID that you would like to edit: ")
            print("----Update Personal Information----")
            new_course_name = input("Enter your new course name (leave blank if no changes): ")
            new_course_description = input("Enter your course description (leave blank if no changes): ")
            new_lecturer_name = input("Enter your new lecturer name (leave blank if no changes): ")
            new_course_price = input("Enter your new course price in RM (leave blank if no changes): ")
            try:  # Updating students.txt
                with open(COURSE_FILE, "r") as file:
                    lines = file.readlines()
                with open(COURSE_FILE, "w") as file:
                    for line in lines:
                        parts = line.strip().split(",")
                        if len(parts) == 4:  # Check if there is 4 parts
                            course_id, new_course_name, new_course_description, new_lecturer_name = parts
                            if course_id == course_id:  # identify the correct course
                                if new_course_name:
                                    course_name = new_course_name
                                if new_course_description:
                                    course_topic = new_course_description
                                if new_lecturer_name:
                                    lecturer_name = new_lecturer_name
                                # Writes the updated information back into course.txt file
                                file.write(
                                    f'{course_id},{new_course_name},{new_course_description},{new_lecturer_name}\n')
                            else:
                                file.write(line)
                        else:  # Added else
                            file.write(line)

                with open(COURSE_PRICE_FILE, "r") as file:
                    lines = file.readlines()
                with open(COURSE_PRICE_FILE, "w") as file:
                    for line in lines:
                        parts = line.strip().split(",")
                        if len(parts) == 3:  # Check if there is 3 parts
                            course_id, new_course_name, new_course_price = parts
                            if course_id == course_id:  # identify the correct course
                                if new_course_name:
                                    course_name = new_course_name
                                if new_course_price:
                                    course_price = new_course_price
                                # Writes the updated information back into course and price.txt file
                                file.write(
                                    f'{course_id},{new_course_name},RM {course_price}\n')
                                print("Course updated successfully!")
                            else:
                                file.write(line)
                        else:  # Added else
                            file.write(line)
                            break
            except FileNotFoundError:
                print(f"{COURSE_FILE} not found.")
                break
            except Exception as e:
                print(f"An Error Occurred: {e}")
                continue


        elif admin_choice == 3:
            course_id_to_delete = input("Enter the course ID to delete: ")  # changed course_id variable
            try:
                # Delete from COURSE_FILE
                deleted_course = False
                with open(COURSE_FILE, "r") as file:
                    course_lines = file.readlines()
                with open(COURSE_FILE, "w") as file:
                    for line in course_lines:
                        parts = line.strip().split(",")
                        if len(parts) > 0 and parts[0] != course_id_to_delete:
                            file.write(line)
                        elif len(parts) > 0 and parts[0] == course_id_to_delete:
                            deleted_course = True  # mark if its deleted
                # Delete from COURSE_PRICE_FILE
                deleted_price = False
                with open(COURSE_PRICE_FILE, "r") as file:
                    price_lines = file.readlines()
                with open(COURSE_PRICE_FILE, "w") as file:
                    for line in price_lines:
                        parts = line.strip().split(",")
                        if len(parts) > 0 and parts[0] != course_id_to_delete:
                            file.write(line)
                        elif len(parts) > 0 and parts[0] == course_id_to_delete:
                            deleted_price = True  # mark if its deleted
                if not deleted_course or not deleted_price:  # if course or course file not found,
                    print(f"Course with ID '{course_id_to_delete}' not found.")  # changed variable
                else:  # or else, the following id has been removed
                    print(f"Course with ID '{course_id_to_delete}' removed successfully!")  # changed variable
                    break
            except FileNotFoundError:
                print("Course File not found!")
                break
            except Exception as e:
                print(f"Course file not found: {e}")
                continue

        elif admin_choice == 4: #Exit
            print("Returning back to Admin Menu")
            break

#-----------------------------------------------------------------------------------------------------------------------


def update_class_schedules(file_paths, admin_username):
    if admin_username is None:
        print("You must be logged in to manage class schedules.")
        return

    TIMETABLE_FILE = file_paths["timetable_file_path"]
    RESOURCE_FILE = file_paths["RESOURCE_FILE"]

    while True:
        print("\nManaging Class Schedules")
        print("1. Update Class Schedules")
        print("2. Update Resource Allocation")
        print("3. Exit")

        try:
            admin_choice = int(input("Enter your choice (1-3): "))
        except ValueError:
            print("Invalid Input. Please enter a number between 1 and 3.")
            continue

        if admin_choice not in [1, 2, 3]:
            print("Invalid Input. Please enter a number between 1 and 3.")
            continue

        if admin_choice == 1:
            print("---Updating Class Schedules---")
            course_id_to_update = input("Enter Course ID to update: ")  # Specify which course to update
            course_name = input("Enter new Course Name: ")
            course_time = input("Enter new Class Time (e.g., Monday 7AM - 9AM): ")
            course_room = input("Enter new Classroom: ")

            try:
                with open(TIMETABLE_FILE, "r") as file:
                    lines = file.readlines()

                updated_lines = []  # Store the modified lines

                for line in lines:
                    parts = line.strip().split(",")
                    if len(parts) == 4:
                        course_id, _, _, _ = parts  # Extract course ID from existing data
                        if course_id == course_id_to_update:  # Compare with entered course ID
                            updated_lines.append(
                                f'{course_id_to_update},{course_name},{course_time},{course_room}\n')  # Update if matches
                        else:
                            updated_lines.append(line)  # Keep original line if it does not match
                    else:
                        updated_lines.append(line)  # Keep original line if it is not in the right format

                with open(TIMETABLE_FILE, "w") as file:
                    file.writelines(updated_lines)  # Write updated lines back to the file

                print("Timetable updated successfully!")


            except FileNotFoundError:
                print("Timetable File not found!")
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                continue

        elif admin_choice == 2:
            print("---Updating Recourse Allocation---")
            recourse_id = input("Enter recourse id: ")
            new_recourse_name = input("Enter recourse Name: ")
            new_material_file = input("Enter material file: ")
            try:  # Updating recourse
                with open(RESOURCE_FILE, "r") as file:
                    lines = file.readlines()

                updated_lines = []
                for line in lines:
                    parts = line.strip().split(",")
                    if len(parts) == 3:  # Check if there is 3 parts
                        course_id = parts[0]
                        course_name = parts[1]
                        material_file = parts[2]
                        if course_id == recourse_id:
                            if new_recourse_name:
                                course_name = new_recourse_name
                            if new_material_file:
                                material_file = new_material_file

                            # Writes the updated information back into resources.txt file
                            updated_lines.append(f'{course_id},{course_name},{material_file}\n')
                            print("Recourse updated successfully!")
                        else:
                            updated_lines.append(line)
                    else:
                        updated_lines.append(line)

                with open(RESOURCE_FILE, "w") as file:
                    file.writelines(updated_lines)

            except FileNotFoundError:
                print(f"{recourse_id} not found.")
            except Exception as e:
                print(f"An Error Occurred: {e}")

        elif admin_choice == 3:  # Exit
            print("Returning back to Admin Menu")
            break

#-----------------------------------------------------------------------------------------------------------------------

def generate_reports(file_paths, admin_username):
    if admin_username is None:
        print("You must be logged in to generate reports.")
        return
    STUDENT_FILE = file_paths["STUDENT_FILE"]
    GRADES_FILE = file_paths["GRADES_FILE"]
    ATTENDANCE_FILE = file_paths["ATTENDANCE_FILE"]
    COURSE_PRICE_FILE = file_paths["COURSE_PRICE_FILE"]
    while True:
        print("\nGenerate Reports")
        print("1. Generate Academic Performance")
        print("2. Generate Student Attendance")
        print("3. Generate Financial Reports")
        print("4. Exit")
        try:
            admin_choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid Input. Please enter a number between 1 and 4.")
            continue
        if admin_choice not in [1, 2, 3, 4]:
            print("Invalid Input. Please enter a number between 1 and 4.")
            continue
        if admin_choice == 1:
            print("---Generating Academic Reports---")
            student_id = input("Enter Student ID to generate report: ")
            try:
                with open(STUDENT_FILE, "r") as file:
                    student_name = None
                    for line in file:
                        s_id, student_name, _, _, _, _ = line.strip().split(",")
                        if s_id == student_id:
                            break
                    if not student_name:
                        print("Student ID not found.")
                        return
            except FileNotFoundError:
                print("Student file not found.")
                return
            except Exception as e:
                print(f"Error reading student file: {e}")
                return
            print(f"--- Student Report for {student_name} (Student ID: {student_id}) ---")
            try:
                with open(GRADES_FILE, "r") as file:
                    grades_found = False
                    for line in file:
                        s_id, course, grade, instructor = line.strip().split(",")
                        if s_id == student_id:
                            print(f"  Course: {course}, Grade: {grade}, Instructor: {instructor}")
                            grades_found = True
                    if not grades_found:
                        print("  No grades found for this student.")
            except FileNotFoundError:
                print("Grades file not found.")
                break
            except Exception as e:
                print(f"An error occurred while reading the grades file: {e}")
                print("--- End of Report ---")

        elif admin_choice == 2:
            print("---Generate Student Attendance---")
            student_id = input("Enter Student ID to generate report: ")

            try:
                with open(STUDENT_FILE, "r") as file:
                    student_name = None
                    for line in file:
                        s_id, student_name, _, _, _, _ = line.strip().split(",")
                        if s_id == student_id:
                            break
                    if not student_name:
                        print("Student ID not found.")
                        return
            except FileNotFoundError:
                print("Student file not found.")
                return
            except Exception as e:
                print(f"Error reading student file: {e}")
                return
            print(f"--- Student Report for {student_name} (Student ID: {student_id}) ---")

            try:
                with open(ATTENDANCE_FILE, "r") as file:
                    attendance_found = False
                    for line in file:
                        s_id, date, status, course_name = line.strip().split(",")
                        if s_id == student_id:
                            print(f"  Date: {date}, Status: {status}, Course: {course_name}")
                            attendance_found = True
                    if not attendance_found:
                        print("  No attendance records found for this student.")
            except FileNotFoundError:
                print("Attendance file not found.")
                break
            except Exception as e:
                print(f"An error occurred while reading the attendance file: {e}")
                print("--- End of Report ---")

        elif admin_choice == 3:
            print("---Generate Financial Reports---")
            student_id = input("Enter Student ID to generate report: ")
            course_id = input("Enter the Course ID: ")

            try:
                with open(STUDENT_FILE, "r") as file:
                    student_name = None
                    student_found = False  # Flag to track if student ID is found in STUDENT_FILE
                    for line in file:
                        s_id, student_name, _, _, _, _ = line.strip().split(",")
                        if s_id == student_id:
                            student_found = True
                            break  # Exit loop once student ID is found
                    if not student_found:
                        print("Student account not found.")
                        return  # Exit function if student ID is not found
            except FileNotFoundError:
                print("Student file not found.")
                return
            except Exception as e:
                print(f"Error reading student file: {e}")
                return
            print(f"--- Financial Report for {student_name} (Student ID: {student_id}) ---")

            try:

                with open(COURSE_PRICE_FILE, "r") as file:
                    course_found = False
                    for line in file:
                        parts = line.strip().split(",")
                        if len(parts) == 3 and parts[
                            0] == course_id:  # Check for correct number of parts *and* course ID
                            course_id, course, course_price = parts
                            print(f"  Course: {course}, Course price: {course_price}")
                            course_found = True
                            break  # No need to read the rest of the file

                    if not course_found:
                        print("  No course price found for this course ID.")

            except FileNotFoundError:
                print("Course price file not found.")
            except Exception as e:
                print(f"An error occurred while reading the course price file: {e}")
            print("--- End of Report ---")

        elif admin_choice == 4: #Exit
            print("Returning back to Admin Menu")
            break

def exiting():
    print("Exiting Program. Goodbye!")

#-----------------------------------------------------------------------------------------------------------------------

#---ADMIN MENU---
def admin_menu(file_paths):
    stored_admin_username = None
    admin_username = None  # initialize username here

    USER_FILE = file_paths["USER_FILE"]
    STUDENT_FILE = file_paths["STUDENT_FILE"]
    GRADES_FILE = file_paths["GRADES_FILE"]
    ATTENDANCE_FILE = file_paths["ATTENDANCE_FILE"]
    COURSE_FILE = file_paths["COURSE_FILE"]
    TEACHER_FILE = file_paths["TEACHER_FILE"]
    STAFF_FILE = file_paths["STAFF_FILE"]
    COURSE_PRICE_FILE = file_paths["COURSE_PRICE_FILE"]
    SCHEDULE_FILE = file_paths["SCHEDULE_FILE"]
    RESOURCE_FILE = file_paths["RESOURCE_FILE"]

    while True:
        print("\nAdministrator Menu:")
        print("1. Login Admin Account")
        print("2. Create User Account")
        print("3. Delete User Account")
        print("4. Edit User Account")
        print("5. Updating Student Records")
        print("6. View Student Records")
        print("7. Manage Course Offerings")
        print("8. Update Class Schedules")
        print("9. Generate Reports")
        print("10. Exit")
        try:
            user_choice = int(input("Enter your choice (1-10): "))
        except ValueError:
            print("Invalid Input. Please enter a number between 1 and 10.")
            continue  # jumps to the next iteration in the loop

        if user_choice == 1:
            print("---Admin Account Login---")
            admin_username = admin_login(file_paths, admin_username)
            if admin_username:
                print(f"Successfully logged in as {admin_username}")
                stored_admin_username = admin_username
            else:
                print("Login failed")
                admin_username = None
        elif user_choice == 2:
            create_user_account(file_paths, admin_username)
        elif user_choice == 3:
            if admin_username:  # checks if the admin is signed in
                delete_user_account(file_paths, admin_username)
            else:  # tells you to sign in
                print("You must sign in before deleting!")
        elif user_choice == 4:
            print("---Edit User Accounts---")
            edit_user_info_admin(file_paths, stored_admin_username)
        elif user_choice == 5:
            print("---Updating Student Records---")
            updating_student_records(file_paths, admin_username)
        elif user_choice == 6:
            print("---View Student Records---")
            if stored_admin_username:
                viewing_student_records(file_paths, stored_admin_username)
            else:
                print("You must log in before viewing Student records")
        elif user_choice == 7:
            if stored_admin_username:
                manage_course_offering(file_paths, admin_username)
            else:
                print("You must log in before managing course offerings")
        elif user_choice == 8:
            if stored_admin_username:
                update_class_schedules(file_paths, admin_username)
            else:
                print("You must log in before update class schedules")
        elif user_choice == 9:
            if stored_admin_username:
                generate_reports(file_paths, admin_username)
            else:
                print("You must log in before generating reports")
        elif user_choice == 10:
            print("Exiting")
            break
        else:
            print("Invalid choice. Try Again")  # error handling if user invalid choice

#-----------------------------------------------------------------------------------------------------------------------

# ---STUDENT LOGIN FUNCTION---
#allows for student users to log in to their account
def student_login(file_paths):
    print("----Student Login----\n")
    student_username = input("Enter your username: ")
    student_pass = input("Enter your password: ")
    try:
        with open(file_paths["USER_FILE"], "r") as file:  # Access through file_paths dictionary
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:  # separates into 3 parts to format the file
                    stored_student_user, stored_student_pass, role = parts
                    if role == "student" and student_username == stored_student_user and student_pass == stored_student_pass:
                        return student_username
            print("Login Failed! Invalid Credentials.")
            return None
    except FileNotFoundError:
        print("users.txt file doesn't exist. Please contact your administrator.")
        return None
    except Exception as e:
        print(f'An Error Occurred, Please Try Again: {e}')
        return None

# -------------------------------------------------------------------------------------------------------------------------------

# ---UPDATE PERSONAL INFO FUNCTION---
def update_personal_info(username, file_paths):
    # Updates personal information for a student.
    # The current username of the student (username)
    # The updated username, or the original username if no changes were made.
    if username is None: #if its not detected/read (didnt log in)
        print("You must be logged in to update your information.")
        return None
#all file paths are localized and ONLY declared in the function
    print("----Update Personal Information----")
    new_student_username = input("Enter your new username (leave blank if no changes): ")
    new_student_password = input("Enter your new password (leave blank if no changes): ")
    new_contact_num = input("Enter your new contact number (leave blank if no changes): ")
    new_emergency_num = input("Enter your new emergency contact number (leave blank if no changes): ")
    new_address = input("Enter your city of residency (leave blank if no changes): ")
    student_file_path = file_paths["STUDENT_FILE"]
    user_file_path = file_paths["USER_FILE"]
    grades_file_path = file_paths["GRADES_FILE"]
    enrollment_file_path = file_paths["ENROLLMENT_FILE"]
    try: # Update students.txt
        with open(student_file_path, "r") as file:
            lines = file.readlines()
        with open(student_file_path, "w") as file:
            for line in lines:
                parts = line.strip().split(",")
                if len(parts) == 6: #reads the old 5 commas and replaces it with new values
                    student_id, student_username, student_pass, contact_num, emergency_contact_num, address = parts
                    if student_username == username:
                        if new_student_username:
                            student_username = new_student_username
                        if new_student_password:
                            student_pass = new_student_password
                        if new_contact_num:
                            contact_num = new_contact_num
                        if new_emergency_num:
                            emergency_contact_num = new_emergency_num
                        if new_address:
                            address = new_address
                        file.write(
                            f'{student_id},{student_username},{student_pass},{contact_num},{emergency_contact_num},{address}\n')
                        print("Personal information updated successfully!")
                    else:
                        file.write(line)
                else:
                    file.write(line)
        with open(user_file_path, "r") as file: # updates users.txt
            user_lines = file.readlines()
        with open(user_file_path, "w") as file:
            for line in user_lines:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    user_user, user_pass, user_role = parts
                    if user_user == username:
                        if new_student_username:
                            user_user = new_student_username
                        if new_student_password:
                            user_pass = new_student_password
                        file.write(f"{user_user},{user_pass},{user_role}\n")
                    else:
                        file.write(line)
                else:
                    file.write(line)  # in case any corrupted lines in file
    except FileNotFoundError:
        print(f"{student_file_path} not found.")
    except Exception as e:
        print(f"An Error Occurred: {e}")
    if new_student_username:
        return new_student_username
    return username

# -------------------------------------------------------------------------------------------------------------------------------

# ---BROWSE COURSES FUNCTION---
def browse_courses(file_paths):
    #Browses and displays available courses from the course file.
    #file_paths dictionary containing file paths.
    course_file_path = file_paths["COURSE_FILE"]
    try:
        with open(course_file_path, "r") as file:
            courses = file.readlines()
    except FileNotFoundError:
        print("Course file does not exist")
        return  # Add return to exit function if course file is not found
    print("\n----Available Courses----")
    for course in courses:
        course_id, course_name, course_description, course_instructor = course.strip().split(",")
        print(f"Course ID: {course_id}")
        print(f"Course Name: {course_name}")
        print(f"Description: {course_description}")
        print(f"Instructor: {course_instructor}\n")

# -------------------------------------------------------------------------------------------------------------------------------

# ---ENROLL IN COURSE FUNCTION---
def enroll_in_course(file_paths, username):
    # username : The username of the student.
    if username is None:
        print("You must be logged in to enroll in a course.")
        return
    print("----Enroll In Course----")
    course_id_to_enroll = input("Enter the Course ID to enroll in : ")
    enrollment_file_path = file_paths["ENROLLMENT_FILE"]
    student_file_path = file_paths["STUDENT_FILE"]
    course_file_path = file_paths["COURSE_FILE"]
    try:
        with open(course_file_path, "r") as file:
            courses = file.readlines()
            course_exists = False
            course_name = None  # Capture the course name
            for course in courses:
                course_id, course_name, _, _ = course.strip().split(",")
                if course_id == course_id_to_enroll:
                    course_exists = True #if the course ID entered by the student exists then continue to enroll
                    break
            if not course_exists:
                print("Invalid Course ID. Please enter a valid Course ID.")
                return
    except FileNotFoundError:
        print(f"Error: {course_file_path} not found.")
        return
    except Exception as e:
        print(f"An error occurred while reading {course_file_path}: {e}")
        return
    student_id = None
    try:
        with open(student_file_path, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 6:
                    stored_student_id, stored_student_username, _, _, _, _ = parts
                    if stored_student_username == username:
                        student_id = stored_student_id
                        break
    except FileNotFoundError:
        print(f"Error: {student_file_path} not found.")
        return
    except Exception as e:
        print(f"An error occurred while reading {student_file_path}: {e}")
        return
    if student_id is None:
        print("Student ID not found. Please contact administrator.")
        return
    try:
        with open(enrollment_file_path, "a") as file:
            file.write(f"{student_id},{course_id_to_enroll}\n")
            if course_name != None: #makes sure the course name has a value before executing the if block
              print(f"Successfully enrolled in {course_name}")
            else:
              print(f"Successfully enrolled")
    except Exception as e:
        print(f"An error occurred while enrolling in a course: {e}")

# -------------------------------------------------------------------------------------------------------------------------------

# ---ACCESS COURSE MATERIALS FUNCTION---
def access_course_materials(file_paths):
    print("----Access Course Materials----")
    course_id = input("Enter the Course ID to access materials: ")
    material_file_path = file_paths["MATERIAL_FILE"]  #
    try:
        with open(material_file_path, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    material_course_id, material_course_name, material_file = parts
                    if material_course_id == course_id:
                        print(f"\nCourse Materials for {material_course_name}:")
                        print(f"File: {material_file}\n")
                        return
            print("Course materials not found for the given Course ID.")
    except FileNotFoundError:
        print(f"Error: {material_file_path} not found. Please contact administrator.")
    except Exception as e:
        print(f"An error occurred while reading {material_file_path}: {e}")

# -------------------------------------------------------------------------------------------------------------------------------

# ---VIEW GRADES FUNCTION---
def view_grades(file_paths, username):
    if username is None:
        print("You must be logged in to view your grades.")
        return
    print("\n----Your Grades----")
    student_id = None
    grades_file_path = file_paths["GRADES_FILE"]  # Access through file_paths
    student_file_path = file_paths["STUDENT_FILE"]  # Access through file_paths
    try:
        with open(student_file_path, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 6:
                    stored_student_id, stored_student_username, _, _, _, _ = parts
                    if stored_student_username == username:
                        student_id = stored_student_id
                        break
    except FileNotFoundError:
        print(f"Error: {student_file_path} not found.")
        return
    except Exception as e:
        print(f"An error occurred while reading {student_file_path}: {e}")
        return
    if student_id is None:
        print("Student ID not found for the logged-in user.")
        return
    try:
        with open(grades_file_path, "r") as file:
            grades_found = False
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    student_grade_id, course, grade, instructor = parts
                    if student_grade_id == student_id:
                        print(f"Course: {course}, Grade: {grade}, Instructor: {instructor}")
                        grades_found = True
            if not grades_found:
                print("No grades found for your account.")
    except FileNotFoundError:
        print("Grades file not found.")
    except Exception as e:
        print(f"Error reading grades file: {e}")

# -------------------------------------------------------------------------------------------------------------------------------

# ---FUNCTION TO SUBMIT FEEDBACK---
def submit_feedback(file_paths,username):
    if username is None:
        print("You must be logged in to send feedback.")
        return
    print("----Student Feedback----")
    student_feedback = input("Please enter your feedback:  ")
    student_id = None
    feedback_file_path = file_paths["FEEDBACK_FILE"]
    student_file_path = file_paths["STUDENT_FILE"]
    try:
        with open(student_file_path, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 6:
                    stored_student_id, stored_student_username, _, _, _, _ = parts
                    if stored_student_username == username:
                        student_id = stored_student_id
                        break
    except FileNotFoundError:
        print(f"Error: {student_file_path} not found.")
        return
    except Exception as e:
        print(f"An error occurred while reading {student_file_path}: {e}")
        return
    if student_id is None:
        print("Error: Student ID not found for the logged-in user.")
        return
    try:
        with open(feedback_file_path, "a") as file:
            file.write(f'{student_id},{student_feedback}\n')
            print("Your feedback has been sent!")
    except Exception as e:
        print(f"An error occurred while saving feedback: {e}")


# -------------------------------------------------------------------------------------------------------------------------------

# ---STUDENT MENU---
def student_menu(file_paths):
    user_file_path = file_paths["USER_FILE"]
    student_file_path = file_paths["STUDENT_FILE"]
    course_file_path = file_paths["COURSE_FILE"]
    enrollment_file_path = file_paths["ENROLLMENT_FILE"]
    feedback_file_path = file_paths["FEEDBACK_FILE"]
    grades_file_path = file_paths["GRADES_FILE"]
    material_file_path = file_paths["MATERIAL_FILE"]
    # Access student_login with file_paths["STUDENT_FILE"]
    logged_in_username = None
    while True:
        print("-----Welcome to the Student Menu----\n")
        print("1. Login")
        print("2. Update Personal Information")
        print("3. Browse Courses")
        print("4. Enroll in a Course")
        print("5. Access Course Materials")
        print("6. View Grades")
        print("7. Submit Feedback")
        print("8. Exit")
        try:
            student_choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid Input. Please enter a number between 1 and 9.")
            continue
        if student_choice == 1:
            logged_in_username = student_login(file_paths)
            if logged_in_username:
                print(f"Successfully logged in as {logged_in_username}")
        elif student_choice == 2:
            if logged_in_username:
                logged_in_username = update_personal_info(logged_in_username, file_paths)
            else:
                print("You must log in before updating your information.")
        elif student_choice == 3:
            browse_courses(file_paths) #Pass the file_paths dictionary
        elif student_choice == 4:
            if logged_in_username:
                enroll_in_course(file_paths, logged_in_username)
            else:
                print("You must be logged in to enroll in a course.")
        elif student_choice == 5:
            if logged_in_username:
                access_course_materials(file_paths) #Pass the file_paths dictionary
            else:
                print("You must be logged in to access course materials.")
        elif student_choice == 6:
            if logged_in_username:
              view_grades(file_paths, logged_in_username) #Pass the file_paths dictionary
            else:
                print("You must be logged in to view your grades.")
        elif student_choice == 7:
            if logged_in_username:
                submit_feedback(file_paths, logged_in_username) #Pass the file_paths dictionary
            else:
                print("You must log in to submit feedback.")
        elif student_choice == 8:
            print("Exiting Student Menu...")
            return
        else:
            print("Invalid choice. Please try again.")

# ---TEACHER MENU---
def teacher_menu(file_paths):
    user_file_path = file_paths["USER_FILE"]
    teacher_file_path = file_paths["TEACHER_FILE"]
    course_file_path = file_paths["COURSE_FILE"]
    enrollment_file_path = file_paths["ENROLLMENT_FILE"]
    grades_file_path = file_paths["GRADES_FILE"]
    attendance_file_path = file_paths["ATTENDANCE_FILE"]
    student_file_path = file_paths["STUDENT_FILE"]
    # Access student_login with file_paths["STUDENT_FILE"]
    logged_in_username = None
    while True:
        print("\n-----Welcome to the Teacher Menu-----\n")
        print("1. Login")
        print("2. Create Teacher Account")  # Moved to second option
        print("3. Create Course")
        print("4. Edit Course")
        print("5. Enroll/Unenroll Student")
        print("6. Grade Assignments")
        print("7. Track Attendance ")
        print("8. Generate Student Report")
        print("9. Logout")
        try:
            teacher_choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
        if teacher_choice == 1:
            logged_in_username = teacher_login(file_paths) #changed here
            if logged_in_username:
                print(f"Successfully logged in as {logged_in_username}")
        elif teacher_choice == 2:  # Create Teacher Account
            create_teacher_account(file_paths) #changed here
        elif teacher_choice == 3:
            if logged_in_username:
                create_course(file_paths, logged_in_username)
            else:
                print("You must log in to create a course.")
        elif teacher_choice == 4:
            if logged_in_username:
                edit_course(file_paths)
            else:
                print("You must log in to edit a course.")
        elif teacher_choice == 5:
            if logged_in_username:
                enroll_unenroll_student(file_paths)
            else:
                print("You must log in to enroll/unenroll students.")
        elif teacher_choice == 6:
            if logged_in_username:
                grade_assignments(file_paths)
            else:
                print("You must log in to grade assignments.")
        elif teacher_choice == 7:
            if logged_in_username:
                track_attendance(file_paths)  # Just view for now
            else:
                print("You must log in to track attendance.")
        elif teacher_choice == 8:
            if logged_in_username:
                generate_student_report(file_paths)
            else:
                print("You must log in to generate reports.")
        elif teacher_choice == 9:
            print("Logging out...")
            return
        else:
            print("Invalid choice. Please try again.")

#--------------------------------------------------------------------------------------------------------------------------------


# ---TEACHER LOGIN FUNCTION----
def teacher_login(file_paths):
    print("----Teacher Login----\n")
    teacher_username = input("Enter your username: ")
    teacher_pass = input("Enter your password: ")

    user_file_path = file_paths["USER_FILE"]

    try:
        with open(user_file_path, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    stored_teacher_user, stored_teacher_pass, role = parts
                    if role == "teacher" and teacher_username == stored_teacher_user and teacher_pass == stored_teacher_pass:
                        return teacher_username
            print("Login Failed! Invalid Credentials.")
            return None
    except FileNotFoundError:
        print("users.txt file doesn't exist. Please contact administrator.")
        return None
    except Exception as e:
        print(f'An Error Occurred, Please Try Again: {e}')
        return None

#--------------------------------------------------------------------------------------------------------------------------------

# ---CREATE COURSE FUNCTION TEACHER---
def create_course(file_paths, logged_in_username):
    #Creates a new course, generating a unique course ID and writing course details to the course file.
        #file_paths : Dictionary of file paths.
       #logged_in_username: The username of the logged-in teacher.
    print("----Create Course----\n")
    course_name = input("Enter Course Name: ")
    course_description = input("Enter Course Description: ")
    course_file_path = file_paths["COURSE_FILE"]

    course_id = generate_course_id(file_paths)  # Pass file_paths to generate_course_id

    try:
        with open(course_file_path, "a") as file:
            file.write(f"{course_id},{course_name},{course_description},{logged_in_username}\n")
        print(f"Course '{course_name}' created successfully with ID: {course_id}!")
    except Exception as e:
        print(f"An error occurred while creating the course: {e}")
#-----------------------------------------------------------------------------------------------------------------------

def generate_course_id(file_paths):
    #Generates a unique course ID (C01, C02, etc.)
        #file_paths (dict): Dictionary of file paths.
    #Returns:
        #unique course ID
    course_file_path = file_paths["COURSE_FILE"]
    try:
        with open(course_file_path, "r") as file:
            lines = file.readlines()
            if not lines:
                return "C01"  # Start with C01 if the file is empty
            last_line = lines[-1].strip()
            last_course_id = last_line.split(",")[0]
            try:
                last_id_number = int(last_course_id[1:])  # Changed to [1:] to account for "C"
                new_id_number = last_id_number + 1
                new_course_id = f"C{new_id_number:02}"
            except ValueError:  # handles cases where the course ID is not in the expected format
                return "C01"
            return new_course_id
    except FileNotFoundError:
        return "C01"  # Start with C01 if the file doesn't exist
    except Exception:
        return "C01"  # Start with C01 in case of error

#------------------------------------------------------------------------------------------------------------------------------

# ---EDIT COURSE---
def edit_course(file_paths):
    #Edits a course in the course file.
    #Args:
        #file_paths (dict): Dictionary of file paths.
    print("----Edit Course----\n")
    course_id_to_edit = input("Enter the Course ID to edit: ")
    course_file_path = file_paths["COURSE_FILE"]  # Access via file_paths
    try:
        with open(course_file_path, "r") as file:
            courses = file.readlines()
    except FileNotFoundError:
        print("Course file not found.")
        return
    except Exception as e:
        print(f"An error occurred while reading the course file: {e}")
        return
    updated_courses = []
    course_found = False
    for course in courses:
        course_id, course_name, course_description, instructor = course.strip().split(",")
        if course_id == course_id_to_edit:
            course_found = True
            print(f"Current Course Name: {course_name}")
            new_course_name = input("Enter new Course Name (leave blank to keep current): ")
            print(f"Current Course Description: {course_description}")
            new_course_description = input("Enter new Course Description (leave blank to keep current): ")
            if new_course_name:
                course_name = new_course_name
            if new_course_description:
                course_description = new_course_description
            updated_courses.append(f"{course_id},{course_name},{course_description},{instructor}\n")
            print("Course updated successfully!")
        else:
            updated_courses.append(course)
    if not course_found:
        print("Course not found.")
        return
    try:
        with open(course_file_path, "w") as file:
            file.writelines(updated_courses)
    except Exception as e:
        print(f"An error occurred while writing to the course file: {e}")

#-----------------------------------------------------------------------------------------------------------------------

# ---ENROLL/UNENROLL STUDENT---
def enroll_unenroll_student(file_paths):
    print("----Enroll/Unenroll Student----\n")
    action = input("Enter 'enroll' to enroll or 'unenroll' to unenroll: ").lower() #only accepts lowercase answer
    if action not in ("enroll", "unenroll"):
        print("Invalid action. Please enter 'enroll' or 'unenroll'.")
        return
    student_id = input("Enter Student ID: ")
    course_id = input("Enter Course ID: ")
    enrollment_file_path = file_paths["ENROLLMENT_FILE"]
    student_file_path = file_paths["STUDENT_FILE"]
    course_file_path = file_paths["COURSE_FILE"]
    # Check if the student ID exists
    try:
        with open(student_file_path, "r") as student_file:
            student_found = False
            for line in student_file:
                s_id, _, _, _, _, _ = line.strip().split(",")
                if s_id == student_id:
                    student_found = True
                    break
            if not student_found:
                print("Student ID not found.")
                return
    except FileNotFoundError:
        print("Student file not found.")
        return
    except Exception as e:
        print(f"Error reading student file: {e}")
        return
    # Check if the course ID exists
    try:
        with open(course_file_path, "r") as course_file:
            course_found = False
            for line in course_file:
                c_id, _, _, _ = line.strip().split(",")
                if c_id == course_id:
                    course_found = True
                    break
            if not course_found:
                print("Course ID not found.")
                return
    except FileNotFoundError:
        print("Course file not found.")
        return
    except Exception as e:
        print(f"Error reading course file: {e}")
        return
    if action == "enroll":
        try:
            with open(enrollment_file_path, "r") as file:
                for line in file:
                    s_id, c_id = line.strip().split(",")
                    if s_id == student_id and c_id == course_id:
                        print("Student is already enrolled in this course.")
                        return
            with open(enrollment_file_path, "a") as file:
                file.write(f"{student_id},{course_id}\n")
            print("Student enrolled successfully!")
        except FileNotFoundError:
            print("Enrollment file not found.")
            return
        except Exception as e:
            print(f"An error occurred while enrolling the student: {e}")
    elif action == "unenroll":
        try:
            with open(enrollment_file_path, "r") as file:
                enrollments = file.readlines()
        except FileNotFoundError:
            print("Enrollment file not found.")
            return
        except Exception as e:
            print(f"An error occurred while reading the enrollment file: {e}")
            return
        updated_enrollments = []
        unenrollment_successful = False
        for line in enrollments:
            s_id, c_id = line.strip().split(",")
            if s_id == student_id and c_id == course_id:
                unenrollment_successful = True
                print("Student unenrolled successfully!")
            else:
                updated_enrollments.append(line)

        if not unenrollment_successful:
            print("Student is not enrolled in this course.")
            return
        try:
            with open(enrollment_file_path, "w") as file:
                file.writelines(updated_enrollments)
        except Exception as e:
            print(f"An error occurred while writing to the enrollment file: {e}")

#-----------------------------------------------------------------------------------------------------------------------

# ---GRADE ASSIGNMENTS TEACHER FUNCTION---
def grade_assignments(file_paths):
    print("----Grade Assignments----\n")
    student_id = input("Enter Student ID: ")
    course_id = input("Enter Course ID: ")
    grade = input("Enter Grade: ")
    grades_file_path = file_paths["GRADES_FILE"]
    course_file_path = file_paths["COURSE_FILE"]
    student_file_path = file_paths["STUDENT_FILE"]
    # Check if the student ID exists
    try:
        with open(student_file_path, "r") as student_file:
            student_found = False
            for line in student_file:
                s_id, _, _, _, _, _ = line.strip().split(",")
                if s_id == student_id:
                    student_found = True
                    break
            if not student_found:
                print("Student ID not found.")
                return
    except FileNotFoundError:
        print("Student file not found.")
        return
    except Exception as e:
        print(f"Error reading student file: {e}")
        return
    # Check if the course ID exists
    try:
        with open(course_file_path, "r") as course_file:
            course_found = False
            for line in course_file:
                c_id, _, _, _ = line.strip().split(",")
                if c_id == course_id:
                    course_found = True
                    instructor = line.strip().split(",")[3]  # Get the instructor name
                    break
            if not course_found:
                print("Course ID not found.")
                return
    except FileNotFoundError:
        print("Course file not found.")
        return
    except Exception as e:
        print(f"Error reading course file: {e}")
        return
    try:
        # Check if the grade already exists for the student and course
        with open(grades_file_path, "r") as file:
            grades = file.readlines()
    except FileNotFoundError:
        print("Grades file not found.")
        grades = []  # Create an empty list if the file doesn't exist
    except Exception as e:
        print(f"An error occurred while reading the grades file: {e}")
        return
    updated_grades = []
    grade_updated = False
    for line in grades:
        s_id, c_id, _, _ = line.strip().split(",")
        if s_id == student_id and c_id == course_id:
            updated_grades.append(f"{student_id},{course_id},{grade},{instructor}\n")
            grade_updated = True
            print("Grade updated successfully!")
        else:
            updated_grades.append(line)
    if not grade_updated:
        # If the grade doesn't exist, add a new entry
        updated_grades.append(f"{student_id},{course_id},{grade},{instructor}\n")
        print("Grade added successfully!")
    try:
        with open(grades_file_path, "w") as file:
            file.writelines(updated_grades)
    except Exception as e:
        print(f"An error occurred while writing to the grades file: {e}")

#-----------------------------------------------------------------------------------------------------------------------

def track_attendance(file_paths):
    # Allows a teacher to mark or view attendance for students.
    print("----Attendance Menu----")
    print("1. Mark Attendance")
    print("2. View Attendance")
    attendance_file_path = file_paths["ATTENDANCE_FILE"]
    try:
        choice = int(input("Enter your choice (1 or 2): "))
    except ValueError:
        print("Invalid input. Please enter 1 or 2.")
        return
    if choice == 1:
        mark_attendance(file_paths)  # Pass file_paths
    elif choice == 2:
        view_attendance(file_paths)  # Pass file_paths
    else:
        print("Invalid choice. Please enter 1 or 2.")

#-----------------------------------------------------------------------------------------------------------------------

def mark_attendance(file_paths):
    # Marks attendance for a student and writes it to the attendance file.
    print("----Mark Attendance----")
    student_id = input("Enter Student ID: ")
    date = input("Enter Date (DD/MM/YY): ")
    status = input("Enter Status (Present/Absent): ")
    course_name = input("Enter Course Name: ")
    attendance_file_path = file_paths["ATTENDANCE_FILE"]
    try:
        with open(attendance_file_path, "a") as file:
            file.write(f"{student_id},{date},{status},{course_name}\n")
        print("Attendance marked successfully.")
    except Exception as e:
        print(f"An error occurred while marking attendance: {e}")

#-----------------------------------------------------------------------------------------------------------------------

def view_attendance(file_paths):
    # Views attendance records for a specific student.
    print("----View Attendance----")
    student_id_to_view = input("Enter Student ID to view attendance records: ")
    attendance_file_path = file_paths["ATTENDANCE_FILE"]
    try:
        with open(attendance_file_path, "r") as file:
            attendances = file.readlines()
            if not attendances:
                print("No attendance records found.")
                return
            attendance_found = False
            print(f"Attendance Records for Student ID: {student_id_to_view}")
            for attendance in attendances:
                student_id, date, status, course_name = attendance.strip().split(",")
                if student_id == student_id_to_view:
                    print(f"  Course: {course_name}, Date: {date}, Status: {status}")
                    attendance_found = True

            if not attendance_found:
                print(f"No attendance records found for Student ID: {student_id_to_view}")
    except FileNotFoundError:
        print("Attendance file not found.")
    except Exception as e:
        print(f"An error occurred while reading the attendance file: {e}")

#-----------------------------------------------------------------------------------------------------------------------

# ---GENERATE STUDENT REPORTS---
def generate_student_report(file_paths):
    print("----Generate Student Report----\n")
    student_id = input("Enter Student ID to generate report: ")
    attendance_file_path = file_paths["ATTENDANCE_FILE"]
    grades_file_path = file_paths["GRADES_FILE"]
    student_file_path = file_paths["STUDENT_FILE"]

    # Retrieve Student Name
    try:
        with open(student_file_path, "r") as file:
            student_name = None
            for line in file:
                s_id, username, _, _, _, _ = line.strip().split(",")
                if s_id == student_id:
                    student_name = username
                    break
            if not student_name:
                print("Student ID not found.")
                return
    except FileNotFoundError:
        print("Student file not found.")
        return
    except Exception as e:
        print(f"Error reading student file: {e}")
        return
    print(f"--- Student Report for {student_name} (Student ID: {student_id}) ---")

    # --- Attendance Information ---
    print("\n--- Attendance ---")
    try:
        with open(attendance_file_path, "r") as file:
            attendance_found = False
            for line in file:
                s_id, date, status, course_name = line.strip().split(",")
                if s_id == student_id:
                    print(f"  Date: {date}, Status: {status}")
                    attendance_found = True
            if not attendance_found:
                print("  No attendance records found for this student.")
    except FileNotFoundError:
        print("Attendance file not found.")
    except Exception as e:
        print(f"An error occurred while reading the attendance file: {e}")

    # --- Grades Information ---
    print("\n--- Grades ---")
    try:
        with open(grades_file_path, "r") as file:
            grades_found = False
            for line in file:
                s_id, course, grade, instructor = line.strip().split(",")
                if s_id == student_id:
                    print(f"  Course: {course}, Grade: {grade}, Instructor: {instructor}")
                    grades_found = True
            if not grades_found:
                print("  No grades found for this student.")
    except FileNotFoundError:
        print("Grades file not found.")
    except Exception as e:
        print(f"An error occurred while reading the grades file: {e}")
    print("\n--- End of Report ---")

#-------------------------------------------------------------------------------------------------------------------------------------------

# ---CREATE TEACHER ACCOUNT FUNCTION---
def create_teacher_account(file_paths):
    print("----Teacher Account Creation----\n")
    teacher_username = input("Enter your username: ")
    teacher_pass = input("Enter your password: ")
    teacher_file_path = file_paths["TEACHER_FILE"]
    user_file_path = file_paths["USER_FILE"]
    teacher_id = generate_teacher_id(file_paths)  # Changed to pass file_paths
    try:
        # Store teacher data in teacher file
        with open(teacher_file_path, "a") as file:
            file.write(f'{teacher_id},{teacher_username},{teacher_pass}\n')
            print("Teacher credentials successfully saved!")
        # Store username, password, and role in user file
        with open(user_file_path, "a") as file:
            file.write(f'{teacher_username},{teacher_pass},teacher\n')
            print("User credentials saved in user file.")
    except Exception as e:
        print(f'An Error Occurred, Please Try Again: {e}')

#----------------------------------------------------------------------------------------------------------------------

# ---GENERATE TEACHER ID FUNCTION---
def generate_teacher_id(file_paths):
    teacher_file_path = file_paths["TEACHER_FILE"]
    try:
        with open(teacher_file_path, "r") as file:
            lines = file.readlines()
            if not lines:
                return "T01"  # First teacher
            last_line = lines[-1].strip()
            last_teacher_id = last_line.split(",")[0]
            last_id_number = int(last_teacher_id[1:])  # Extract number from "T01"
            new_id_number = last_id_number + 1
            new_teacher_id = f"T{new_id_number:02}"
            return new_teacher_id
    except FileNotFoundError:
        return "T01"  # If file doesn't exist
    except Exception as e:
        print(f"Error generating teacher ID: {e}")
        return "T01"  # In case of error

#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------------

# ---GENERATE STUDENT REPORTS---
#-------------------------------------------------------------------------------------------------------------------------------------------


def staff_menu(file_paths):
    USER_FILE = file_paths["USER_FILE"]
    STUDENT_FILE = file_paths["STUDENT_FILE"]
    TIMETABLE_FILE = file_paths["TIMETABLE_FILE"]
    EVENT_FILE = file_paths["EVENT_FILE"]
    COURSE_FILE = file_paths["COURSE_FILE"]
    COMMUNICATION_FILE = file_paths["COMMUNICATION_FILE"]
    STAFF_FILE = file_paths["STAFF_FILE"]
    MATERIAL_FILE = file_paths["MATERIAL_FILE"]


    # Function for staff login
    def staff_login():
        print("\n----- Staff Login -----")
        username = input("Enter username: ")
        password = input("Enter password: ")
        try:
            with open(STAFF_FILE, "r") as file:  # Uses variable STAFF_FILE correctly
                for line in file:
                    stored_username, stored_password, role = line.strip().split(",")
                    if username == stored_username and password == stored_password:
                        print("Login successful!")
                        return True
            print("Invalid username or password.")
            return False
        except FileNotFoundError:
            print("Staff file not found. Contact the administrator.")
            return False
        except Exception as e:
            print(f"Error during login: {e}")
            return False

    # Function to display the staff menu
    def display_menu():
        print("\n----- Staff Menu -----")
        print("1 : staff login")
        print("2 : Manage Student Records")
        print("3 : Timetable Management")
        print("4 : Access course material")
        print("5 : Manage Events")
        print("6 : communication")
        print("7 : Log Out")

    # Function to handle user choice
    def handle_choice(choice):
        if choice == 1:
            staff_login()
        elif choice == 2:
            manage_student_records()
        elif choice == 3:
            timetable_management()
        elif choice == 4:
            courses_resources()
        elif choice == 5:
            manage_events()
        elif choice == 6:
            communication()
        elif choice == 7:
            print("Logging out...")
        else:
            print("Invalid choice. Please try again.")

    # Function to manage student records
    def manage_student_records():
        action = input("Enter 'add', 'view', or 'remove': ").strip().lower()
        if action == 'add':
            add_student()
        elif action == 'view':
            view_students()
        elif action == 'remove':
            remove_student()
        else:
            print("Invalid action.")

    # Function to add a student
    def add_student():
        username = input("Enter username: ")
        if check_username_exists(username):
            print("Username already exists.")
            return
        details = [input("Enter password: "), input("Enter contact number: "),
                   input("Enter emergency contact number: "), input("Enter city of residency: ")]
        try:
            with open(STUDENT_FILE, "a") as file:
                student_id = generate_student_id()
                file.write(f"{student_id},{username},{','.join(details)}\n")
                print("Student added successfully!")
        except Exception as e:
            print(f"Error adding student: {e}")

    # Function to check if a username exists
    def check_username_exists(username):
        try:
            with open(STUDENT_FILE, "r") as file:
                return any(username == line.split(",")[1] for line in file)
        except FileNotFoundError:
            return False
        except Exception as e:
            print(f"error checking user name: {e}")
            return False

    # Function to view all students
    def view_students():
        try:
            with open(STUDENT_FILE, "r") as file:
                students = file.readlines()
                print("List of Students:" if students else "No students found.")
                for student in students:
                    print(student.strip())
        except FileNotFoundError:
            print("Student file not found.")
            return
        except Exception as e:
            print(f"student file not found: {e}")
            return

    # Function to remove a student
    def remove_student():
        username = input("Enter the username of the student to remove: ")
        try:
            with open(STUDENT_FILE, "r") as file:
                students = file.readlines()
            with open(STUDENT_FILE, "w") as file:
                found = False
                for student in students:
                    if student.split(",")[1] != username:
                        file.write(student)
                    else:
                        found = True
                print(f"Student '{username}' removed successfully!" if found else f"Student '{username}' not found.")
        except FileNotFoundError:
            print("Student file not found.")
            return
        except Exception as e:
            print(f"Student file not found: {e}")
            return

    # Function to generate a unique student ID
    def generate_student_id():
        try:
            with open(STUDENT_FILE, "r") as file:
                lines = file.readlines()
                return f"S{int(lines[-1].split(',')[0][1:]) + 1:02}" if lines else "S01"
        except FileNotFoundError:
            return "S01"
        except Exception as e:
            print(f"cannot generate student id: {e}")
            return "S01"

    # Function to manage timetable
    def timetable_management():
        action = input("Enter 'view' or 'add': ").strip().lower()
        if action == 'view':
            view_timetable()
        elif action == 'add':
            add_timetable_entry()
        else:
            print("Invalid action.")

    # Function to view timetable
    def view_timetable():
        try:
            with open(TIMETABLE_FILE, "r") as file:
                timetable_entries = file.readlines()
                print("Current Timetable:" if timetable_entries else "No timetable entries found.")
                for entry in timetable_entries:
                    print(entry.strip())
        except FileNotFoundError:
            print("Timetable file not found.")
            return
        except Exception as e:
            print(f"Timetable file not found: {e}")
            return

    # Function to add a new timetable entry
    def add_timetable_entry():
        course_id = input("Enter Course ID: ")
        course_name = input("Enter Course Name: ")
        instructor = input("Enter Instructor Name: ")
        schedule = input("Enter Schedule (e.g., Mon 10-12): ")

        try:
            with open(TIMETABLE_FILE, "a") as file:
                file.write(f"{course_id},{course_name},{instructor},{schedule}\n")
                print("Timetable entry added successfully!")
        except Exception as e:
            print(f"Error adding timetable entry: {e}")

    # Function to manage courses
    def courses_resources():
        action = input("Enter 'view' or 'allocate': ").strip().lower()
        if action == 'view':
            view_courses()
        elif action == 'allocate':
            allocate_courses()
        else:
            print("Invalid action.")

    # Function to view resources
    def view_courses():
        try:
            with open(COURSE_FILE, "r") as file:
                courses = file.readlines()
                print("Current courses:" if courses else "No courses found.")
                for resource in courses:
                    print(resource.strip())
        except FileNotFoundError:
            print("course file not found.")
            return
        except Exception as e:
            print(f"error no view courses: {e}")
            return

    # Function to allocate a new resource
    def allocate_courses():
        course_id = input("Enter courses Name: ")
        course_name = input("Enter course id: ")
        material_file = input("enter material file: ")
        try:
            with open(MATERIAL_FILE, "a") as file:
                file.write(f"{course_id},{course_name},{material_file}\n")
                print("courses allocated successfully!")
        except Exception as e:
            print(f"Error allocating courses: {e}")

    # Function to manage events
    def manage_events():
        action = input("Enter 'view' or 'add': ").strip().lower()
        if action == 'view':
            view_events()
        elif action == 'add':
            add_event()
        else:
            print("Invalid action.")

    # Function to view events
    def view_events():
        try:
            with open(EVENT_FILE, "r") as file:
                events = file.readlines()
                print("Upcoming Events:" if events else "No events found.")
                for event in events:
                    print(event.strip())
        except FileNotFoundError:
            print("Event file not found")
            return
        except Exception as e:
            print(f"error managing events: {e}")
            return

    # Function to add a new event
    def add_event():
        event_name = input("Enter Event Name: ")
        event_date = input("Enter Event Date (YYYY-MM-DD): ")
        event_time = input("Enter Event Time (HH:MM): ")
        try:
            with open(EVENT_FILE, "a") as file:
                file.write(f"{event_name},{event_date},{event_time}\n")
                print("Event added successfully!")
        except Exception as e:
            print(f"Error adding event: {e}")

    # Function for communication
    def communication():
        message = input("Enter your message to students: ")
        try:
            with open(COMMUNICATION_FILE, "a") as file:  # Open file in append mode
                file.write(message + "\n")  # Store the message in the file
            print(f"Message stored successfully in {COMMUNICATION_FILE}!")
        except Exception as e:
            print(f"Error saving message: {e}")

    choice = 0
    while choice != 7:  # Ensuring the menu runs until logout
        display_menu()
        try:
            choice = int(input("Input your choice: "))
            handle_choice(choice)  # This correctly calls the intended function
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")

    print("You have successfully logged out.")  # Confirm logout before exiting




if __name__ == "__main__":
    file_paths = {  # its a dictionary object (looks up the key to find the definition (function)
        # method before was using global variables so had to change
        "USER_FILE": "users.txt",
        "STUDENT_FILE": "students.txt",
        "FEEDBACK_FILE": "feedback.txt",
        "COURSE_FILE": "courses.txt",
        "ENROLLMENT_FILE": "enrollments.txt",
        "GRADES_FILE": "grades.txt",
        "MATERIAL_FILE": "materials.txt",
        "ATTENDANCE_FILE": "attendance.txt",
        "TEACHER_FILE": "teachers.txt",
        "COURSE_PRICE_FILE": "course and price.txt",
        "SCHEDULE_FILE": "schedule.txt",
        "STAFF_FILE": "staff.txt",
        "RESOURCE_FILE": "resources.txt",
        "TIMETABLE_FILE": "timetable.txt",
        "EVENT_FILE": "events.txt",
        "COMMUNICATION_FILE": "communication.txt",
        "timetable_file_path": "timetable.txt"
    }
    try:
        with open(file_paths["USER_FILE"], "r") as check_file:
            pass
    except FileNotFoundError:
        print(None)
    # Call the main menu function AFTER initializing data
    __main__(file_paths)
# Project Prompt:

# You are hired to build a Student Lookup Tool for a school front office. The secretary must be able to:

    # Enter a student’s full name

    # Instantly see:

            # CPS ID

            # Homeroom

            # Grade Level

            # Primary Email

            # Students must:

            # Describe the search process

## be able to add new data
# Your program must allow the secretary to ADD a brand new student
# into the system while the program is running.

# Your job is to let the secretary type in a new student just like filling out a registration form.
# Once the form is complete, your program must turn that information into a dictionary and add it to the main list of students.
# If the student already exists (same CPS ID), your program must block the entry to prevent duplicates.

# The program should:
    # 1. Ask the user for the following information:
    #    - CPS ID
    #    - First Name
    #    - Last Name
    #    - Middle Name
    #    - Homeroom
    #    - Grade Level
    #    - Primary Email
    #    - Secondary Email

# 2. Combine the First and Last name into this format:
    #    "Last, First"  

# 3. Store all of the new information into ONE dictionary
    #    that matches the structure of the existing student data.

# 4. Add (append) that new dictionary into the main students list.

# 5. After adding the student, the program must:
    #    - Print a confirmation message
    #    - Print the total number of students in the system
    #    - Print the newly added student record

# 6. The program must NOT delete or overwrite any existing students.

# 7. If the CPS ID already exists in the system:
        #    - Do NOT add the student
        #    - Display an error message saying the CPS ID is already taken


print("Hello! Welcome to the Student Lookup Tool for John Hancock Highschool.") 
user_choice = input("Please press 1 to find an existing student, press 2 to eneter a new student, or any key to restart: ")




#code for when user presses 2 to eneter a new student
# first_name = input("Please enter the new student's FIRST name: ")
# last_name = input("Please enter the new student's LAST name: ")
# middle_name = input("Please enter your MIDDLE name: ")
# combo_name = input("Please enter your full name: ")
# homeroom = input("Please enter your homeroom: ")
# grade_level = input("Please enter your grade level: ")
# primary_email = input("Please enter your primary email address: ")
# secondary_email = input("Please enter your secondary email address: ")




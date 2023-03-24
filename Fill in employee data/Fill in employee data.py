# ---------------------------
# -- Fill in employee data --
# --------------------------- 

# Bu satır, dosya yoksa bir veri dosyası oluşturmak için yazılmıştır.
file_open = open("employeedata.txt", "a")
file_open.close()


def Add_employees():  # 1
    file_ID = open("employeedata.txt", "r")
    file_ID_list = file_ID.readlines()
    file_ID.close()

    while True:
        Employee_id = input("- Please enter the employee number (ID): ")
        if f"- Employee number (ID): {Employee_id}\n" in file_ID_list:
            print("There is an employee with this number, please choose another number..")
        else:
            break

    print(Employee_id)
    First_Name = input("- Please enter the first name: ")
    print(First_Name.capitalize())
    last_name = input("- Please enter the last name: ")
    print(last_name.capitalize())
    Salary = input("- Please enter employee salary: ")
    print(Salary)
    absence_days = input("- Please enter the number of days of absence: ")
    if absence_days == "0":
        print(absence_days)
    else:
        old_salary = Salary
        absence_days_int = int(absence_days)
        Discount = absence_days_int*150
        salary_int = int(Salary)
        New_salary = salary_int - Discount
        Salary = str(New_salary)
        print(absence_days)
        print("--------------------")
        print(f"> Salary before discount = {old_salary}")
        print(f"> Salary after discount = {New_salary}")
    Incentives = "No incentives"

    print("--------------------")

    data = [f"- Employee number (ID): {Employee_id}\n",
            f"- First Name: {First_Name.capitalize()}\n",
            f"- last name: {last_name.capitalize()}\n",
            f"- Salary: {Salary}\n",
            f"- Number of employee absence days: {absence_days}\n",
            f"- Incentives: {Incentives}\n"]

    bos = []

    file_b = open("employeedata.txt", "r")
    file_data_b_r = file_b.readlines()
    file_b.close()

    if file_data_b_r == ['All data has been deleted by the user..!!']:
        file_b_w = open("employeedata.txt", "w")
        file_b_w.writelines(bos)
        file_b_w.close()

    file_r = open("employeedata.txt", "r")
    file_data_r = file_r.readlines()
    file_r.close()

    if file_data_r == []:
        file_w = open("employeedata.txt", "a")
        file_w.write("------------------------------------------\n")
        file_w.close()
    elif file_data_b_r[0] != "------------------------------------------\n":
        file_b_w2 = open("employeedata.txt", "w")
        file_b_w2.write("------------------------------------------\n")
        file_b_w2.close()

    file = open("employeedata.txt", "a")
    file.writelines(data)
    file.write("------------------------------------------\n")
    file.close()


def Edit_employees():  # 2
    file_edit = open("employeedata.txt", "r")
    edit_list = file_edit.readlines()
    file_edit.close()

    while True:
        print("You want to edit what?")
        print("- To edit the employee number (ID) [1]")
        print("- To edit the first name [2]")
        print("- To edit the last name [3]")
        print("- To edit salary [4]")
        print("- To edit the days of absence [5]")
        edit = input("> Choose: ")
        print("--------------------")
        if edit == "1" or edit == "2" or edit == "3" or edit == "4" or edit == "5":
            break
        else:
            print("Please choose a valid operation number")
            print("--------------------")

    while True:
        emp_num = input(
            "- Enter the number of the employee (ID) whose data you want to edit: ")
        if f"- Employee number (ID): {emp_num}\n" in edit_list:
            index_edit = edit_list.index(
                f"- Employee number (ID): {emp_num}\n")
            print("--------------------")
            print("> Searching for employee data....")
            print("--------------------")
            break
        else:
            print(
                "There is no employee with this ID, please enter the number of another employee")

    if edit == "1":  # ID
        while True:
            new_id = input("- Enter the new employee number (ID): ")
            if new_id == emp_num:
                break
            elif f"- Employee number (ID): {new_id}\n" in edit_list:
                print(
                    "There is an employee with this number, please choose another number..")
            else:
                break
        edit_list[index_edit] = f"- Employee number (ID): {new_id}\n"
        print("--------------------")
        print("The data has been edited, you can check..!")
        print(f"- Old employee number (ID) => {emp_num}")
        print(f"- New employee number (ID) => {new_id}")
        print("--------------------")
    elif edit == "2":  # First name
        old_name = edit_list[index_edit+1][14:]
        new_name = input("- Enter the new first name: ")
        edit_list[index_edit+1] = f"- First Name: {new_name.capitalize()}\n"
        new2_name = edit_list[index_edit+1][14:]
        print("--------------------")
        print("The data has been edited, you can check..!")
        print(f"- Old first name => {old_name}", end="")
        print(f"- New first name => {new2_name}", end="")
        print("--------------------")
    elif edit == "3":  # last name
        old_lname = edit_list[index_edit+2][13:]
        new_lname = input("- Enter the new last name: ")
        edit_list[index_edit+2] = f"- last Name: {new_lname.capitalize()}\n"
        new2_lname = edit_list[index_edit+2][13:]
        print("--------------------")
        print("The data has been edited, you can check..!")
        print(f"- Old last name => {old_lname}", end="")
        print(f"- New last name => {new2_lname}", end="")
        print("--------------------")
    elif edit == "4":  # Salary
        o_salary = edit_list[index_edit+3][10:]
        n_salary = input("- Enter the new salary: ")
        edit_list[index_edit+3] = f"- Salary: {n_salary}\n"
        new2_salary = edit_list[index_edit+3][10:]
        print("--------------------")
        print("The data has been edited, you can check..!")
        print(f"- Old Salary => {o_salary}", end="")
        print(f"- New Salary => {new2_salary}", end="")
        print("--------------------")
    elif edit == "5":  # days of absence
        absence_int = int(edit_list[index_edit+4][35:])
        o_absence = absence_int
        salary_int_2 = int(edit_list[index_edit+3][10:])
        print("Do you want to add days or delete days?")
        print("- For add days of absence [1]")
        print("- For delete days of absence [2]")
        print("# Note:")
        print("- The salary will be adjusted based on the days of absence")
        while True:
            day_op = input("> Select: ")
            print("--------------------")
            if day_op == "1":  # For add
                add_absence = int(
                    input("- Enter the number of absence days you want to add: "))
                n_absence = absence_int + add_absence
                edit_list[index_edit +
                          4] = f"- Number of employee absence days: {n_absence}\n"
                print("--------------------")
                print("The data has been edited, you can check..!")
                print(
                    f"- The number of old days of absence => {o_absence}")
                print(
                    f"- The number of new days of absence => {n_absence}")
                print("--------------------")
                print("(Salary after the new discount)")
                discoun = add_absence*150
                ne_salary = salary_int_2 - discoun
                edit_list[index_edit+3] = f"- Salary: {ne_salary}\n"
                print(
                    f"- Old salary => {salary_int_2}")
                print(f"- New salary => {ne_salary}")
                print(f"{discoun} deducted from salary..")
                print("--------------------")
                break
            elif day_op == "2":  # For delete
                while True:
                    delet_absence = int(
                        input("- Enter the number of absence days you want to delete: "))
                    n_absence_d = absence_int - delet_absence
                    if n_absence_d >= 0:
                        break
                    else:
                        print(
                            f"{absence_int} - {delet_absence} = ({n_absence_d})")
                        print(
                            "The number of absence days has become negative and this is an error, please try again..!")
                edit_list[index_edit +
                          4] = f"- Number of employee absence days: {n_absence_d}\n"
                print("--------------------")
                print("The data has been edited, you can check..!")
                print(
                    f"- The number of old days of absence => {o_absence}")
                print(
                    f"- The number of new days of absence => {n_absence_d}")
                print("--------------------")
                print("(New salary adjustment)")
                f_add_ = delet_absence*150
                ne_salary_a = salary_int_2 + f_add_
                edit_list[index_edit+3] = f"- Salary: {ne_salary_a}\n"
                print(f"- Old salary => {salary_int_2}")
                print(f"- New salary => {ne_salary_a}")
                print(f"{f_add_} has been added to the salary..")
                print("--------------------")
                break
            else:
                print("Wrong choice, please select 1 or 2..")

    file_edit_p = open("employeedata.txt", "w")
    file_edit_p.writelines(edit_list)
    file_edit_p.close()

    print()
    print("(Printing new employee data..)")
    print(edit_list[index_edit-1], end="")
    print(edit_list[index_edit], end="")
    print(edit_list[index_edit+1], end="")
    print(edit_list[index_edit+2], end="")
    print(edit_list[index_edit+3], end="")
    print(edit_list[index_edit+4], end="")
    print(edit_list[index_edit+5], end="")
    print(edit_list[index_edit+6], end="")
    print()


def Delete_employee():  # 3
    file_delet = open("employeedata.txt", "r")
    delet_list = file_delet.readlines()
    file_delet.close()

    while True:
        id_delet = input(
            "- Please enter the employee number (ID) you want to delete: ")

        if f"- Employee number (ID): {id_delet}\n" in delet_list:
            index_delet = delet_list.index(
                f"- Employee number (ID): {id_delet}\n")
            print("--------------------")
            print("Employee data is being deleted..")
            print("--------------------")
            delet_list.pop(index_delet+6)
            delet_list.pop(index_delet+5)
            delet_list.pop(index_delet+4)
            delet_list.pop(index_delet+3)
            delet_list.pop(index_delet+2)
            delet_list.pop(index_delet+1)
            delet_list.pop(index_delet)
            print("The employee's data has been deleted, you can check..!")
            print("--------------------")
            break
        else:
            print(
                "There is no employee with this ID, please enter the number of another employee")

    file_delet_p = open("employeedata.txt", "w")
    file_delet_p.writelines(delet_list)
    file_delet_p.close()


def incentives_for_employees():  # 4
    file_incentives = open("employeedata.txt", "r")
    incentives_list = file_incentives.readlines()
    file_incentives.close()

    data = {}
    key = 0

    while True:  # For ID
        empl_num = input(
            "- Enter the number of the employee (ID) you want to add incentives to: ")
        if f"- Employee number (ID): {empl_num}\n" in incentives_list:
            index_add = incentives_list.index(
                f"- Employee number (ID): {empl_num}\n")
            print("--------------------")
            print("Searching for employee data....")
            print("--------------------")
            break
        else:
            print(
                "There is no employee with this ID, please enter the number of another employee")

    salary_a = 0

    while True:
        print("Choose the incentives you want to add to the employee:-")
        print("- Increase the salary [1]")
        print("- Add vacation days [2]")
        print("- other [3]")
        add_in = input("> Choose: ")
        print("--------------------")

        if add_in == "1":  # Increase the salary
            ad_salary = int(
                input("- How much do you want to add to the salary: "))
            old_salary = int(incentives_list[index_add+3][10:])
            new_salary = old_salary + ad_salary
            incentives_list[index_add+3] = f"- Salary: {new_salary}\n"
            salary_a += ad_salary
            print("--------------------")
            print("(New salary after adding incentive)")
            print(f"- Old Salary => {old_salary}")
            print(f"- New Salary => {new_salary}")
            print(f"{ad_salary} was added to the salary as an incentive.")
            print("--------------------")
            print("Do you want to add another incentive?")
            print("Yes [1]")
            print("No [2]")
            cont = input("> Choose: ")
            print("--------------------")
            if cont == "2":
                break
        if add_in == "2":  # Add vacation days
            key += 1
            days = int(
                input("- How many vacation days do you want to add to the employee: "))
            days_vac = f"{days} #"
            data[key] = days_vac
            print("--------------------")
            print("Do you want to add another incentive?")
            print("Yes [1]")
            print("No [2]")
            cont = input("> Choose: ")
            print("--------------------")
            if cont == "2":
                break
        if add_in == "3":  # other
            key += 1
            print("What incentive do you want to add?")
            other_inc = input("> Please write the incentive: ")
            data[key] = other_inc
            print("--------------------")
            print("Do you want to add another incentive?")
            print("Yes [1]")
            print("No [2]")
            cont = input("> Choose: ")
            print("--------------------")
            if cont == "2":
                break
        else:
            print("Wrong choice, please choose from the available operations..")
            print("--------------------")

    days_l = []
    other_l = []
    for i in data:
        if "#" in data[i]:
            days_l.append(int(data[i][0:-1]))
        else:
            other_l.append(data[i])

    num_day = 0
    for i in days_l:
        num_day += i

    day_add = f"{num_day} days vacation"
    other_add = f'{" + ".join(other_l)}'

    if salary_a == 0:
        if days_l == [] and other_l != []:
            incentives_list[index_add+5] = f"- Incentives: {other_add}\n"
            print("Incentives added:-")
            print(f"- {other_add}")
            print("--------------------")
        elif other_l == [] and days_l != []:
            incentives_list[index_add+5] = f"- Incentives: {day_add}\n"
            print("Incentives added:-")
            print(f"- {day_add}")
            print("--------------------")
        elif other_l != [] and days_l != []:
            incentives_list[index_add +
                            5] = f"- Incentives: {day_add} + {other_add}\n"
            print("Incentives added:-")
            print(f"- {day_add}")
            print(f"- {other_add}")
            print("--------------------")
        else:
            noth = 0
    elif salary_a > 0:
        if days_l == [] and other_l != []:
            incentives_list[index_add +
                            5] = f"- Incentives: {salary_a} salary increase + {other_add}\n"
            print("Incentives added:-")
            print(f"- {salary_a} salary increase")
            print(f"- {other_add}")
            print("--------------------")
        elif other_l == [] and days_l != []:
            incentives_list[index_add +
                            5] = f"- Incentives: {salary_a} salary increase + {day_add}\n"
            print("Incentives added:-")
            print(f"- {salary_a} salary increase")
            print(f"- {day_add}")
            print("--------------------")
        elif other_l != [] and days_l != []:
            incentives_list[index_add +
                            5] = f"- Incentives: {salary_a} salary increase + {day_add} + {other_add}\n"
            print("Incentives added:-")
            print(f"- {salary_a} salary increase")
            print(f"- {day_add}")
            print(f"- {other_add}")
            print("--------------------")
        else:
            incentives_list[index_add +
                            5] = f"- Incentives: {salary_a} salary increase \n"
            print("Incentives added:-")
            print(f"- {salary_a} salary increase")
            print("--------------------")

    file_print = open("employeedata.txt", "w")
    file_print.writelines(incentives_list)
    file_print.close()


def Add_deduction_Salary():  # 5
    file = open("employeedata.txt", "r")
    a_d_list = file.readlines()
    file.close()

    print("Do you want to add or discount the salary?")
    print("- For add [1]")
    print("- For discount [2]")
    while True:
        a_d = input("> Choose: ")
        print("--------------------")
        if a_d == "1" or a_d == "2":
            break
        else:
            print("Please choose a valid operation number 1 or 2..!!")
            print("--------------------")

    while True:  # For ID
        emplo_num = input(
            "- Enter the number of the employee (ID) whose salary you want to edit: ")
        if f"- Employee number (ID): {emplo_num}\n" in a_d_list:
            index_dis = a_d_list.index(
                f"- Employee number (ID): {emplo_num}\n")
            print("--------------------")
            print("Searching for employee data....")
            print("--------------------")
            break
        else:
            print(
                "There is no employee with this ID, please enter the number of another employee")

    Salary_Old = int(a_d_list[index_dis+3][10:])
    if a_d == "1":  # For add
        while True:
            add = int(
                input("- How much do you want to add to the employee's salary: "))
            Salary_New_a = Salary_Old + add
            if Salary_New_a >= 0:
                break
            else:
                print("--------------------")
                print(f"{Salary_Old} + {add} = ({Salary_New_a})")
                print("Salary value cannot be negative, please try again..!")
                print("--------------------")

        a_d_list[index_dis+3] = f"- Salary: {Salary_New_a}\n"
        print("--------------------")
        print(f"Salary before adding => {Salary_Old}")
        print(f"Salary after adding => {Salary_New_a}")
        print(f"> {add} has been added to the salary..")
        print("--------------------")
    elif a_d == "2":  # For discount
        while True:
            dis = int(
                input("- How much do you want to deduct from the employee's salary: "))
            Salary_New_d = Salary_Old - dis
            if Salary_New_d >= 0:
                break
            else:
                print("--------------------")
                print(f"{Salary_Old} - {dis} = ({Salary_New_d})")
                print("Salary value cannot be negative, please try again..!")
                print("--------------------")

        a_d_list[index_dis+3] = f"- Salary: {Salary_New_d}\n"
        print("--------------------")
        print(f"Salary before discount => {Salary_Old}")
        print(f"Salary after discount => {Salary_New_d}")
        print(f"> {dis} has been deducted from the salary..")
        print("--------------------")

    file_a_d_p = open("employeedata.txt", "w")
    file_a_d_p.writelines(a_d_list)
    file_a_d_p.close()


def Searching_for_employee():  # 6
    file = open("employeedata.txt", "r")
    list_print = file.readlines()
    file.close()
    while True:
        employee_num = input(
            "- Please enter the employee number (ID) you want to search for: ")
        if f"- Employee number (ID): {employee_num}\n" in list_print:
            num_index = list_print.index(
                f"- Employee number (ID): {employee_num}\n")
            print()
            print(list_print[num_index-1], end="")
            print(list_print[num_index], end="")
            print(list_print[num_index+1], end="")
            print(list_print[num_index+2], end="")
            print(list_print[num_index+3], end="")
            print(list_print[num_index+4], end="")
            print(list_print[num_index+5], end="")
            print(list_print[num_index+6], end="")
            print()
            break
        else:
            print(
                "There is no employee with this ID, please enter the number of another employee")


def View_all_data():  # 7
    file = open("employeedata.txt", "r")
    emp_list = file.readlines()
    file.close()

    if emp_list == []:
        print("--------------------")
        print("This file is empty..")
        print("--------------------")
    else:
        file = open("employeedata.txt", "r")
        print("--------------------\n")
        print(file.read())
        print("--------------------")
        file.close()


def Clear_all_library_data():  # 8
    file = open("employeedata.txt", "w")
    file.write("All data has been deleted by the user..!!")
    file.close()
    print("The data has been deleted, you can check..!")


## WorkSpace ##

print("""---------Welcome to the workers library---------
# This library is programmed to display workers data
# You can add, edit and view the data in this library
-------------------------------------------------
# Notes:-
- Please save the employee's number (ID) because it will be used to search for him, modify his data and delete it.
- 150 will be deducted from the salary for each day of absence.
-------------------------------------------------""")

while(True):
    print("Available operations:-")
    print("- Add employees [1]")
    print("- Edit employees [2]")
    print("- Delete employees [3]")
    print("- Add incentives for employee [4]")
    print("- Add, deduction for employee salary [5]")
    print("- Searching for employee [By employee number (ID)] [6]")
    print("- View all data [7]")
    print("- Delete all library data [8]")
    print("- Exit [9]")
    print("--------------------")
    operation = int(input("> Choose a operation: "))

    if operation == 1:  # Add employees
        print("--------------------")
        while True:
            Add_employees()
            print("Do you want to add another employee?")
            print("- Yes [1]")
            print("- No [2]")
            con = input("> Select:")
            print("--------------------")
            if con == "1":
                None
            else:
                break

    elif operation == 2:  # Edit employees
        print("--------------------")
        while True:
            Edit_employees()
            print("Do you want to edit another employee?")
            print("- Yes [1]")
            print("- No [2]")
            con = input("> Select:")
            print("--------------------")
            if con == "1":
                None
            else:
                break

    elif operation == 3:  # Delete employees
        print("--------------------")
        while True:
            Delete_employee()
            print("Do you want to delete another employee?")
            print("- Yes [1]")
            print("- No [2]")
            con = input("> Select:")
            print("--------------------")
            if con == "1":
                None
            else:
                break

    elif operation == 4:  # Add incentives for employee
        print("--------------------")
        while True:
            incentives_for_employees()
            print("Do you want to add incentives to another employee?")
            print("- Yes [1]")
            print("- No [2]")
            con = input("> Select:")
            print("--------------------")
            if con == "1":
                None
            else:
                break

    elif operation == 5:  # Add deduction Salary
        print("--------------------")
        while True:
            Add_deduction_Salary()
            print("Do you want to add or deduct the salary of another employee?")
            print("- Yes [1]")
            print("- No [2]")
            con = input("> Select:")
            print("--------------------")
            if con == "1":
                None
            else:
                break

    elif operation == 6:  # Searching for employee [By employee number
        print("--------------------")
        while True:
            Searching_for_employee()
            print("Do you want to Search another employee?")
            print("- Yes [1]")
            print("- No [2]")
            con = input("> Select:")
            print("--------------------")
            if con == "1":
                None
            else:
                break

    elif operation == 7:  # View all data
        while True:
            View_all_data()
            print("Do you want to view the data again?")
            print("- Yes [1]")
            print("- No [2]")
            con = input("> Select:")
            if con == "1":
                None
            else:
                print("--------------------")
                break

    elif operation == 8:  # Clear all library data
        print("--------------------")
        Clear_all_library_data()
        print("--------------------")
        print("Do you want to exit or continue?")
        print("- For Exit [1]")
        print("- For continue [2]")
        con = input("> Select:")
        if con == "1":
            print("--------------------")
            print("Thank you..")
            print("--------------------")
            exit()
        print("--------------------")

    elif operation == 9:  # Exit
        print("--------------------")
        print("Thank you..")
        print("--------------------")
        exit()

    else:
        print("--------------------")
        print("Wrong entry, please choose from the available operations only..!")
        print("--------------------")

# Fill in employee data (Python)
With this automation, employee data is fully recorded and controlled.

When you run the code, a file named "employeedata.txt" is automatically created in which employee data is saved. When you add employee data, this data is added to this file. When modifying or deleting employee data, these changes are also made inside the file, and you can access the file whenever you want.

**Nots:-**
1. Please save the employee's number (ID) because it will be used to search for him, modify his data and delete it.
2. 150 will be deducted from the salary for each day of absence.
3. The "employeedata.txt" file is created in the same path where the code is located, and as we mentioned earlier, it is created automatically

### Functions description:-
- Add_employees()
> This function is used to fill in the employee's data in the (list) and print it to the file, and 150 deductions are made from the salary for each Absence day.

> The function does not allow the use of a pre-existing employee number (ID)

> This function also examines the linked file and makes sure it does not contain junk data and deletes it if it does.

- Edit_employees()
> This function is used to change personnel data.

> When the employee number is changed, the use of an employee number that is already in use will not be allowed.

> When changing the days of absence, if the days of absence are added, 150 deductions are made for each additional day, and if the days of absence are deleted, 150 salaries are returned for each deleted day.

> when you finish using the function, the new employee data is printed.

- Delete_employee()
> This function is used to delete a specific employee's data by employee number (ID).

- incentives_for_employees()
> This function is used to add incentives to employees and available incentives (salary increase - holidays) and the function provides another option to add other incentives by the user.

> the function stores the incentive data in a type (Dictionary) variable and then processes it correctly and then prints the incentives for the specified employee into the file.

> In case of salary increase, the determined amount will be automatically added to the salary.

> the added incentives will be printed after the use of the function is completed.

- Add_deduction_Salary()
> This function is used to make deductions and additions from the employee's salary.

> In case of deduction from the salary, if the salary is negative, the deduction will not be accepted as the salary cannot be negative.

- Searching_for_employee()
> This function is used to search for a specific employee with (ID) and the employee's data is printed on the screen.

- View_all_data()
> Although you can see the employee data in the file, this function allows you to print all the file data to the screen, and if the file is empty, it tells you that the file is empty.

- Clear_all_library_data()
> This function is used to completely delete all employee data and a message is added to the file that the data has been deleted by the user, and if you want to add employees again, don't worry, the attached message will be deleted automatically and the employees will be added without any problems.


## Information about the file:-
- **Code Type:** Assignment for AVP-2 course at Necmettin Erbakan University
- **Date of writing the code:** 11/06/2022
- **The language of the text inside the code:** English


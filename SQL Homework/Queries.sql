--Data Analysis

-- 1. List the following details of each employee: 
--    employee number, last name, first name, gender, and salary.
SELECT 
	EE.emp_no,
	EE.last_name,
	EE.first_name,
	EE.gender,
	Sal.salary
FROM "Employees" AS EE
JOIN "Salaries" AS Sal
	ON EE.emp_no = Sal.emp_no;

-- 2.List employees who were hired in 1986.
SELECT 
	first_name, 
	last_name, 
	hire_date 
FROM "Employees"
	WHERE hire_date >= '1986-01-01' 
	AND hire_date <='1987-01-01';


-- 3. List the manager of each department with the following information: 
--    department number, department name, the manager's employee number, last name, first name, 
--    and start and end employment dates.
SELECT 
	D.dept_no,
	D.dept_name,
	DM.emp_no,
	EE.last_name,
	EE.first_name,
	DM.from_date,
	DM.to_date
FROM "Departments" AS D
JOIN "Department_Manager" AS DM
	ON D.dept_no = DM.dept_no
JOIN "Employees" As EE
	ON EE.emp_no = DM.emp_no;

-- 4. List the department of each employee with the following information:
--    employee number, last name, first name, and department name.
SELECT 
	DE.emp_no,
	EE.last_name,
	EE.first_name,
	D.dept_name
FROM "Department_Employee" AS DE
JOIN "Departments" AS D
	ON D.dept_no = DE.dept_no
JOIN "Employees" As EE
	ON EE.emp_no = DE.emp_no;

-- 5. List all employees whose first name is "Hercules" and last names begin with "B."
SELECT 
	first_name, 
	last_name	
FROM "Employees"
	WHERE first_name = 'Hercules' 
	AND last_name LIKE 'B%';

-- 6. List all employees in the Sales department, including their 
--    employee number, last name, first name, and department name.
SELECT 
	DE.emp_no,
	EE.last_name,
	EE.first_name,
	D.dept_name
FROM "Department_Employee" AS DE
JOIN "Departments" AS D
	ON D.dept_no = DE.dept_no
JOIN "Employees" As EE
	ON EE.emp_no = DE.emp_no
	WHERE D.dept_name = 'Sales';

-- 7. List all employees in the Sales and Development departments, including their
--    employee number, last name, first name, and department name.
SELECT 
	DE.emp_no,
	EE.last_name,
	EE.first_name,
	D.dept_name
FROM "Department_Employee" AS DE
JOIN "Departments" AS D
	ON D.dept_no = DE.dept_no
JOIN "Employees" As EE
	ON EE.emp_no = DE.emp_no
	WHERE 
		D.dept_name = 'Sales'
		OR D.dept_name = 'Development';

-- 8. In descending order, list the frequency count of employee last names,
--     i.e., how many employees share each last name.
SELECT 
	last_name,
	COUNT(last_name) AS "Frequency"
FROM "Employees"
GROUP BY last_name
ORDER BY COUNT(last_name) DESC;
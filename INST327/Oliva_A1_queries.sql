/*Answer 1*/
USE ischool;
SELECT person_id,lname, fname, pronoun_id, email, college, department, title, start_date
FROM people
ORDER BY lname, fname;

/*Answer 2*/
USE ischool;
SELECT CONCAT(fname, ' ', lname) AS "Full Name", Email, Title, start_date AS "Start Date" 
FROM people
ORDER BY -start_date;

/*Answer 3*/
USE ischool;
SELECT address_id AS "Adress" , Street, City, State, Zipcode, Country
FROM addresses
WHERE country  >= 'A' and country < 'D'
ORDER BY country;












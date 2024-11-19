/* Answer 1 */
USE ischool;

SELECT 
    L.building_name,
    CONCAT(P.lname, ', ', P.fname) AS Instructor, 
    COUNT(CS.course_id) AS course_count
FROM 
    locations L
JOIN 
    course_sections CS ON L.location_id = CS.location_id
LEFT JOIN 
    people P ON CS.instructor_id = P.person_id
WHERE 
    P.person_id IS NOT NULL
GROUP BY 
    L.building_name, 
    P.lname, 
    P.fname

UNION ALL

SELECT 
    L.building_name,
    NULL AS Instructor,
    COUNT(CS.course_id) AS total_course_count
FROM 
    locations L
JOIN 
    course_sections CS ON L.location_id = CS.location_id
JOIN 
    people P ON CS.instructor_id = P.person_id
GROUP BY 
    L.building_name

UNION ALL

SELECT 
    NULL AS building_name,
    NULL AS Instructor,
    COUNT(DISTINCT CS.instructor_id) AS total_course_count
FROM 
    course_sections CS

ORDER BY 
    CASE 
        WHEN building_name IS NULL AND Instructor IS NULL THEN 1 
        ELSE 0 
    END,
    building_name,
    CASE 
        WHEN Instructor IS NULL THEN 1 
        ELSE 0 
    END,
    Instructor;

    
/* Answer 2 */
USE ischool;

SELECT 
    a.zipcode, 
    a.country, 
    COUNT(DISTINCT a.address_id) AS num_address
FROM 
    addresses a
JOIN 
    person_addresses pa ON a.address_id = pa.address_id
JOIN 
    people p ON pa.person_id = p.person_id
WHERE 
    a.zipcode REGEXP '^[0-9-]+$' 
    AND a.zipcode != '0'
GROUP BY 
    a.zipcode, 
    a.country
ORDER BY 
    num_address DESC;

/* Answer 3 */
USE ischool;

SELECT 
    p.person_id, 
    CONCAT(p.lname, ', ', p.fname) AS Full_Name, 
    COUNT(e.section_id) AS num_courses
FROM 
    people p
JOIN 
    enrollments e ON p.person_id = e.person_id
JOIN 
    course_sections cs ON e.section_id = cs.section_id
WHERE 
    cs.year = 2021 
    OR cs.year = 2022
GROUP BY 
    p.person_id, 
    p.fname, 
    p.lname
ORDER BY 
    num_courses DESC, 
    p.lname, 
    p.fname;


/* Answer 4 */
USE ischool;

WITH CourseCount AS (
    SELECT 
        p.person_id, 
        p.fname, 
        p.lname, 
        COUNT(e.section_id) AS num_courses
    FROM 
        people p
    JOIN 
        enrollments e ON p.person_id = e.person_id
    JOIN 
        course_sections cs ON e.section_id = cs.section_id
    WHERE 
        cs.year = 2021 
        OR cs.year = 2022
    GROUP BY 
        p.person_id, 
        p.fname, 
        p.lname
)
SELECT 
    person_id, 
    CONCAT(lname, ', ', fname) AS Full_Name, 
    num_courses
FROM 
    CourseCount
ORDER BY 
    num_courses DESC, 
    lname, 
    fname;



/* A common table expression (CTE) is written with the "WITH" keyword,
 which makes a query easier to read and manage by breaking it into parts with clear names.
 This would be more beneficial when managing complex queries and making changes in the future .
 A subquery is included directly within the main query, which can be simpler but harder to follow
 if it gets too jumbled and complex. I chose a CTE  because it keeps the query clear and easy to adjust.
 Even though a subquery would also work, a CTE is just better for any future changes. */
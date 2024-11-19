/* View 1 */
CREATE VIEW collisions_manhattan_2024 AS
SELECT 
    c.collision_id, 
    c.crash_date, 
    c.crash_time, 
    c.location_id, 
    l.borough, 
    l.on_street_name, 
    l.cross_street_name, 
    l.off_street_name, 
    c.number_of_persons_injured, 
    c.number_of_persons_killed
FROM 
    Collision c
JOIN 
    Location l ON c.location_id = l.location_id
WHERE 
    l.borough = 'Manhattan' 
    AND YEAR(c.crash_date) = 2024;

/* View 2 */
DROP VIEW IF EXISTS Borough_Time_of_Day_Impact;
CREATE VIEW Borough_Time_of_Day_Impact AS
SELECT l.borough,
       CASE
           WHEN HOUR(c.crash_time) BETWEEN 0 AND 6 THEN 'Night'
          WHEN HOUR(c.crash_time) BETWEEN 7 AND 12 THEN 'Morning'
           WHEN HOUR(c.crash_time) BETWEEN 13 AND 18 THEN 'Afternoon'
           ELSE 'Evening'
       END AS time_of_day,
       COUNT(c.collision_id) AS total_collisions,
       SUM(c.number_of_persons_injured + c.number_of_persons_killed +
           c.number_of_pedestrians_injured + c.number_of_pedestrians_killed +
           c.number_of_cyclists_injured + c.number_of_cyclists_killed +
           c.number_of_motorists_injured + c.number_of_motorists_killed) AS total_casualties,
       AVG(c.number_of_persons_injured + c.number_of_persons_killed +
           c.number_of_pedestrians_injured + c.number_of_pedestrians_killed +
           c.number_of_cyclists_injured + c.number_of_cyclists_killed +
           c.number_of_motorists_injured + c.number_of_motorists_killed) AS avg_casualties_per_collision
FROM Collision c
JOIN Location l ON c.location_id = l.location_id
GROUP BY l.borough, time_of_day
ORDER BY l.borough, avg_casualties_per_collision DESC;
SELECT * FROM Borough_Time_of_Day_Impact;

/* View 3 */
DROP VIEW IF EXISTS holiday_collisions;
CREATE VIEW holiday_collisions AS
SELECT c.collision_id, c.crash_date, c.crash_time, l.borough,
       c.number_of_persons_injured, c.number_of_persons_killed
FROM collision c
JOIN location l ON c.location_id = l.location_id
WHERE c.crash_date IN ('2024-01-01', '2024-01-15', '2024-05-27', '2024-06-19',
                       '2024-07-04', '2024-09-02', '2024-10-14', '2024-11-11',
                       '2024-11-28', '2024-11-29','2024-12-25');
SELECT * FROM holiday_collisions;

/* View 4 */
DROP VIEW IF EXISTS borough_fatality_rate;
CREATE VIEW borough_fatality_rate AS
SELECT l.borough, COUNT(c.collision_id) AS total_collisions,
       SUM(c.number_of_persons_killed) AS total_fatalities,
 (SUM(c.number_of_persons_killed) / COUNT(c.collision_id)) AS fatality_rate
FROM collision c
JOIN location l ON c.location_id = l.location_id
GROUP BY l.borough
ORDER BY fatality_rate DESC;
SELECT * FROM borough_fatality_rate;

/* View 5 */
CREATE VIEW collisions_by_borough_date AS
SELECT borough, crash_date, COUNT(collision_id) AS TotalCollisions
FROM collision 
JOIN location USING(location_id)
GROUP BY borough, crash_date
ORDER BY TotalCollisions DESC;

/* View 6 */
CREATE VIEW collisions_per_street AS
SELECT 
    main_street_name,
    (SELECT COUNT(*) 
     FROM collision 
     WHERE on_street_name = main_street_name OR cross_street_name = main_street_name 
     OR off_street_name = main_street_name) AS total_collisions,
    SUM(number_of_persons_injured) AS total_injuries
FROM 
    (SELECT on_street_name AS main_street_name FROM collision
     UNION
     SELECT cross_street_name FROM collision
     UNION
     SELECT off_street_name FROM collision) AS streets
JOIN 
    collision ON streets.main_street_name 
    IN (collision.on_street_name, collision.cross_street_name, collision.off_street_name)
GROUP BY 
    main_street_name



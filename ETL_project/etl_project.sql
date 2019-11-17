CREATE TABLE fitness_sleep(
	date date PRIMARY KEY,
	step_count int,
	mood int,
	calories_burned int,
	hours_of_sleep int,
	weight_lb float
);

CREATE TABLE moon_phases(
	id INT PRIMARY KEY,
	Date date,
	Moon_Phase varchar
);


SELECT * from fitness_sleep;
SELECT * from moon_phases;

--Frequency of moon phases during the time period 	
SELECT moon_phase, count(moon_phase) as moon_phase_count
FROM moon_phases
GROUP BY moon_phase;

-- Average amount of sleep and average mood overall
--sad:100
--neutral:200
--happy: 300
SELECT AVG(hours_of_sleep) as avg_amount_sleep, AVG(mood) as average_mood
FROM fitness_sleep; 


-- The frequency of the amount of night the individual recieved per night
SELECT hours_of_sleep, count(hours_of_sleep) as count_of_hours_sleep
FROM fitness_sleep
GROUP BY hours_of_sleep
ORDER BY hours_of_sleep ASC;

-- The frequency of the person's mood
SELECT mood, count(mood) as count_of_mood
FROM fitness_sleep
GROUP BY mood;

-- Join tables to show moon phases ordered by hours of sleep
SELECT fitness_sleep.date, hours_of_sleep, Moon_Phase
FROM fitness_sleep
	INNER JOIN moon_phases
		on fitness_sleep.date = moon_phases.date
	ORDER BY hours_of_sleep;
-- Moon phases and Mood of each date 
SELECT fitness_sleep.date, moon_phases, mood, hours_of_sleep
FROM fitness_sleep
	INNER JOIN moon_phases
		on fitness_sleep.date = moon_phases.date;

--grouping by mood to observe moon phases for each mood
SELECT mood, moon_phase
FROM fitness_sleep
INNER JOIN moon_phases
		on fitness_sleep.date = moon_phases.date
order by mood DESC;

-- Maximum amount of hours of sleep, minimum hours of sleep and their moon phases
SELECT MAX(hours_of_sleep) as max_sleep, MIN(hours_of_sleep) as min_sleep, moon_phase
FROM fitness_sleep
	INNER JOIN moon_phases
		on fitness_sleep.date = moon_phases.date
group by moon_phase;



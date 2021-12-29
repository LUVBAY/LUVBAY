SELECT title

FROM movies

WHERE year = 2008; 

SELECT name

FROM people

JOIN directors ON directors.person_id = people.id

JOIN ratings ON directors.movie_id = ratings.movie_id

WHERE rating >= 9.0;

SELECT DISTINCT title

FROM people JOIN stars ON people.id = stars.person_id

JOIN movies ON movies.id = stars.movie_id

JOIN ratings ON ratings.movie_id = stars.movie_id

WHERE name = "Chadwick Boseman"

ORDER BY rating DESC

LIMIT 5;
 
SELECT title

FROM people JOIN stars ON stars.person_id = people.id

JOIN movies ON stars.movie_id = movies.id

WHERE name = "Johnny Depp"

AND movie_id IN (SELECT movie_id FROM people JOIN stars ON stars.person_id = people.id WHERE name = "Helena Bonham Carter"); 
 
SELECT DISTINCT name

FROM people JOIN stars ON stars.person_id = people.id

WHERE name != "Kevin Bacon"

AND movie_id IN (SELECT movie_id FROM people JOIN stars ON stars.person_id = people.id WHERE name = "Kevin Bacon" AND birth = 1958); 
 
SELECT birth

FROM people

WHERE name = "Emma Stone"; 
 
SELECT title

FROM movies

WHERE year >= 2018

ORDER BY title 

SELECT COUNT(*) as number_Of_Movies_With_Ratings_As10

FROM ratings

WHERE rating = 10.0 
 
SELECT title, year

FROM movies

WHERE title LIKE "Harry Potter%"

ORDER BY year; 

SELECT AVG(rating)

FROM ratings JOIN movies ON movies.id = ratings.movie_id

WHERE year = 2012; 
 
SELECT title, rating

FROM movies JOIN ratings ON movies.id = ratings.movie_id

WHERE year = 2010

ORDER BY rating DESC, title; 
 
SELECT name

FROM people JOIN stars ON people.id = stars.person_id

JOIN movies ON movies.id = stars.movie_id

WHERE title = "Toy Story"; 
 
SELECT DISTINCT name

FROM people JOIN stars ON people.id = stars.person_id

JOIN movies ON movies.id = stars.movie_id

WHERE year = 2004

ORDER BY birth;

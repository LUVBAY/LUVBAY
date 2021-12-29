The THIEF is: Ernest
The thief ESCAPED TO: London
The ACCOMPLICE is: Berthold
==============================================================================================================================================================================
-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT description
FROM crime_scene_reports
WHERE day = 28 AND month = 7 AND year = 2020 AND street = "Chamberlin Street";



SELECT transcript
FROM interviews
WHERE day = 28 AND month = 7 AND year = 2020 AND transcript LIKE "%courthouse%";




SELECT name
FROM people
JOIN courthouse_security_logs ON people.license_plate = courthouse_security_logs.license_plate
WHERE day = 28 AND month = 7 AND year = 2020 AND hour = 10 AND minute >= 15 AND minute < 25 AND activity = "exit";




SELECT DISTINCT name
FROM people
JOIN bank_accounts ON people.id = bank_accounts.person_id
JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE day = 28 AND year = 2020 AND month = 7 AND transaction_type = "withdraw" AND atm_location = "Fifer Street";




SELECT name
FROM people
JOIN passengers ON people.passport_number = passengers.passport_number
WHERE flight_id = (SELECT id FROM flights WHERE day = 29 AND month = 7 AND year = 2020 ORDER BY hour,minute LIMIT 1);




SELECT DISTINCT name
FROM people
JOIN phone_calls ON people.phone_number = phone_calls.caller
WHERE day = 28 AND month = 7 AND year = 2020 AND duration < 60;




SELECT city
FROM airports
WHERE id = (SELECT destination_airport_id FROM flights WHERE year = 2020 AND month = 7 AND day = 29 ORDER BY hour, minute LIMIT 1);




SELECT name
FROM people
JOIN phone_calls ON people.phone_number = phone_calls.receiver
WHERE day = 28 AND month = 7 AND duration < 60 AND caller = (SELECT phone_number FROM people WHERE name = "Ernest");

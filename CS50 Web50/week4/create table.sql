CREATE TABLE flights {
    id INTEGER PRIMARY KEY AUTOINCERMENT,
    oringin TEXT NOT NULL,
    destination TEXT NOT NULL,
    duration INTEGER NOT NULL
};

INSERT INTO flights
    (oringin, destination, duration)
    VALUES ("New York", "London", 415);

SELECT * FROM flights;

SElECT oringin, destination FROM flights;

SELECT * FROM WHERE id = 3;

SELECT * FROM flights where oringin = "New York";
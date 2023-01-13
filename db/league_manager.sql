DROP TABLE IF EXISTS leagues;
DROP TABLE IF EXISTS teams;


CREATE TABLE leagues (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE teams (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  leagues_id INT NOT NULL REFERENCES leagues(id),
  wins INT,
  losses INT,
  draws INT,
  score INT
);
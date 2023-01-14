DROP TABLE IF EXISTS leagues;
DROP TABLE IF EXISTS teams;
DROP TABLE IF EXISTS fixtures;


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

CREATE TABLE fixtures (
  id SERIAL PRIMARY KEY,
  round INT,
  team1_id INT NOT NULL REFERENCES teams(id),
  team2_id INT NOT NULL REFERENCES teams(id),
  team1score INT,
  team2score INT
);
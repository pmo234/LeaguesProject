DROP TABLE IF EXISTS leagues;
DROP TABLE IF EXISTS teams;

CREATE TABLE teams (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  wins INT,
  losses INT,
  draws INT,
  score INT
);

CREATE TABLE leagues (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  teams_id INT NOT NULL REFERENCES teams(id)
);

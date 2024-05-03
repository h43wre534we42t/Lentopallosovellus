CREATE TABLE courts (id SERIAL PRIMARY KEY, name TEXT, address TEXT);
CREATE TABLE reserved (id SERIAL PRIMARY KEY, res_date DATE, res_start TIME, res_end TIME, court_id INT, reservee TEXT);
CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT, password TEXT, is_admin BOOL)

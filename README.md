-App shows volleyball courts in the database
-You can add courts
-You can view reservations
-Adding reservations is not working

To use:
 - clone this repository
 - open terminal
 - cd Lentopallosovellus
 - python3 -m venv venv
 - source venv/bin/activate
 - flask, flask-sqlalchemy, psycopg2 and python-dotenv are needed and can be installed with pip install command
 - create .env file with "DATABASE_URL=postgresql:///user" with user as your own user
 - psql
 - CREATE TABLE courts (id SERIAL PRIMARY KEY, name TEXT, address TEXT);
 - CREATE TABLE reserved (id SERIAL PRIMARY KEY, res_date DATE, res_start TIME, res_end TIME, court_id INT, reservee TEXT);
 - \q
 - flask run

To test viewing reservations you can add some through the terminal manually, though the user interface is quite bad for now.




original idea:

    voi kirjautua sisään tai luoda käyttäjätunnuksen
    käyttäjä voi olla peruskäyttäjä tai ylläpitäjä
    voi nähdä listan paikoista missä voi pelaa lentopalloa
    ylläpitäjä voi lisätä paikkoja
    paikkoihin voi lisätä vuoroja sekä nähdä ketä niihin menee
    voi lisätä muita käyttäjiä kavereiksi ja muodostaa ryhmiä


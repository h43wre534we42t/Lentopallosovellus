-App shows volleyball courts in the database
-You can add courts
-You can view reservations
-Reserving courts for your group
-Creating account and logging in
-Creating groups and adding members

To use:
 -clone this repository
 - cd Lentopallosovellus
 - python3 -m venv venv
 - source venv/bin/activate
 - install requirements.txt
 - create .env file with "DATABASE_URL=postgresql:///user" with user as your own user and SECRET_KEY="something"
 - create tables from schema
 - flask run

This project simulates the relationships between Authors, Articles, and Magazines using Python and SQLite with raw SQL queries. It includes full CRUD functionality, relationship methods, and a structured, testable codebase.

Description
In this challenge, you'll work with three main entities:

Author: A writer who can write many articles.
Article: A piece written by an author and published in a magazine.
Magazine: A publication that contains many articles from various authors.
You’ll use raw SQL to manage these relationships through Python model classes and a SQLite database.

Technologies Used
Python 3.x
SQLite3
Raw SQL Queries
pytest for testing
Project Structure
articles_code_challenge/ │ ├── models/ │ ├── init.py │ ├── author.py │ ├── article.py │ └── magazine.py │ ├── db/ │ └── connection.py │ ├── tests/ │ ├── test_author.py │ ├── test_article.py │ └── test_magazine.py │ ├── seed.py ├── README.md └── requirements.txt

markdown Copy Edit

Features
Create, read, and manage authors, articles, and magazines
View all articles written by an author
List all contributors to a magazine
Retrieve all article titles in a magazine
Enforce data validation using property setters
Deliverables
Author class:

name property
articles() method
magazines() method
add_article(magazine, title) method
topic_areas() method
Article class:

title, author_id, magazine_id fields
author() and magazine() methods
Magazine class:

name, category properties
articles() and contributors() methods
article_titles() method
contributing_authors() method (only authors with >2 articles)
Running Tests
Make sure you have pytest installed:

pip install pytest
To run all tests:

bash
Copy
Edit
pytest
💾 Seeding the Database
Use the seed.py script to populate your database with initial data:

bash
Copy
Edit
python seed.py
🔧 Setup & Installation
Clone the repo:

bash
Copy
Edit
git clone https://github.com/MaginaBrian/articles-code-challenge.git
cd articles-code-challenge
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the seed file to initialize the database:

bash
Copy
Edit
python seed.py
Start exploring the models or running tests!

 Notes
All SQL operations are performed through raw queries — no ORM (like SQLAlchemy) is used.

Code is modular, testable, and follows Python best practices.

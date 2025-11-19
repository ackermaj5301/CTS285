# Flask Tutorial – CTS 285 Assignment

This folder contains my Flask tutorial application called Flaskr.
The goal of the assignment was to follow the official Flask documentation and build a working microblog.

---

## How to Run This Project

1. Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate

2. Install Flask:

pip install Flask

3. Set the Flask app environment variable:

export FLASK_APP=flaskr

4. Initialize the database:

flask init-db

You should see: "Initialized the database."

5. Run the Flask development server:

flask run

Then open the link that appears (usually http://127.0.0.1:5000).

---

## Features Implemented

- User registration
- User login and logout
- Create blog posts
- View all posts
- Edit existing posts
- Login required to create/edit posts
- Template and static file loading
- SQLite database working with Flask

---

## Notes

- templates/ and static/ are stored outside the flaskr package.
- The template_folder and static_folder paths were added to flaskr/__init__.py to support this structure.
- The project runs with no errors and matches the Flask tutorial behavior.

---

Project completed successfully for the CTS 285 Flask assignment.

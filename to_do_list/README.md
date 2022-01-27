# OTo Do List
This web application records a users to-do list

System Requirements

    a) Python 3.8 and above


##Getting Started

1. Install (virtualenv) by running `python -m pip install virtualenv`. 
2. Create a (virtual environment)[https://docs.python.org/3/library/venv.html#:~:text=A%20virtual%20environment%20is%20a,part%20of%20your%20operating%20system.] by running `virtualenv env`(this will create the virtual environment folders in a folder named `env`).
3. Enter to the virtual environment and run `pip install -r requrements.txt` to install necessary python packages.
4. Download the repository as a zo=ip file or (clone it)[https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository].
5. Run the command `python manage.py migrate` to create a database(SQLite is the default).
6. Run the command `python manage.py createsuperuser` and follow the prompts to add a  user to the system.
7. Run the command `python manage.py runserver`.
8. Open a web browser and navigate to the path (https://localhost:8080)[https://localhost:8080].

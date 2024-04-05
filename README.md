#Student Management System using Django
This project   is a Student Management System built with Django, allowing users to perform CRUD (Create, Read, Update, Delete) operations on student data.

#Features
User Authentication: Secure user authentication and authorization system.
Student CRUD Operations: Perform Create, Read, Update, and Delete operations on student records.
Search and Filters: Easily search and filter students based on various parameters.
Responsive Design: Ensures compatibility and usability across multiple devices.

#Installation

$Prerequisites
Python (3.6 and above)
Django (3.0 and above)

#Steps
#Clone the repository:
git clone https://github.com/pratiklamichhane/student-management-system-CRUD-django.git

#Navigate to the project directory:
cd base_project

#Create a virtual environment (optional but recommended):

python -m venv venv
Activate the virtual environment:

For Windows:
venv\Scripts\activate

For macOS and Linux:
source venv/bin/activate

#Apply database migrations:

python manage.py migrate
Start the development server:

python manage.py runserver
Access the application at http://127.0.0.1:8000/

#Usage
Create a superuser:

python manage.py createsuperuser
Access the admin dashboard at http://127.0.0.1:8000/admin/ and log in using the superuser credentials.

Manage student records by adding, updating, or deleting them via the admin interface or access the CRUD operations at http://127.0.0.1:8000

#Contributing
Contributions are welcome! Feel free to open issues or pull requests.

#License
This project is licensed under the MIT License.

 

# Todo Django Project

This is a Django-based Todo app project.

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

---

### Prerequisites

- Python 3.x installed (https://www.python.org/downloads/)
- Git installed (https://git-scm.com/downloads/)

---

### Setup Instructions

1. **Clone the repository**

   git clone <your-repo-url>
   cd todo-django

2. **Create and activate a virtual environment**

   On Windows (PowerShell):

   python -m venv env
   .\env\Scripts\Activate.ps1

   On Windows (Command Prompt):

   python -m venv env
   .\env\Scripts\activate

   On macOS/Linux:

   python3 -m venv env
   source env/bin/activate

3. **Install dependencies**

   pip install -r requirements.txt

4. **Apply database migrations**

   python manage.py migrate

5. **Create a superuser**

   python manage.py createsuperuser

6. **Run the development server**

   python manage.py runserver

7. **Open the app**

   Navigate to http://127.0.0.1:8000 in your browser to see the app running.

---

### Notes

- Make sure **not to commit** the `env/` folder or any sensitive data.
- Use a `.gitignore` file to exclude unnecessary files such as the virtual environment and compiled Python files.

---

### Updating Dependencies

To update the `requirements.txt` file after installing new packages, run:

pip freeze > requirements.txt

---

Happy coding! 🚀

1. Open command prompt and navigate to the project directory.
2. Run command python -m venv venv, this will create the Cirtual Environment and a folder called venv containing a clean python environment.
3. Actiavet the Virtual Environment by running command venv\Scripts\activate 
 Activate the Virtual Environment
🪟 On Windows (Command Prompt):
venv\Scripts\activate
🪟 On Windows (PowerShell):
.\venv\Scripts\Activate.ps1
If PowerShell gives a permissions error, run this first:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
4. Install dependencies, pip install -r requirements.txt
5. pip freeze > requirements.txt (If no requirements file found)
6. Deactivate when done. Run command deactivate
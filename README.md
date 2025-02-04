# Set up the virtual environment and installing Falsk
1. Set up a virtual environment (e.g., ```python3 -m venv venv```)
2. Activate the virtual environment (e.g., Macbook: ```source venv/bin/activate```, Windows - Cmd.exe: ```venv\Scripts\activate.bat``` Windows - PowerShell: ```venv\Scripts\Activate.ps1```)
3. Check if Flask is installed (e.g., ```pip3 show Flask```) and if needed, install it (e.g., ```pip3 install Flask```)

# Running the Jinja app
1. Tell Flask where your web app is (Macbook: ```export FLASK_APP=app``` Windows: ```set FLASK_APP=app```) 
2. Set Flask to run in development mode (enabling the debugger and automatic reloads): Macbook:  ```export FLASK_ENV=development``` Windows: ```set FLASK_ENV=development```
3. Run your Flask app with ```flask run``` and access your web app at: http://127.0.0.1:5000 

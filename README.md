# Set up the virtual environment and installing Falsk
1. Set up a virtual environment (e.g., ```python3 -m venv venv```)
2. Activate the virtual environment (e.g., Macbook: ```source venv/bin/activate```, Windows - Cmd.exe: ```venv\Scripts\activate.bat``` Windows - PowerShell: ```venv\Scripts\Activate.ps1```)
3. Check if Flask is installed (e.g., ```pip3 show Flask```) and if needed, install it (e.g., ```pip3 install Flask```)

# Running the Jinja app
1. Tell Flask where your web app is (Macbook: ```export FLASK_APP=app``` Windows: ```set FLASK_APP=app```) 
2. Set Flask to run in development mode (enabling the debugger and automatic reloads): Macbook:  ```export FLASK_ENV=development``` Windows: ```set FLASK_ENV=development```
3. Run your Flask app with ```flask run``` and access your web app at: http://127.0.0.1:5000 

# Running on PythonAnywhere
1. Open a bash shell and pull your git repo. I used HTTPs. Copy the content of your ```app.py``` file. 
2. Click "web" and then "Create a new web app"; I selected "Flask" and "Python 3.7" and then switched to: ```<username>/home/mysite/app.py``` from the default ```<username>/home/mysite/my_app.py```
3. Paste your code back into the ```app.py``` file, because PythonAnywhere will overwrite your code. 
4. Use the GUI to go to your web app and click the teal/green colored button labeled "reload \<username\>.pythonanywhere.com" and your code should be live at ```<username>.pythonanywhere.com```

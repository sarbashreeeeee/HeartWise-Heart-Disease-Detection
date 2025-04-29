# **HeartWise - Heart Disease Detection System**  

HearWise is a full-stack Flask web application developed for early detection of heart disease using machine learning.

----------------------------------------

## **Getting Started (Local Setup)**  
Follow these steps to run HeartWise on your local device.  
(Before proceeding, note that **PostgreSQL and pgAdmin should be installed and running in your device**.)


### 1. **Clone the repository**  
Run this command in your device's terminal:  
```
git clone https://github.com/sarbashreeeeee/HeartWise-Heart-Disease-Detection.git
```


### 2. **Open the project**  
Open the cloned folder in Visual Studio Code.


### 3. **Set up virtual environment**  
Run these commands one after the other in the terminal of VSCode.

* Windows (cmd-only):  
```
python -m venv venv
```
```  
venv\Scripts\activate
```  

* Mac/Linux:  
```
python3 -m venv venv
```
```
source venv/bin/activate
```
OR
```
full_path_to_python_installed_location -m venv venv
```  
```
source venv/bin/activate
```


### 4. **Install all dependencies**  
In the VSCode terminal, run:  
```
pip install -r requirements.txt
```


### 5. **Create `.env` file**  
At the root folder, create a file named `.env`.  
Copy the contents from `.env.example` and paste it into `.env`.

#### **Replace:**  
- `SECRET_KEY` value with any random long string  
- `SQLALCHEMY_DATABASE_URI` value with your actual username, password, host, port, and dbname


### 6. **Kill & reopen terminal**  
Close the current terminal in VS Code and open a new one.  
If you're on Windows, use CMD (not PowerShell).


### 7. **Reset migrations**  
Delete the entire `migrations` folder. Then in the terminal, run (one after the other):  
```
flask db init
```
```
flask db migrate -m "Any comments you would like to include"
```
```
flask db upgrade
```

**Confirm via pgAdmin that the tables are created.**


----------------------------------------

Done! The app is now ready to run locally.  
To run the app, run this command in the VSCode terminal:  
```
flask run
```

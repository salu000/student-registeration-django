### How to use this project 

# step 1
1. Extract this file and create a virtual Environment like 
  python -m venv venv

2. Activate virtual Environment like 
    venv/scripts/Activate

3. Now run command below to install requirements.txt file
   
   ```
   cd register_std_project
   pip install -r requirements.txt
   
   ```
4. Now configure your database in core/settings.py and make migrations like 
   
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver // to start your application and check it
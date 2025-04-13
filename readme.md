### Project UI/UX
**Register Student Form Page**
![image](https://github.com/user-attachments/assets/884eea1c-a63c-4e5c-b9f4-55d32425d158)

**Show Students Form Page**
![image](https://github.com/user-attachments/assets/adb4764b-4509-4afd-b301-9a6ad3f13bed)


### How to use this project 

# step 1
1. Clone this repo using following command : Note Git Must be installed on your laptop on install using ```https://git-scm.com/downloads/win```

```

 git clone https://github.com/salu000/student-registeration-django.git

```
4. 
5. Now create a virtual Environment like following using vs code terminal 
  python -m venv venv

6. Activate virtual Environment like 
    venv/scripts/Activate

7. Now run command below to install requirements.txt file
   
   ```
   cd student-registeration-django
   ```
   ```
   pip install -r requirements.txt
   ```

8. Now configure your database in core/settings.py and make migrations like 

      
  ```
  python manage.py makemigrations 
  ```
  ``` 
  python manage.py migrate
  ```
  ``` 
  python manage.py runserver
 ```
// After starting server your application will be available on this address http://127.0.0.1:8000/

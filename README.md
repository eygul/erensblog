
# Setup (Local Environment)

- Make sure Python is installed
- Create a virtual environment in your root directory by using the following command (for Windows):
  
  ```
  py -m venv yourvenvname
  ```
- You can change the "yourvenvname" with any name. 
- Activate virtual environment by using the following command (for Windows):

  ```
  yourvenvname\Scripts\activate.bat
  ```
- Download the project folder into the root directory. That means your virtual environment and project will be in the same level in the directory.
- Install project dependencies using pip.
- Migrate the database changes using the following commands (for Windows):

   ```
    py manage.py makemigrations
    py manage.py migrate
   ```
- Create a superuser using the following command (for Windows):
  
    ```
    py manage.py createsuperuser
    ```
- Congratulations! Now you can run your local server to use the app locally by using the following command (for Windows):

  ```
  py manage.py  createsuperuser
  ```

Note #1: For Linux or MacOS, use "python manage.py" instead of "py manage.py".

Note #2: This project currently uses django-ckeditor package which is the CKEditor 4. It is currently outdated, and may cause problems. 
I am not responsible in any way for any use of this project, and you can change your rich-text editor to a better one if you would like. 
It is also the reason why I will not be publishing this project live since I wanted to build this project to showcase my skills and not to use it in real life. 

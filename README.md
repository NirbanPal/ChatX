# ChatX
<p>ChatX is an interactive, real-time, responsive web-based chat application built on the popular web-development Python framework Django. </p>

**➤ Features :**
<p><b>The key features of this chat application include:-</b></p>
<p>1. Enabling real-time conversations between users. Users can interact with eachother.</p>
<p>2. Easy identification of users' application usage status by indicating whether they are online or offline fostering a sense of real-time connectivity</p>
<p>3. Ability to create and join different chat rooms allowing worldwide users' to connect among themselves over shared interest of topics</p> 
<p>4. new users can register themselves and then login to the application by providing valid credentials</p>
<p>5. message-content validation prevents users from sending blank messages or just plain white spaces</p>
<p>6. User will get notifications on receiving a message. After reading that message the notification from that message will be vanished.</p>


**➤ Tech used :**
<p> HTML , CSS, TAILWIND CSS, BOOTSTRAP, JAVASCRIPT, WEB SOCKETS, DJANGO, DJANGO CHANNELS, DJANGO SIGNALS, REDIS(MEMURAI FOR WINDOWS), PYTHON, MYSQL, WHITENOISE(FOR SERVING STATIC FILES WHEN NGINX IS NOT USED), UVICORN(AS ASGI SERVER)</p>

**➤ Setup this project :**
1. Clone this git repo->

  ```git
  git clone <gitRepoLink>
  ```
2. Go to the directory->

   ```git
   cd <directory>
   ```
   
3. Put your django secret key in the settings.py SECRET_KEY section. Download and install memurai for windows or install redis for linux. Run memurai or redis using command prompt.

4. Install virtual environment(if not preinstalled):
   ```pip
   pip install virtualenv
   ```
5. Create virtual environment->
   
   ```python
   python -m venv <your_virtual_environment_name>
   ```
6. To activate your virtual environment(windows)->

   ```shell
   <your_virtual_environment_name>\Scripts\activate
   ```
   
7. Install dependencies(requirements.py file)->
   
   ```pip
   pip install -r requirements.py
   ```

8. Migrate your database->

   ```python
   python manage.py makemigrations
   ```

   ```python
   python manage.py migrate
   ```

9. To run the application in your local machine->
   
   ```uvicorn
   uvicorn chatproject.asgi:application
   ```
   or
   
   ```uvicorn
   #Here n is number of workers. example->uvicorn chatproject.asgi:application --workers=4
   uvicorn chatproject.asgi:application --workers=n
   ```

**➤ Contributions :**
<p>Any contributions from the community is welcomed. If you find any bugs or have suggestions for new features, please submit an issue or create a pull request.</p>

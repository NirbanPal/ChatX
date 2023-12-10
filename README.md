# ChatX
<p>ChatX is an interactive, real-time, web-based chat application built on the popular web-development Python framework Django. </p>

**Features->**
<p><b>The key features of this chat application include:-</b></p>
<p>1. Enabling real-time conversations between users. Users can interact with eachother.</p>
<p>2. Easy identification of users' application usage status by indicating whether they are online or offline fostering a sense of real-time connectivity</p>
<p>3. Ability to create and join different chat rooms allowing worldwide users' to connect among themselves over shared interest of topics</p> 
<p>4. new users can register themselves and then login to the application by providing valid credentials</p>
<p>5. message-content validation prevents users from sending blank messages or just plain white spaces</p>
<p>6. User will get notifications on receiving a message. After reading that message the notification from that message will be vanished.</p>


**Tech used->**
<p> HTML , CSS, TAILWIND CSS, BOOTSTRAP, JAVASCRIPT, WEB SOCKETS, DJANGO, DJANGO CHANNELS, DJANGO SIGNALS, REDIS(MEMURAI FOR WINDOWS), PYTHON, MYSQL, UVICORN(AS ASGI SERVER)</p>

**Setup this project**
1. Clone this git repo->

  ```git
  git clone <gitRepoLink>
  ```
2. Go to the directory->

   ```git
   cd <directory>
   ```
   
3. Put your django secret key in the settings.py SECRET_KEY section and create a online redis account and get the host from it and put in the host section of CHANNEL_LAYERS. I have given the instructions how to get the host from online in settings.py also.
   
4. Create virtual environment->
   
   ```python
   python -m venv <your_virtual_environment_name>
   ```
5. To activate your virtual environment(windows)->

   ```python
   <your_virtual_environment_name>\Scripts\activate
   ```
   
6. Install dependencies(requirements.py file)->
   
   ```python
   pip install -r requirements.py
   ```

7. Migrate your database->

   ```python
   python manage.py makemigrations
   ```

   ```python
   python manage.py migrate
   ```

8. To run the application in your local machine->
   
   ```uvicorn
   uvicorn chatproject.asgi:application
   ```
   or
   
   ```uvicorn
   #Here n is number of workers. example->uvicorn chatproject.asgi:application --workers=4
   uvicorn chatproject.asgi:application --workers=n
   ```


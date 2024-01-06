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
    git clone https://github.com/NirbanPal/ChatX.git
    ```

2. Go to the directory->

   ```shell
   cd ChatX
   ```

3. Create a .env file and create a database and give the credentials of that databse in that .env file. Put your django secret key in SECRET_KEY section and do DUBUG=FALSE for production.
    ```
        SECRET_KEY='putyoursecretkey'
        DEBUG=False
        ENGINE='django.db.backends.mysql'
        HOST='putyouhost'
        NAME='putyourdbname'
        USER='putyourdbusername'
        PASSWORD='putdbpassword'
        PORT='portnumber'
    ```
4. Download and install memurai for windows or install redis for linux. Run memurai or redis using command prompt.

5. Install virtual environment(if not preinstalled):

   ```pip
   pip install virtualenv
   ```
6. Create virtual environment->
   
   ```python
   python -m venv <your_virtual_environment_name>
   ```
7. To activate your virtual environment(windows)->

   ```shell
   <your_virtual_environment_name>\Scripts\activate
   ```
   
8. Install dependencies(requirements.py file)->
   
   ```pip
   pip install -r requirements.txt
   ```

9. Migrate your database->

   ```python
   python manage.py makemigrations
   ```

   ```python
   python manage.py migrate
   ```
10. Collection os static files->
    
    ```python
    python manage.py collectstatic
    ```

11. To run this application in your local machine->
   
    ```uvicorn
    uvicorn ChatX.asgi:application
    ```
    or
    
    ```uvicorn
    #Here n is number of workers. example->uvicorn ChatX.asgi:application --workers=4
    uvicorn ChatX.asgi:application --workers=n
    ```

**➤ Contributions :**
<p>Any contributions from the community is welcomed. If you find any bugs or have suggestions for new features, please submit an issue or create a pull request. Some features will be added in future also.</p>

**➤ Glimpses of ChatX :**

<a href="https://ibb.co/3RQdSRH"><img src="https://i.ibb.co/dmxMkmy/signuppage.png" alt="signuppage" border="0"></a><br />
<a href="https://ibb.co/WfDKtgp"><img src="https://i.ibb.co/gJvgVzF/loginpage.png" alt="loginpage" border="0"></a>
<a href="https://ibb.co/6BzxY0m"><img src="https://i.ibb.co/pyc82jx/onetoone.png" alt="onetoone" border="0"></a>
<a href="https://ibb.co/kB4jtpb"><img src="https://i.ibb.co/yP6trDv/onetoonechat.png" alt="onetoonechat" border="0"></a>
<a href="https://ibb.co/7SX9xct"><img src="https://i.ibb.co/3T7J5Xm/rooms.png" alt="rooms" border="0"></a>
<a href="https://ibb.co/vLZc6DM"><img src="https://i.ibb.co/QYrJ3Xx/createroom.png" alt="createroom" border="0"></a>
<a href="https://ibb.co/PZHZWMz"><img src="https://i.ibb.co/vxnxdhv/exampleofroomdiscussions.png" alt="exampleofroomdiscussions" border="0"></a>
<a href="https://ibb.co/fv36Dr3"><img src="https://i.ibb.co/bJ4wbN4/blankroom.png" alt="blankroom" border="0"></a>
<a href="https://ibb.co/FVV4Xzs"><img src="https://i.ibb.co/L55dr1Q/offline-SS.png" alt="offline-SS" border="0"></a>



echo off
echo Activating Anaconda
Call C:\Users\garre\AppData\Local\anaconda3\Scripts\activate.bat
echo Activating flask envirnoment
Call conda activate flask
echo Configuring FLASK_APP variable
Call conda env config vars set FLASK_APP=myblog.py
echo Reactivating flask envirnoment
Call conda activate flask
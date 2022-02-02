# User Registration and authentication using PyJWT
## Setup libraries and Environment for using API 
### Used libraries versions :
> Python  3.9.7 <br>
> Fastapi 0.73.0 <br>
> Uvicorn 0.15.0<br>
> PyJWT 2.3.0<br>
> SQLAlchemy 1.4.31<br>

## Introduction

This is a user management system on FASTAPI framework.
In this I used to register user and use bcrypt for hashing the password before saving into the database,
after login a json web token is generated which have username of logged in user
through that token user can access 

```
    localhost:8000/protected
```

This project currently runs on the local host. So every api should run from the local host.


## Run this project:-

For run this project you have to first clone this by using

```	 
	 	git clone https://github.com/ongraphpythondev/usermanagement_fastapi_jwt.git
```
### Firstly Install python virtual environment and install all required libraries in python virtualenvironment.
#### install virtualenv :
>  pip install virtualenv
#### create python virtualenvironment :
>  virtualenv env
#### activate virtualenv/env :
>  env\Scripts\activate.bat <br> this will activate virtual environment
#### after that install required libraries

In linux/Macos
```		
				pip3 install -r requirenment.txt  
```
In windows
```
				pip install -r requirenment.txt
```
				
To run this project go to this directory(Where you put this project) and run this command.

```
		uvicorn main:app --reload
```
**here --reload is used to automatically reload the server if get any changes in the code**

## Operations:


**Register a new user**:-   For registering a new user, you have to go to 
```
				localhost:8000/register
```

**logging the user**:- For login the user , you have to go to 
```
        localhost:8000/login
```

**accessing the unprotected content** :- For accessing the unprotected content without token verfication, you have to go 
```
        localhost:8000/unprotected
```
**accessing the protected content** :- For accessing the protected content ,you have to go 
```
        localhost:8000/protected
```
for accesssing the /protected path  you have to pass the token u get after login 

**Thank you**

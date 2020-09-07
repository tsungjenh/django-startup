## Django For Startup

### Intro
Django is a popular backend framework to develop a web services. This Project aims to provide a clear skeleton for anyone to start a django project.   
It will provide a clear project structure with a bunch of the common backend modules including the
1. `Request Middlewares`, 
2. `Log Parser`, 
3. `Params Validators`, 
4. `Session Handle`, 
5. `Response`
6. `Custom Exception Handling`  


### Project Structure
~~~
.
+-- api
|   +-- user
|   |   +-- forms.py
|   |   +-- views.py
|   +-- echo
|   |   +-- forms.py
|   |   +-- views.py
|   +-- {module in the futures}
|   |   +-- forms.py
|   |   +-- views.py
|   +-- urls.py
+-- doc 
+-- scripts 
|   +-- management
|   |   +-- commands
|   |   |   +-- {command}.py
+-- service 
|   +-- biz 
|   |   +-- user
|   |   |   +-- models.py
|   |   |   +-- handler.py
|   |   |   +-- dao.py
|   +-- django_ext
|   +-- libs 
+-- tests 
+-- webservices 
~~~
1. `api`: The **api** folder contains the `urls.py` and a list of business modules view layers. In each modules, there should ba a `forms.py` to define the request and response `schema`
2. `doc`: To put Documents(api.doc, tech_design.doc etc...)
3. `script`: The **scripts** folder contains Django command scripts.
4. `service`: The core business logic. The **service** folder contains
    1. `libs`: common utility for the project such as `decorator`, `custom exception`, `log parser`
    2. `django_ext`: extend and enhance django utils such as `models`, `response`, `view`
    3. `biz`: for the actual business service logic. In each modules, there are modules as belows(from bottom-up)
        1. `models.py`: Define db and all the models
        2. `dao.py`: The interface to the database
        3. `handler.py`: business logic
5. `tests`: To put test script
6. `webservices`: The **webservices** contains **configuration**, **middleware** and **settings.py** 

> The overall flow should be api -> handler -> dao -> model. We should keep the structure and make the project well organized.

### Quick Start
1. Install docker and docker-compose: Please follow the instruction here. [Docker Installation](https://docs.docker.com/get-docker/)
2. Run the project with docker-compose
~~~
> cd <path to project>
> docker-compose up
~~~ 
3. Test the echo API
~~~
> curl --location --request GET 'localhost:8000/api/echo/?echo=echo' \
--header 'Cookie: sessionid=nr4jtmcqd295al1j9w2vxprkng2u49ts'
{"status": "ok", "msg": "", "data": {"echo": {"echo": "echo"}}}% 
~~~
    
  

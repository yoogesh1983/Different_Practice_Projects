**You must do the following before start the server:**

> pip install bcrypt 

> pip install django-taggit

> pip install requests

To install the Django Rest API, install following:

> pip install djangorestframework
>
> pip install markdown      
> 
> pip install django-filter

The Application can now be browsed at http://127.0.0.1:8000

Similarly, the Admin view can be browsed at http://127.0.0.1:8000/admin/

**How to create virtualEnv?**
> pip install virtualenvwrapper-wi (Only needed for windows)
>
> mkvirtualenv --python=python3.8 myvirtualenv
>
> pip install -U django==3.1.3
>
> pip list
>
> git clone https://github.com/yoogesh1983/Different_Practice_Projects.git

**How to set the created enviroment?**

> find / | grep bin/activate
>
> cd /home/yoogesh2002/.virtualenvs/myvirtualenv/bin
>
> source activate

By the way, in the case of windows, you need below:

> activate.bat

The **_myvirtualenv_** is now set for your current project at:
 
 > /home/yoogesh2002/.virtualenvs/myvirtualenv

You need to configure below static path while deploying application to cloud:

> /home/yoogesh2002/.virtualenvs/myvirtualenv/lib/python3.8/site-packages/django/contrib/admin/static/admin &nbsp;&nbsp;[for _/static/admin_]
>
> /home/yoogesh2002/Different_Practice_Projects/python/01_Django/YoogehPythonProject/blogpost/static &nbsp;&nbsp; [For _/static_]
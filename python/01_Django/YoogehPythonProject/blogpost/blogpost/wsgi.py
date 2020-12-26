"""
WSGI config for blogpost project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogpost.settings')

application = get_wsgi_application()


"""
# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys
#
## assuming your django settings file is at '/home/yoogesh2002/mysite/mysite/settings.py'
## and your manage.py is is at '/home/yoogesh2002/mysite/manage.py'
path = '/home/yoogesh2002/Different_Practice_Projects/python/01_Django/YoogehPythonProject/blogpost'
if path not in sys.path:
    sys.path.append(path)
os.chdir(path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogpost.settings')
#
#os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
#
## then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

"""

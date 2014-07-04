import os, sys

#Calculate the path based on the location of the WSGI script.
#apache_configuration= os.path.dirname(__file__)
#project = os.path.dirname(apache_configuration)
#workspace = os.path.dirname(project)
#sys.path.append(workspace)

#Add the path to 3rd party django application and to django itself.
sys.path.insert(0, '/home/spoken-17/ashwini_booktype/')
sys.path.insert(1, '/home/spoken-17/ashwini_booktype/mybook/lib/')
sys.path.insert(2, '/home/spoken-17/ashwini_booktype/Booktype/lib/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'mybook.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()


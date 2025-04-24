import os
import sys
from django.core.wsgi import get_wsgi_application

# Set the Python path to the directory where this file is located
sys.path.insert(0, os.path.dirname(__file__))

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rotaryproject.settings')  

# Create the WSGI application object
application = get_wsgi_application()
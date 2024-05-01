from django.contrib import admin
from .models import Post

''' 
    Register models here.
    This will allow the models to be viewed and edited in the Django admin interface.
    
'''

admin.site.register(Post)


# Campaign Site

This is a fictional campaign website, demonstrating the use of Django apps and bootstrap for serving user interactive features, and dynamic display.




## Deployment

To deploy this project in an environment, first install a virtual environment
in the project root folder using the command prompt:

'''cmd
  python -m venv env
'''

The environment can then be started from the command prompt in the venv with
'''cmd
  Scripts/Activate
'''

To start the server in the venv, enter the following in the command prompt


```cmd
  python manage.py runserver 
```


From the docker

'''cmd
  docker run -i -p 8000:8000 campaignsite
'''

On dockerhub

'''cmd
  docker run -i -p 8000:8000 stevenmeare/campaignsite

Superuser credentials can be assigned from cmd using

'''cmd
    python manage.py createsuperuser
'''

## 

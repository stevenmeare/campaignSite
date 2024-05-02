
# Campaign Site

This is a fictional campaign website, demonstrating the use of Django apps and bootstrap for serving user interactive features, and dynamic display.




## Deployment

To deploy this project run

```cmd
  python manage.py runserver 
```

within the environment. 

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

from django.db import models

'''
Define Models for the blog app.
Each model represents a table in the database.
Each model class is a subclass of django.db.models.Model.
Each attribute of the model represents a column in the table.
'''

class Post(models.Model):
    '''
    This model defines a blog post.
    :param title: The title of the post.
    :type title: str

    :param body: The content of the post.
    :type body: str

    :param signature: The author of the post.
    :type signature: str

    :param date: The date the post was created.
    :type date: datetime

    :return: The title of the post.
    :rtype: str

    '''
    title = models.CharField(max_length=140)
    body = models.TextField()
    signature = models.CharField(max_length=140, default="Steve")
    date = models.DateTimeField()

    def __str__(self):
        return self.title

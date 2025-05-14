from django.db import models


class Post(models.Model):
    """
    The following commands in terminal will activate the model in the posts app:
        $ python manage.py makemigrations posts
        $ python manage.py migrate
    """
    text = models.TextField()

    def __str__(self):
        return self.text[:50]
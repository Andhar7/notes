# Create a model Note for working with DB - Postgres
from django.db import models
from django.core.validators import MaxLengthValidator

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=210, verbose_name='Notes title', help_text='Please enter the title of the note')
    content = models.TextField(validators=[MaxLengthValidator(10000)], verbose_name='Your content is here', help_text='Please enter the content of the note')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')


    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
        ordering = ['-created_at']

    def __str__(self):
        # How look like in an admin panel
        return self.title[:50]


"""
A Model to represent a Page in the website
A page can only be created in the admin section by
a valid user
"""

from django.db import models


class Page(models.Model):
    """ A Model representing a page on the website """
    title = models.CharField(max_length=60)
    permalink = models.CharField(max_length=12,
                                 unique=True)
    update_date = models.DateTimeField('Last Updated')
    bodytext = models.TextField('Page Content', blank=True)

    def __str__(self):
        return self.title

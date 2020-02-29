"""
A model for a quote submitted by a user of the website
"""
from django.contrib.auth.models import User
from django.db import models

STATUS_CHOICES = (
    ('NEW', 'New Site'),
    ('EX', 'Existing Site'),
)

PRIORITY_CHOICES = (
    ('U', 'Urgent - 1 week or less'),
    ('N', 'Normal - 2 to 4 weeks'),
    ('L', 'Low - still Researching'),
)


class Quote(models.Model):
    """
    A model representing a Quote submitted by a user
    on the website
    """
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=60,
                                blank=True)
    company = models.CharField(max_length=60,
                               blank=True)
    address = models.CharField(max_length=200,
                               blank=True)
    phone = models.CharField(max_length=30,
                             blank=True)
    email = models.EmailField()
    web = models.URLField(blank=True)
    description = models.TextField()
    sitesstatus = models.CharField(max_length=20,
                                   choices=STATUS_CHOICES)
    priority = models.CharField(max_length=40,
                                choices=PRIORITY_CHOICES)
    jobfile = models.FileField(upload_to='uploads/',
                               blank=True)
    submitted = models.DateField(auto_now_add=True)
    quotedate = models.DateField(blank=True,
                                 null=True)
    quoteprice = models.DecimalField(decimal_places=2,
                                     max_digits=7, blank=True,
                                     default=0)
    username = models.ForeignKey(User, blank=True,
                                 null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

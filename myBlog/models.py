from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    def __unicode__(self):
        return self.name

class Author(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=40)
    email = models.EmailField('e-mail')
    def __unicode__(self):
        return u'%s %s' % (self.firstName, self.lastName)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publicationDate = models.DateField('PDate', blank=True)

    def __unicode__(self):
        return self.title

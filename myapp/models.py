from django.db import models

class Person(models.Model):
    id_card = models.CharField(unique=True, max_length=10)
    name = models.CharField(verbose_name='Names', max_length=60)
    last_name = models.CharField(verbose_name='Last Name', max_length=60)

    def __unicode__(self):
        return self.id_card

class Project(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Person)

    def __unicode__(self):
        return self.title

from django.db import models


class Name_Picture(models.Model):
    names = models.CharField(max_length=128, verbose_name='姓名')
    picture = models.CharField(max_length=128, verbose_name='picture')

    def __str__(self):
        return '<names: {}>'.format(self.names)

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    def get_name(self):
        return self.names


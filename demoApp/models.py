from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.


class Owner(models.Model):
    name = models.CharField(_('Name'), max_length=45, db_index=True)

    dog = models.ForeignKey(
        'demoApp.Dog',
        verbose_name=_('Dog'),
        on_delete=models.SET_NULL,
        null=True
    )

    cat = models.ForeignKey(
        'demoApp.Cat',
        verbose_name=_('Cat'),
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.name


class Pet(models.Model):
    name = models.CharField(_('Name'), max_length=45, db_index=True)
    dob = models.DateField(_('Date of Birth'), db_index=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Dog(Pet):
    pass


class Cat(Pet):
    pass

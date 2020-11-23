import uuid

from django.db import models

from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractUser, Permission, GroupManager

from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


# class User(models.Model):
#
#     TYPE_CHOICES = (
#         (0, 'Estudante'),
#         (1, 'Monitor')
#     )
#
#     name = models.CharField(max_length=200)
#     registration = models.CharField(max_length=11, unique=True)
#     password = models.CharField(max_length=200)
#     registration_type = models.IntegerField(choices=TYPE_CHOICES)
#     photo = StdImageField('Imagem', upload_to=get_file_path,
#                           variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
#     about = models.TextField(max_length=400)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Usuário'
#         verbose_name_plural = 'Usuários'


class User(AbstractUser):

    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    registration = models.CharField(max_length=11, unique=True)
    photo = StdImageField('Imagem', upload_to=get_file_path,
                          variations={'thumb': {'width': 300, 'height': 300, 'crop': True}})
    about = models.TextField(max_length=400)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'


# class Teste(models.Model):
#
#     GENDER = (
#         (0, 'Masculino'),
#         (1, 'Feminino')
#     )
#
#     name = models.CharField(max_length=100)
#     gender_choice = models.IntegerField(choices=GENDER)

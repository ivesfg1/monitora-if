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


class User(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    registration = models.CharField(max_length=11, unique=True)
    photo = StdImageField('Imagem', upload_to=get_file_path,
                          variations={'thumb': {'width': 300, 'height': 300, 'crop': True}}, blank=True, null=True)
    about = models.TextField(max_length=400, blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

# models.py

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(_('name'), max_length=100, null=True)
    organization = models.CharField(_('organization'), max_length=100)
    user_type = models.CharField(_('user_type'), max_length=100)
    linkedin_url = models.CharField(_('linkedin_url'), max_length=100)

    # Define related names for groups and user_permissions
    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='custom_user_set', related_query_name='user')
    user_permissions = models.ManyToManyField(Permission, verbose_name=_('user permissions'), blank=True, related_name='custom_user_set', related_query_name='user')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email  # Assign email to username if username is not set
        super().save(*args, **kwargs)

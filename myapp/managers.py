from django.db import models as django_models
 
 

class CustomerManager(django_models.Manager):
    def get_authenticated(self, user):
        if user.is_authenticated:
            return self.get(user=user)
        return None

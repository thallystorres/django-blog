from django.db import models
from django.core.exceptions import ValidationError


def validate_png(image: models.ImageField):
    if not image.name.lower().endswith('.png'):
        print('Que chato...')
        print('Que chato...')
        print('Que chato...')
        print('Que chato...')
        print('Que chato...')
        print('Que chato...')
        raise ValidationError('Image needs to be PNG.')

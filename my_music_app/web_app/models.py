from django.core import validators
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
import re

INVALID_USERNAME_EXCEPTION_MESSAGE = "Ensure this value contains only letters, numbers, and underscore."


def validate_username(value: str):

    if not re.match(r'^\w*$', value):
        raise ValidationError(INVALID_USERNAME_EXCEPTION_MESSAGE)


class Profile(models.Model):
    USER_NAME_MIN_LENGTH = 2
    USER_NAME_MAX_LENGTH = 15
    AGE_MIN_VALUE = 0

    user_name = models.CharField(
        max_length=USER_NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(USER_NAME_MIN_LENGTH),
            validate_username,
        ]
    )

    email = models.EmailField()
    age = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(AGE_MIN_VALUE)
        ],
        null=True,
        blank=True
    )

    def __str__(self):
        return self.user_name


class Album(models.Model):
    ALBUM_NAME_MAX_LENGTH = 30
    ARTIST_NAME_MAX_LENGTH = 30
    GENRE_MAX_LENGTH = 30

    PRICE_DEFAULT_VALUE = 0.0
    PRICE_MIN_VALUE = 0.0

    album_choices = (
        ('pop_music', 'Pop Music'),
        ('jazz_music', 'Jazz Music'),
        ('rb_music', 'R&B Music'),
        ('rock_music', 'Rock Music'),
        ('country_music', 'Country Music'),
        ('dance_music', 'Dance Music'),
        ('hip_hop_music', 'Hip Hop Music'),
        ('other', 'Other'),
    )

    name = models.CharField(max_length=ALBUM_NAME_MAX_LENGTH, unique=True, verbose_name='Album Name')
    artist = models.CharField(max_length=ARTIST_NAME_MAX_LENGTH)
    genre = models.CharField(
        max_length=GENRE_MAX_LENGTH,
        choices=album_choices,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    image_url = models.URLField(verbose_name='Image URL')
    price = models.FloatField(
        default=PRICE_DEFAULT_VALUE,
        validators=[
            MinValueValidator(PRICE_MIN_VALUE)
        ]
    )

    def __str__(self):
        return self.name

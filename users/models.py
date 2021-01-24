from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """ Custon User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "English"), (LANGUAGE_KOREAN, "Korean"))

    CURRENCY_USD = "USD"
    CURRENCY_KRW = "KRW"

    CURRENCY_CHOICES = ((CURRENCY_USD, "usd"), (CURRENCY_KRW, "krw"))

    avatar = models.ImageField("프로필 사진", null=True, blank=True)
    gender = models.CharField(
        "성별", choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )
    bio = models.TextField("사용자정보", default="", blank=True)
    birthdate = models.DateField("생년월일", null=True, blank=True)
    language = models.CharField(
        "언어유형", choices=LANGUAGE_CHOICES, max_length=5, null=True, blank=True
    )
    currency = models.CharField(
        "화폐유형", choices=CURRENCY_CHOICES, max_length=5, null=True, blank=True
    )
    superhost = models.BooleanField("호스트권한", default=False)

from django.db import models
from core import models as core_models
from users import models as user_models
from rooms import models as room_models


class Reservation(core_models.TimeStampedModel):

    """ Reservation Model Definition """

    class Meta:
        verbose_name_plural = "예약 관리"

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANELED = "canceled"

    STATUS_CHOICE = (
        (STATUS_PENDING, "pending"),
        (STATUS_CONFIRMED, "confirmed"),
        (STATUS_CANELED, "canceled"),
    )

    stauts = models.CharField(
        max_length=12, choices=STATUS_CHOICE, default=STATUS_PENDING
    )
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    room = models.ForeignKey(room_models.Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room} - {self.check_in}"

from django.contrib.auth.hashers import check_password, make_password
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    # Stored as a hashed value (not plain text).
    password = models.CharField(max_length=255)
    age = models.PositiveIntegerField()

    def set_password(self, raw_password: str) -> None:
        self.password = make_password(raw_password)

    def check_password(self, raw_password: str) -> bool:
        return check_password(raw_password, self.password)

    def __str__(self) -> str:
        return f"{self.name} <{self.email}>"

from django.db import models

class Member(models.model):
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)

    def __str__(self):
        return str(self.id)
    class Meta:
        db_table='member_atin'
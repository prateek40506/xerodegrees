from django.db import models

# Create your models here.
class Table(models.Model):
    choices = (
        ('unoccupied', 'unoccupied'),
        ('occupied', 'occupied')
    )
    table_id = models.IntegerField()
    status = models.CharField(max_length=50, choices=choices)


    def __int__(self):
        return self.table_id

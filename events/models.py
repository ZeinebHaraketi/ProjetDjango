from django.db import models
import datetime
from django.core.exceptions import ValidationError
from Users.models import Person 
# Create your models here.
def in_the_future(value):
   if value <= datetime.date.today():
    raise ValidationError('verifier votre date ')
class Event(models.Model):
     title = models.CharField("Title" ,max_length=250)
     description =models.TextField()
     state =models.BooleanField(default=False)
     imageEvent=models.ImageField(upload_to='images/',blank=True )
     nbParticipants=models.IntegerField(default=0)
     CATEGORY_CHOICES=(
        ('Music','Music'),
        ('Sport','Sport'),
        ('Cinema','Cinema'),
    )
     category=models.CharField(max_length=10,choices=CATEGORY_CHOICES)
     dateEvent=models.DateField(validators=[in_the_future])
     createdAt=models.DateField(auto_now_add=True)
     updateAt=models.DateField(auto_now=True)
     organized =models.ForeignKey(Person,on_delete=models.CASCADE)
     participants =models.ManyToManyField(
        Person,
        related_name="participations",
        through="Participation"
     )
     def __str__(self):
        return self.title


class Participation(models.Model):
    person=models.ForeignKey(Person,on_delete=models.CASCADE)
    event=models.ForeignKey(Event, on_delete=models.CASCADE)
    datePart=models.DateField(auto_now=True)
    class Meta:
      unique_together=('person','event')

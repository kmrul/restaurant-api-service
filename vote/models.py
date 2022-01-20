from sqlite3 import IntegrityError
from django.db import models
from base.models import Restaurant




class Candidate(models.Model):
    name = models.CharField(max_length=250)
    restaurant = models.ForeignKey(to=Restaurant, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    date = models.DateField()
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.name




class Vote(models.Model):
    name = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=50, default="None", unique=True)
    candidate = models.ForeignKey(to=Candidate, on_delete=models.CASCADE)
    date = models.DateField()
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)




    def save(self, commit=True, *args, **kwargs):
        print("self:",self,"commit:", commit)
        if commit:
            try:
                self.candidate.votes +=1
                self.candidate.save()
                super(Vote, self).save(*args, **kwargs)
            except IntegrityError:
                self.candidate.votes -= 1
                self.candidate.save()
                raise IntegrityError
        else:
            raise IntegrityError




    def __str__(self):
        return self.name



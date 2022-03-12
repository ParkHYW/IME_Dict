from django.db import models 

# 엑셀 연결
class Company(models.Model):
    term = models.CharField(max_length=200)
    meaning = models.TextField()
    
    def __str__(self):
        return self.term

class Analytics(models.Model):
    term = models.CharField(max_length=200)
    meaning = models.TextField()

    def __str__(self):
        return self.term

class Anthropometry(models.Model):
    term = models.CharField(max_length=200)
    meaning = models.TextField()

    def __str__(self):
        return self.term


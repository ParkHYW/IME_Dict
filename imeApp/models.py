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

class Computer(models.Model):
    term = models.CharField(max_length=200)
    meaning = models.TextField()

    def __str__(self):
        return self.term

class Cost(models.Model):
    term = models.CharField(max_length=200)
    meaning = models.TextField()

    def __str__(self):
        return self.term

class Distribution(models.Model):
    term = models.CharField(max_length=200)
    meaning = models.TextField()

    def __str__(self):
        return self.term

class Employee(models.Model):
    term = models.CharField(max_length=200)
    meaning = models.TextField()

    def __str__(self):
        return self.term

class Engineering(models.Model):
    term = models.CharField(max_length=200)
    meaning = models.TextField()

    def __str__(self):
        return self.term

class Facility(models.Model):
    term = models.CharField(max_length=200)
    meaning = models.TextField()

    def __str__(self):
        return self.term

class Human(models.Model):
    term = models.CharField(max_length=200)
    meaning = models.TextField()

    def __str__(self):
        return self.term

class Management(models.Model):
    term = models.CharField(max_length=200)
    meaning = models.TextField()

    def __str__(self):
        return self.term

class Manufacturing(models.Model):
    term = models.CharField(max_length=200)
    meaning = models.TextField()

    def __str__(self):
        return self.term
#수정
class new_Materials(models.Model):
    term = models.CharField(max_length=200)
    meaning = models.TextField()

    def __str__(self):
        return self.term

class Materials(models.Model):
    term = models.CharField(max_length=200)
    meaning = models.TextField()

    def __str__(self):
        return self.term

class Occupational(models.Model):
    term = models.CharField(max_length=200)
    meaning = models.TextField()

    def __str__(self):
        return self.term

#수정
class new_Operation(models.Model):
    term = models.CharField(max_length=200)
    meaning = models.TextField()

    def __str__(self):
        return self.term

class Operations(models.Model):
    term = models.CharField(max_length=200)
    meaning = models.TextField()

    def __str__(self):
        return self.term

class Organization(models.Model):
    term = models.CharField(max_length=200)
    meaning = models.TextField()

    def __str__(self):
        return self.term

class Quality(models.Model):
    term = models.CharField(max_length=200)
    meaning = models.TextField()

    def __str__(self):
        return self.term

class Work(models.Model):
    term = models.CharField(max_length=200)
    meaning = models.TextField()

    def __str__(self):
        return self.term
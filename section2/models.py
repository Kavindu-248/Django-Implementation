from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)


class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()


class Interviewer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    job = models.ManyToManyField(Job)


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    job = models.ManyToManyField(Job)


class Assessor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    job = models.ManyToManyField(Job)


class Assessment(models.Model):
    assessor = models.ForeignKey(Assessor, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)


class QuestionSet(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=100)
    email = models.CharField(max_length=320)
    is_valid_email = models.BooleanField(default=False)
    school = models.CharField(max_length=30)
    major = models.CharField(max_length=100)
    grade = models.IntegerField(null=False)
    sex = models.BooleanField(default=True)
    point = models.IntegerField(default=0)

class Maincategory(models.Model):
    name = models.CharField(max_length=100)

class Subcategory(models.Model):
    maincategory = models.ForeignKey(Maincategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Notice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()
    content = models.TextField()
    is_trash = models.BooleanField(default=False)
    liked = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

class Maincomment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    content = models.CharField(max_length=200)
    liked = models.IntegerField(default=0)

class Subcomment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    maincomment = models.ForeignKey(Maincomment, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    content = models.CharField(max_length=200)
    liked = models.IntegerField(default=0)
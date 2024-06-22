from django.db import models
class Classes(models.Model):
    Class=models.CharField(max_length=50)
    def __str__(self):
       return self.Class
class Subjects(models.Model):
    Class=models.ForeignKey(Classes, on_delete=models.CASCADE, blank=True, null=True)
    Subject=models.CharField(max_length=50)
    def __str__(self):
           return self.Subject
class Topics(models.Model):
    Class=models.ForeignKey(Classes,on_delete=models.CASCADE,blank=True, null=True)
    Subject=models.ForeignKey(Subjects,on_delete=models.CASCADE)
    
    Topic=models.CharField(max_length=300)
    def __str__(self):
           return self.Topic
class subtopic(models.Model):
    Class=models.ForeignKey(Classes,on_delete=models.CASCADE,blank=True, null=True)
    Subject=models.ForeignKey(Subjects,on_delete=models.CASCADE)
    Topic=models.ForeignKey(Topics,on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    overview=models.TextField()
    videolink=models.CharField(max_length=500)
    def __str__(self):
           return self.title
class image(models.Model):
    Subject=models.ForeignKey(Subjects,on_delete=models.CASCADE)
    image=models.CharField(max_length=300)

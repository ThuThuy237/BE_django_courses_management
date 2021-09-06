from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import mark_safe

# Create your models here.

class User(AbstractUser):
    avatar = models.ImageField(upload_to='static/uploads/%Y/%m',null=True)
class Job(models.Model):
    name_job = models.CharField(max_length=255)
    def __str__(self):
        return self.name_job
class Skill(models.Model):
    name_skill = models.CharField(max_length=255)
    def __str__(self):
        return self.name_skill
class Teacher(models.Model):
    user_id = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    activeTeacher = models.BooleanField(default=False)
    skills = models.ManyToManyField(Skill,blank=True,related_name='teacher')
    job = models.ForeignKey(Job,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return str(self.user_id)


class Follow(models.Model):
    class Meta:
        unique_together = ('student', 'teacher')
    student = models.ForeignKey(User,on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.student)+' followed '+str(self.teacher)

class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name

class ModelBase(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ['-id'] # sắp giảm theo id

class Tag(models.Model):
    name = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name

class Course(ModelBase):
    name_course = models.CharField(max_length=200,null=False,default=None)
    description = models.TextField(null=True,default="Chưa có mô tả Khóa Học")
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    tags = models.ManyToManyField('Tag', blank=True,related_name='course')
    teacher_id = models.ForeignKey(Teacher,on_delete=models.CASCADE,null=False)
    image = models.ImageField(upload_to='courses/%Y/%m/',null=True, blank=True)
    students = models.ManyToManyField('User',blank=True,related_name='course')
    def __str__(self):
        return self.name_course

class Lesson(ModelBase):
    class Meta:
        unique_together = ('subject', 'course')
    subject = models.CharField(max_length=255)
    content = models.TextField()
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='lessons',related_query_name='my_lession')
    image = models.ImageField(upload_to='courses/%Y/%m/',null=True, blank=True)
    def __str__(self):
        return self.subject

class Video(models.Model):

    subject =  models.CharField(max_length=255)
    url_video = models.CharField(max_length=255)
    lession = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='list_video',
                               related_query_name='list_video_lesson')
    def __str__(self):
        return self.subject

class File(models.Model):
    subject = models.CharField(max_length=255)
    file = models.FileField(upload_to='static/file/%Y/%m')
    lession = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='list_file',
                                related_query_name='list_file_lesson')
    def __str__(self):
        return self.subject
class HomeWork(models.Model):
    author_teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name='home_work')
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE,related_name='home_work')
    subject = models.CharField(max_length=255)
    file = models.FileField(upload_to='static/homework/%Y/%m')
    content = models.TextField()

    def __str__(self):
        return self.subject
class GroupChat(models.Model):
    id_course = models.OneToOneField(Course,on_delete=models.CASCADE,primary_key=True)
    name_group = models.CharField(max_length=255,null=False)
    def __str__(self):
        return self.name_group
class Message(models.Model):
    id_user = models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    group_chat = models.ForeignKey(GroupChat,on_delete=models.CASCADE,null=False)
    mess = models.TextField()
    date_post = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id_user) + ' Said ' + str(self.mess) + ' in group chat ' + str(self.group_chat) + ' at time: ' + str(self.date_post)
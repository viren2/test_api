from django.db import models

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=50)
    student_add = models.CharField(max_length=50)
    update_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return " Teacher Name is "+self.teacher_name +" Student add is "+self.student_add +" update date at "+str(self.update_date)
    
class Student(models.Model):
    student_name = models.CharField(max_length=50)
    course_name  =  models.CharField(max_length=50)
    class_name = models.CharField(max_length=10)
    def __str__(self):
        return " Student name is "+self.student_name +" course name is "+self.course_name +" class name is " +self.class_name

class  AdminInfo(models.Model):
    admin_name = models.CharField(max_length=50)
    user_add = models.CharField(max_length=50)
    teacher =  models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    def __str__(self):
         return " admin name is "+self.admin_name +" user add is " +self.user_add





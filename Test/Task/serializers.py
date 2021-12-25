from . models import AdminInfo,Teacher,Student
from rest_framework import serializers

class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = ["id","teacher_name","student_add","update_date"]

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ["id","student_name","course_name","class_name"]

class AdminInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  AdminInfo
        fields = ["id","admin_name","user_add","teacher","student"]



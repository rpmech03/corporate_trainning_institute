from ast import Str
from django.db import models
from django.contrib.auth.models import User
class Student(User):
    mobile=models.CharField(max_length=11)
    join_date=models.DateField(auto_now=False)
    total_fees=models.IntegerField()
    ch=(  
        ('mern','mern'),
        ('java fullstack','java fullstack'),
        ('python fullstack','python fullstack'),
    )
    module=models.CharField(max_length=20,choices=ch)
    image=models.ImageField(upload_to='pics')
    st=(
        ('training','training'),
        ('placed','placed'),
        ('complete','complete'),
    )
    status=models.CharField(max_length=20,choices=st)
    jn=(
        ('bhanwarkua','bhanwarkua'),
        ('vijay_nagar','vijay_nagar'),
        ('ujjain','ujjain'),
    )
    joining_location=models.CharField(max_length=20,choices=jn)

    def __str__(self) :
        return self.first_name 

class Trainer(User):
    mobile=models.CharField(max_length=11)

    def __str__(self) -> str:
        return self.mobile
        
class Task(models.Model):
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    topics=models.TextField()
    date=models.DateField(auto_now=False)
    timings_for_day=models.CharField(max_length=50)
    remarks=models.TextField()

    def __str__(self) -> str:
        return self.topics
    
    

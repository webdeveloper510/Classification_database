from django.db import models
from django.contrib.auth.models import * 

class InputOutput(models.Model):
    input=models.TextField()
    output=models.TextField(null=True , blank=True)

    # class Meta:
    #     db_table = "mobile_technology_database"
   

class Mobile_Technology_Waves(models.Model):
    question=models.TextField(max_length=1000)
    answer=models.TextField(max_length=1000)
    
    class Meta:
        app_label = 'firstmyapp'
        db_table ="mobile_technology_waves"

    # specify the database to use
    using = 'default'

class Technologies(models.Model):
    question=models.TextField(max_length=1000)
    answer=models.TextField(max_length=1000)

    class Meta:
        app_label = 'firstmyapp'
        db_table ="technologies"
    using = 'user1'

class Cricket_Question_and_Answer(models.Model):
    question=models.TextField(max_length=1000)
    answer=models.TextField(max_length=1000)
    
    class Meta:
        app_label = 'firstmyapp'
        db_table ="cricket_question_and_answer"
    using = 'default'
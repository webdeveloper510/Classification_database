from rest_framework import  serializers
from .models import *

class InputOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model= InputOutput
        fields="__all__"
        
    
class Mobile_Technology_WavesSerializer(serializers.ModelSerializer):
     class Meta:
        model= Mobile_Technology_Waves
        fields = '__all__'
           
     def create(self, validate_data):
         return Mobile_Technology_Waves.objects.create(**validate_data)
     
    
class TechnologieSerializer(serializers.ModelSerializer):
     class Meta:
        model= Technologies
        fields = '__all__'
           
     def create(self, validate_data):
         return Technologies.objects.create(**validate_data)
     
class CricketSerializer(serializers.ModelSerializer):
    class Meta:
        model= Cricket_Question_and_Answer
        fields = '__all__'
           
    def create(self, validate_data):
         return Cricket_Question_and_Answer.objects.create(**validate_data)
     
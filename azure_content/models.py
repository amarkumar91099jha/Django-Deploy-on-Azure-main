from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=500, unique=True)
    description = models.CharField(max_length=500,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 
    


class BuildingAddress(models.Model):
    latitude=models.CharField(max_length=20, null=True)
    longitude=models.CharField(max_length=20, null=True)
    address = models.TextField(null=True)
    customer_type=models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    # Add other fields for user address
class IndividualCustomerData(models.Model):
    questions={
        "question-1":"What is the built up area of the building?",
        "question-2":"What is the age of the building?",
        "question-3":"What are the number of floors or storeys in the building?",
        "question-4":"What is your building structure?",
        "question-5":"What is the structural material of the walls of your building?",
        "question-6":"What is the structural material of the roof of your building?",
        "question-7":"What visible damage does the building have?",
        "question-8":"Number of buildings (density) within 100m perimeter of your building?",
        "question-9":"Are there any tall trees or high tension lines near your building that could fall during storm or cyclone?",
        
    }
    building_id=models.OneToOneField(BuildingAddress, on_delete=models.CASCADE)
    question_1=models.CharField(max_length=50,null=True)
    question_2=models.CharField(max_length=50,null=True)
    question_3=models.CharField(max_length=50,null=True)
    question_4=models.CharField(max_length=50,null=True)
    question_5=models.CharField(max_length=50,null=True)
    question_6=models.CharField(max_length=50,null=True)
    question_7=models.CharField(max_length=50,null=True)
    question_8=models.CharField(max_length=50,null=True)
    question_9=models.CharField(max_length=50,null=True)

class ResilianceCustomerData(models.Model):
        questions={
        "question-1":"What is the built up area of the building?",
        "question-2":"What is the age of the building?",
        "question-3":"What are the number of floors or storeys in the building?",
        "question-4":"What is your building structure?",
        "question-5":"What is the structural material of the walls of your building?",
        "question-6":"What is the structural material of the roof of your building?",
        "question-7":"What visible damage does the building have?",
        "question-8":"Number of buildings (density) within 100m perimeter of your building?",
        "question-9":"Are there any tall trees or high tension lines near your building that could fall during storm or cyclone?",
        
        }
        building_id=models.OneToOneField(BuildingAddress, on_delete=models.CASCADE)
        question_1=models.CharField(max_length=50, null=True)
        question_2=models.CharField(max_length=50, null=True)
        question_3=models.CharField(max_length=50,null=True)
        question_4=models.CharField(max_length=50,null=True)
        question_5=models.CharField(max_length=50,null=True)
        question_6=models.CharField(max_length=50,null=True)
        question_7=models.CharField(max_length=50,null=True)
        question_8=models.CharField(max_length=50,null=True)
        question_9=models.CharField(max_length=50,null=True)
        question_10=models.CharField(max_length=50,null=True)
        question_11=models.CharField(max_length=50,null=True)
        question_12=models.CharField(max_length=50,null=True)
        question_13=models.CharField(max_length=50,null=True)
        question_14=models.CharField(max_length=50,null=True)
        question_15=models.CharField(max_length=50,null=True)
        question_16=models.CharField(max_length=50,null=True)
        question_17=models.CharField(max_length=50,null=True)
        question_18=models.CharField(max_length=50,null=True)
        question_19=models.CharField(max_length=50,null=True)
        question_20=models.CharField(max_length=50,null=True)
        question_21=models.CharField(max_length=50,null=True)
        



    

    





from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.core.serializers.json import DjangoJSONEncoder
import json
from .models import *

# myapp/views.py
from django.http import JsonResponse
import os



class HomeView(ListView):
    context_object_name = 'project_list'
    model = BuildingAddress
    template_name = "DRF_App/home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        addresses = BuildingAddress.objects.all().values()
        addresses_json = json.dumps(list(addresses), cls=DjangoJSONEncoder)
        context['address'] = addresses_json
        return context

class AboutView(TemplateView):
    template_name = "DRF_App/about.html"

# class ProjectCreateView(CreateView):
#     model = Project
#     fields = ['name', 'description']
#     template_name = "DRF_App/create.html"
#     success_url ="/"

# class ProjectEditView(UpdateView):
#     model = BuildingAddress
#     fields = ['latitude','longitude','address','customer_type']
#     template_name = "DRF_App/create.html"
#     success_url ="/"

class ProjectDeleteView(DeleteView):
    model =BuildingAddress
    template_name = "DRF_App/delete.html"
    fields = ['id']
    success_url ="/"



def buildingAddress_input(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        address=request.POST.get('address')
        customer_type=request.POST.get('customer_type')
        # Add other fields as needed

        # Create or update UserAddress
        if latitude and longitude and address:
            building_address,created=BuildingAddress.objects.get_or_create(
                latitude = latitude,
                longitude = longitude,
                address=address,
                customer_type=customer_type

            )
        
            messages.success(request, 'Building Address collected successfully!')
            if customer_type=="Resilience AI Customer":
                return redirect('resiliance-views',building_id=building_address.id)
            else:
                return redirect('individual-views',building_id=building_address.id)

    return render(request, "DRF_App/create.html")

def buildingAddress_edit(request,building_id):
    building_addres=BuildingAddress.objects.get(id=building_id)
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        address=request.POST.get('address')
        customer_type=request.POST.get('customer_type')
        # Add other fields as needed

        # Create or update UserAddress
        # building_address=BuildingAddress.objects.get(id=building_id)
        if latitude and longitude and address:
            building_address,created=BuildingAddress.objects.get_or_create(id=building_id)
            building_address.latitude = latitude
            building_address.longitude = longitude
            building_address.address=address
            building_address.customer_type=customer_type
            building_address.save()


            
            print(latitude)
            messages.success(request, 'Building Address collected successfully!')
            if customer_type=="Resilience AI Customer":
                return redirect('resiliance-views',building_id=building_address.id)
            else:
                return redirect('individual-views',building_id=building_address.id)

    return render(request, "DRF_App/edit.html", {
        "building_id":building_id,
        "building_address":building_addres
    })


def IndividualView(request,building_id):
    building_location=BuildingAddress.objects.get(id=building_id)
    if request.method == 'POST':
        # Collect user address
        question1 = request.POST.get('question-1')
        question2 = request.POST.get('question-2')
        question3 = request.POST.get('question-3')
        question4 = request.POST.get('question-4')
        question5 = request.POST.get('question-5')
        question6 = request.POST.get('question-6')
        question7 = request.POST.get('question-7')
        question8 = request.POST.get('question-8')
        question9 = request.POST.get('question-9')

        # Add other fields as needed

        # Create or update UserAddress
        individual_data,created=IndividualCustomerData.objects.get_or_create(building_id=building_location)
        individual_data.question_1=question1
        individual_data.question_2=question2
        individual_data.question_3=question3
        individual_data.question_4=question4
        individual_data.question_5=question5
        individual_data.question_6=question6
        individual_data.question_7=question7
        individual_data.question_8=question8
        individual_data.question_9=question9
        individual_data.save()
        messages.success(request, 'Building Address collected successfully!')
        return redirect('home')

    return render(request, 'DRF_App/Individual.html',{
        "building_id":building_location.id
    })


def CustomerView(request, building_id):
    building_location=BuildingAddress.objects.get(id=building_id)
    if request.method == 'POST':
        # Collect user address
        question1 = request.POST.get('question-1')
        question2 = request.POST.get('question-2')
        question3 = request.POST.get('question-3')
        question4 = request.POST.get('question-4')
        question5 = request.POST.get('question-5')
        question6 = request.POST.get('question-6')
        question7 = request.POST.get('question-7')
        question8 = request.POST.get('question-8')
        question9 = request.POST.get('question-9')
        question10 = request.POST.get('question-10')
        question11 = request.POST.get('question-11')
        question12 = request.POST.get('question-12')
        question13 = request.POST.get('question-13')
        question14 = request.POST.get('question-14')
        question15 = request.POST.get('question-15')
        question16 = request.POST.get('question-16')
        question17 = request.POST.get('question-17')
        question18 = request.POST.get('question-18')
        question19 = request.POST.get('question-19')
        question20 = request.POST.get('question-20')
        question21 = request.POST.get('question-21')


        # Add other fields as needed

        # Create or update UserAddress
        customer_data,created=ResilianceCustomerData.objects.get_or_create(building_id=building_location)
        customer_data.question_1=question1
        customer_data.question_2=question2
        customer_data.question_3=question3
        customer_data.question_4=question4
        customer_data.question_5=question5
        customer_data.question_6=question6
        customer_data.question_7=question7
        customer_data.question_8=question8
        customer_data.question_9=question9
        customer_data.question_10=question10
        customer_data.question_11=question11
        customer_data.question_12=question12
        customer_data.question_13=question13
        customer_data.question_14=question14
        customer_data.question_15=question15
        customer_data.question_16=question16
        customer_data.question_17=question17
        customer_data.question_18=question18
        customer_data.question_19=question19
        customer_data.question_20=question20
        customer_data.question_21=question21
        customer_data.save()

        messages.success(request, 'Building Address collected successfully!')
        return redirect('home')

    return render(request, 'DRF_App/Resiliance.html',{
        "building_id":building_location.id
    })


def buildingAddress_details(request,building_id):
    building_detail=BuildingAddress.objects.get(id=building_id)
    if building_detail.customer_type=="Resilience AI Customer":
        try:
            building_details=ResilianceCustomerData.objects.get(building_id_id=building_id)
        except:
            building_details=None
    
    else:
        try:
            building_details=IndividualCustomerData.objects.get(building_id_id=building_id)
        except:
            building_details=None
    return render(request, "DRF_App/details.html",{
        "building_details":building_detail,
        "building_detail":building_details
    })


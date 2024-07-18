from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.core.serializers.json import DjangoJSONEncoder
import json
from .models import *
from django.http import HttpResponse
import csv

# myapp/views.py
from django.http import JsonResponse
import os
import geojson
from django.contrib.auth.decorators import login_required

def mumbai_geojson_view(request):
    geojson_file = os.path.join(os.path.dirname(__file__), 'static/azure_content/mumbai_final.geojson')
    if os.path.exists(geojson_file):
        with open(geojson_file, 'r') as f:
            geojson_data = json.load(f)
        return JsonResponse(geojson_data, safe=False)
    else:
        return HttpResponse("File not found.", status=404)

# decathalone--------------------------------------------------------
#flood---------------------------------------------------------------
def ahemdabad_flood_geojson_view(request):
    geojson_file = os.path.join(os.path.dirname(__file__), 'static/azure_content/Decathlone_flood/ahemdabad_final_house_level_4326.geojson')
    if os.path.exists(geojson_file):
        with open(geojson_file, 'r') as f:
            geojson_data = json.load(f)
        return JsonResponse(geojson_data, safe=False)
    else:
        return HttpResponse("File not found.", status=404)
def anubhava_flood_geojson_view(request):
    geojson_file = os.path.join(os.path.dirname(__file__), 'static/azure_content/Decathlone_flood/anubhava_final_house_level_4326.geojson')
    if os.path.exists(geojson_file):
        with open(geojson_file, 'r') as f:
            geojson_data = json.load(f)
        return JsonResponse(geojson_data, safe=False)
    else:
        return HttpResponse("File not found.", status=404)
def bangalore_flood_geojson_view(request):
    geojson_file = os.path.join(os.path.dirname(__file__), 'static/azure_content/Decathlone_flood/bangalore_final_house_level_4326.geojson')
    if os.path.exists(geojson_file):
        with open(geojson_file, 'r') as f:
            geojson_data = json.load(f)
        return JsonResponse(geojson_data, safe=False)
    else:
        return HttpResponse("File not found.", status=404)
def nolumbur_flood_geojson_view(request):
    geojson_file = os.path.join(os.path.dirname(__file__), 'static/azure_content/Decathlone_flood/nolumbur_final_house_level_4326.geojson')
    if os.path.exists(geojson_file):
        with open(geojson_file, 'r') as f:
            geojson_data = json.load(f)
        return JsonResponse(geojson_data, safe=False)
    else:
        return HttpResponse("File not found.", status=404)
def teynampet_flood_geojson_view(request):
    geojson_file = os.path.join(os.path.dirname(__file__), 'static/azure_content/Decathlone_flood/teynampet_final_house_level_4326.geojson')
    if os.path.exists(geojson_file):
        with open(geojson_file, 'r') as f:
            geojson_data = json.load(f)
        return JsonResponse(geojson_data, safe=False)
    else:
        return HttpResponse("File not found.", status=404)
def zirkapur_flood_geojson_view(request):
    geojson_file = os.path.join(os.path.dirname(__file__), 'static/azure_content/Decathlone_flood/Zirkapur_final_house_level_4326.geojson')
    if os.path.exists(geojson_file):
        with open(geojson_file, 'r') as f:
            geojson_data = json.load(f)
        return JsonResponse(geojson_data, safe=False)
    else:
        return HttpResponse("File not found.", status=404)



#heatwave------------------------------------------------------------
def ahemdabad_heatwave_geojson_view(request):
    geojson_file = os.path.join(os.path.dirname(__file__), 'static/azure_content/Decathlone/ahemdabad_final_house_level_4326.geojson')
    if os.path.exists(geojson_file):
        with open(geojson_file, 'r') as f:
            geojson_data = json.load(f)
        return JsonResponse(geojson_data, safe=False)
    else:
        return HttpResponse("File not found.", status=404)
def anubhava_heatwave_geojson_view(request):
    geojson_file = os.path.join(os.path.dirname(__file__), 'static/azure_content/Decathlone/anubhava_final_house_level_4326.geojson')
    if os.path.exists(geojson_file):
        with open(geojson_file, 'r') as f:
            geojson_data = json.load(f)
        return JsonResponse(geojson_data, safe=False)
    else:
        return HttpResponse("File not found.", status=404)
def bangalore_heatwave_geojson_view(request):
    geojson_file = os.path.join(os.path.dirname(__file__), 'static/azure_content/Decathlone/bangalore_final_house_level_4326.geojson')
    if os.path.exists(geojson_file):
        with open(geojson_file, 'r') as f:
            geojson_data = json.load(f)
        return JsonResponse(geojson_data, safe=False)
    else:
        return HttpResponse("File not found.", status=404)
def nolumbur_heatwave_geojson_view(request):
    geojson_file = os.path.join(os.path.dirname(__file__), 'static/azure_content/Decathlone/nolumbur_final_house_level_4326.geojson')
    if os.path.exists(geojson_file):
        with open(geojson_file, 'r') as f:
            geojson_data = json.load(f)
        return JsonResponse(geojson_data, safe=False)
    else:
        return HttpResponse("File not found.", status=404)
def teynampet_heatwave_geojson_view(request):
    geojson_file = os.path.join(os.path.dirname(__file__), 'static/azure_content/Decathlone/teynampet_final_house_level_4326.geojson')
    if os.path.exists(geojson_file):
        with open(geojson_file, 'r') as f:
            geojson_data = json.load(f)
        return JsonResponse(geojson_data, safe=False)
    else:
        return HttpResponse("File not found.", status=404)
def zirkapur_heatwave_geojson_view(request):
    geojson_file = os.path.join(os.path.dirname(__file__), 'static/azure_content/Decathlone/Zirkapur_final_house_level_4326.geojson')
    if os.path.exists(geojson_file):
        with open(geojson_file, 'r') as f:
            geojson_data = json.load(f)
        return JsonResponse(geojson_data, safe=False)
    else:
        return HttpResponse("File not found.", status=404)



#new----------------azure_content/
def mallofindi_heatwave_geojson_view(request):
    geojson_file = os.path.join(os.path.dirname(__file__), 'static/azure_content/mallofindia_Heatwave.geojson')
    if os.path.exists(geojson_file):
        with open(geojson_file, 'r') as f:
            geojson_data = json.load(f)
        return JsonResponse(geojson_data, safe=False)
    else:
        return HttpResponse("File not found.", status=404)
def mallofindi_heatwave_geojson_view(request):
    geojson_file = os.path.join(os.path.dirname(__file__), 'static/azure_content/mallofindia_Heatwave.geojson')
    if os.path.exists(geojson_file):
        with open(geojson_file, 'r') as f:
            geojson_data = json.load(f)
        return JsonResponse(geojson_data, safe=False)
    else:
        return HttpResponse("File not found.", status=404)
def mallofindi_heatwave_geojson_view(request):
    geojson_file = os.path.join(os.path.dirname(__file__), 'static/azure_content/mallofindia_Heatwave.geojson')
    if os.path.exists(geojson_file):
        with open(geojson_file, 'r') as f:
            geojson_data = json.load(f)
        return JsonResponse(geojson_data, safe=False)
    else:
        return HttpResponse("File not found.", status=404)
def mallofindi_heatwave_geojson_view(request):
    geojson_file = os.path.join(os.path.dirname(__file__), 'static/azure_content/mallofindia_Heatwave.geojson')
    if os.path.exists(geojson_file):
        with open(geojson_file, 'r') as f:
            geojson_data = json.load(f)
        return JsonResponse(geojson_data, safe=False)
    else:
        return HttpResponse("File not found.", status=404)
def mallofindi_heatwave_geojson_view(request):
    geojson_file = os.path.join(os.path.dirname(__file__), 'static/azure_content/mallofindia_Heatwave.geojson')
    if os.path.exists(geojson_file):
        with open(geojson_file, 'r') as f:
            geojson_data = json.load(f)
        return JsonResponse(geojson_data, safe=False)
    else:
        return HttpResponse("File not found.", status=404)
def mallofindi_heatwave_geojson_view(request):
    geojson_file = os.path.join(os.path.dirname(__file__), 'static/azure_content/mallofindia_Heatwave.geojson')
    if os.path.exists(geojson_file):
        with open(geojson_file, 'r') as f:
            geojson_data = json.load(f)
        return JsonResponse(geojson_data, safe=False)
    else:
        return HttpResponse("File not found.", status=404)




# new files
def mallofindia_flood_geojson_view(request):
    geojson_file = os.path.join(os.path.dirname(__file__), 'static/azure_content/mallofindia_flood.geojson')
    if os.path.exists(geojson_file):
        with open(geojson_file, 'r') as f:
            geojson_data = json.load(f)
        return JsonResponse(geojson_data, safe=False)
    else:
        return HttpResponse("File not found.", status=404)
def mallofindi_heatwave_geojson_view(request):
    geojson_file = os.path.join(os.path.dirname(__file__), 'static/azure_content/mallofindia_Heatwave.geojson')
    if os.path.exists(geojson_file):
        with open(geojson_file, 'r') as f:
            geojson_data = json.load(f)
        return JsonResponse(geojson_data, safe=False)
    else:
        return HttpResponse("File not found.", status=404)
def montera_flood_geojson_view(request):
    geojson_file = os.path.join(os.path.dirname(__file__), 'static/azure_content/motera_flood.geojson')
    if os.path.exists(geojson_file):
        with open(geojson_file, 'r') as f:
            geojson_data = json.load(f)
        return JsonResponse(geojson_data, safe=False)
    else:
        return HttpResponse("File not found.", status=404)
def montera_heatwave_geojson_view(request):
    geojson_file = os.path.join(os.path.dirname(__file__), 'static/azure_content/motera_heatwave.geojson')
    if os.path.exists(geojson_file):
        with open(geojson_file, 'r') as f:
            geojson_data = json.load(f)
        return JsonResponse(geojson_data, safe=False)
    else:
        return HttpResponse("File not found.", status=404)


# -------------------------------------------

# def lucknow_flood_geojson_view(request):
#     geojson_file = os.path.join(os.path.dirname(__file__), 'static/azure_content/lucknow_floood_final.geojson')
#     if os.path.exists(geojson_file):
#         with open(geojson_file, 'r') as f:
#             geojson_data = json.load(f)
#         return JsonResponse(geojson_data, safe=False)
#     else:
#         return HttpResponse("File not found.", status=404)

# def merut_flood_geojson_view(request):
#     geojson_file = os.path.join(os.path.dirname(__file__), 'static/azure_content/meerut_flood_final.geojson')
#     if os.path.exists(geojson_file):
#         with open(geojson_file, 'r') as f:
#             geojson_data = json.load(f)
#         return JsonResponse(geojson_data, safe=False)
#     else:
#         return HttpResponse("File not found.", status=404)


# def geojson_view(request):
#     geojson_file = os.path.join(os.path.dirname(__file__), 'static/azure_content/chennai_final_house_level_4326.geojson')
#     if os.path.exists(geojson_file):
#         with open(geojson_file, 'r') as f:
#             geojson_data = json.load(f)
#         return JsonResponse(geojson_data, safe=False)
#     else:
#         return HttpResponse("File not found.", status=404)

# def merut_geojson_view(request):
#     geojson_file = os.path.join(os.path.dirname(__file__), 'static/azure_content/merut_final_house_level_4326 .geojson')
#     if os.path.exists(geojson_file):
#         with open(geojson_file, 'r') as f:
#             geojson_data = json.load(f)
#         return JsonResponse(geojson_data, safe=False)
#     else:
#         return HttpResponse("File not found.", status=404)

# def lucknow_geojson_view(request):
#     geojson_file = os.path.join(os.path.dirname(__file__), 'static/azure_content/Lucknow_final_house_level_4326 .geojson')
#     if os.path.exists(geojson_file):
#         with open(geojson_file, 'r') as f:
#             geojson_data = json.load(f)
#         return JsonResponse(geojson_data, safe=False)
#     else:
#         return HttpResponse("File not found.", status=404)
    
# def katra_geojson_view(request):
#     geojson_file = os.path.join(os.path.dirname(__file__), 'static/azure_content/Katra_final_house_level_4326.geojson')
#     if os.path.exists(geojson_file):
#         with open(geojson_file, 'r') as f:
#             geojson_data = json.load(f)
#         return JsonResponse(geojson_data, safe=False)
#     else:
#         return HttpResponse("File not found.", status=404)

# def baramullah_geojson_view(request):
#     geojson_file = os.path.join(os.path.dirname(__file__), 'static/azure_content/baramullah_final_house_level_4326 .geojson')
#     if os.path.exists(geojson_file):
#         with open(geojson_file, 'r') as f:
#             geojson_data = json.load(f)
#         return JsonResponse(geojson_data, safe=False)
#     else:
#         return HttpResponse("File not found.", status=404)


def LandingView(request):
    project_list = BuildingAddress.objects.all()
    addresses_json = json.dumps(list(project_list.values()), cls=DjangoJSONEncoder)
    return render(request, "azure_content/landing.html",{
        'address': addresses_json,
        'project_list': project_list,
    })

# @login_required
def home_view(request):
    project_list = BuildingAddress.objects.all()
    addresses_json = json.dumps(list(project_list.values()), cls=DjangoJSONEncoder)
    context = {
        'project_list': project_list,
        'address': addresses_json,
    }
    return render(request, "azure_content/home.html", context)
class AboutView(TemplateView):
    template_name = "azure_content/about.html"

# class ProjectCreateView(CreateView):
#     model = Project
#     fields = ['name', 'description']
#     template_name = "azure_content/create.html"
#     success_url ="/"

# class ProjectEditView(UpdateView):
#     model = BuildingAddress
#     fields = ['latitude','longitude','address','customer_type']
#     template_name = "azure_content/create.html"
#     success_url ="/"

class ProjectDeleteView(DeleteView):
    model =BuildingAddress
    template_name = "azure_content/delete.html"
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

    return render(request, "azure_content/create.html")

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

    return render(request, "azure_content/edit.html", {
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

    return render(request, 'azure_content/Individual.html',{
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

    return render(request, 'azure_content/Resiliance.html',{
        "building_id":building_location.id
    })

@login_required
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
    return render(request, "azure_content/details.html",{
        "building_details":building_detail,
        "building_detail":building_details
    })

def MapView(request):
    return render(request,"azure_content/Map.html")

def export_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="combined_data.csv"'

    writer = csv.writer(response)
    # Write the header row
    writer.writerow([
        'Latitude', 'Longitude', 'Address', 'Customer Type', 'Building Created At', 'Building Updated At',
        'Individual Q1', 'Individual Q2', 'Individual Q3', 'Individual Q4', 'Individual Q5',
        'Individual Q6', 'Individual Q7', 'Individual Q8', 'Individual Q9',
        'Resilience Q1', 'Resilience Q2', 'Resilience Q3', 'Resilience Q4', 'Resilience Q5',
        'Resilience Q6', 'Resilience Q7', 'Resilience Q8', 'Resilience Q9', 'Resilience Q10',
        'Resilience Q11', 'Resilience Q12', 'Resilience Q13', 'Resilience Q14', 'Resilience Q15',
        'Resilience Q16', 'Resilience Q17', 'Resilience Q18', 'Resilience Q19', 'Resilience Q20', 'Resilience Q21'
    ])

    # Fetch data from the database
    for building in BuildingAddress.objects.all():
        individual_data = IndividualCustomerData.objects.filter(building_id=building).first()
        resilience_data = ResilianceCustomerData.objects.filter(building_id=building).first()

        writer.writerow([
            building.latitude, building.longitude, building.address, building.customer_type, building.created_at, building.updated_at,
            individual_data.question_1 if individual_data else '', individual_data.question_2 if individual_data else '', individual_data.question_3 if individual_data else '', individual_data.question_4 if individual_data else '', individual_data.question_5 if individual_data else '',
            individual_data.question_6 if individual_data else '', individual_data.question_7 if individual_data else '', individual_data.question_8 if individual_data else '', individual_data.question_9 if individual_data else '',
            resilience_data.question_1 if resilience_data else '', resilience_data.question_2 if resilience_data else '', resilience_data.question_3 if resilience_data else '', resilience_data.question_4 if resilience_data else '', resilience_data.question_5 if resilience_data else '',
            resilience_data.question_6 if resilience_data else '', resilience_data.question_7 if resilience_data else '', resilience_data.question_8 if resilience_data else '', resilience_data.question_9 if resilience_data else '', resilience_data.question_10 if resilience_data else '',
            resilience_data.question_11 if resilience_data else '', resilience_data.question_12 if resilience_data else '', resilience_data.question_13 if resilience_data else '', resilience_data.question_14 if resilience_data else '', resilience_data.question_15 if resilience_data else '',
            resilience_data.question_16 if resilience_data else '', resilience_data.question_17 if resilience_data else '', resilience_data.question_18 if resilience_data else '', resilience_data.question_19 if resilience_data else '', resilience_data.question_20 if resilience_data else '', resilience_data.question_21 if resilience_data else ''
        ])

    return response
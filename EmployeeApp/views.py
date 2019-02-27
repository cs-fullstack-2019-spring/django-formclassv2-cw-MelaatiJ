from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeApplicationForm


# Create your views here.

# my index function that routes to my index html
def index(request):
    return render(request, "EmployeeApp/index.html")


def apply(request):
    newApplicationForm = EmployeeApplicationForm()
    context = {
        "newForm": newApplicationForm
    }
    return render(request, "EmployeeApp/home.html", context)


def applicant(request):
    # if request.method == "POST":
        print(request.POST)  # print my post in terminal
        context = {  # going to inject this information into my applicant page
            "name": request.POST["name"],
            "date_of_birth": request.POST["date_of_birth"],
            "position": request.POST["position_applying"],
            "salary": request.POST["salary"],

        }  # if there is no post it will send it back to the home page
        return render(request, "EmployeeApp/applicant.html", context)  # if it does it will send you to the applicant page

# def applicant(request):
#     return render(request, "EmployeeApp/applicant.html")

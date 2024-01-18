from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def add_lead(request):
    return render(request, 'lead/add_lead.html')
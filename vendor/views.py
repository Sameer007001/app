from django.shortcuts import render
from vendor.models import Vendor
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request, 'vendor/vendor.html')

@csrf_exempt
def insertVendor(request):
    Vendor().insertVendor(request.POST.dict())
    return HttpResponseRedirect('signup')
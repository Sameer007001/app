from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request, 'manbot/home.html')

# @csrf_exempt
# def insertPromoter(request):
#     Promoter().insertPromoter(request.POST.dict())
#     return HttpResponseRedirect('signup')


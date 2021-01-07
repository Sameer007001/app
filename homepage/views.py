from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request, 'homepage/home.html')

def category(request, service_user, category):
    return render(request, 'homepage/category.html', {'service_user': service_user, 'category': category})

# @csrf_exempt
# def insertPromoter(request):
#     Promoter().insertPromoter(request.POST.dict())
#     return HttpResponseRedirect('signup')


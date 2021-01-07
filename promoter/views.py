from django.shortcuts import render
from promoter.models import Promoter
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request, 'promoter/promoter.html')

@csrf_exempt
def insertPromoter(request):
    Promoter().insertPromoter(request.POST.dict())
    return HttpResponseRedirect('signup')

@csrf_exempt
def promoterLogin(request):
    return render(request, 'promoter/promoter_login.html')

@csrf_exempt
def do_promoterLogin(request):
    res = Promoter().promoterLogin(request.POST.dict())
    goto = '/' if res else 'login'
    return HttpResponseRedirect(goto)

    
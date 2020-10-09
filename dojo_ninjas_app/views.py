from django.shortcuts import render, redirect
from .models import Dojo, Ninja

# Create your views here.
def index(request):
    print(Dojo.objects.last().ninjas)
    context = {
        'all_dojos': Dojo.objects.all()
    }
    return render(request, 'index.html', context)

def process_dojo(request):
    Dojo.objects.create(
        name=request.POST['name'],
        city=request.POST['city'],
        state=request.POST['state']
    )
    return redirect('/')

def process_ninja(request):
    Ninja.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        enroled=Dojo.objects.get(id=request.POST['dojo_id'])
    )
    return redirect('/')
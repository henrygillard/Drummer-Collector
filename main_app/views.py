from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .forms import SponsorForm
from .models import Drummer, Drum, Sponsor 
# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, "about.html")

def drummers_index(request):
  drummers = Drummer.objects.all()
  return render(request, "drummers/index.html", { "drummers": drummers})

def drummers_detail(request, drummer_id):
  drummer = Drummer.objects.get(id=drummer_id)
  drums_drummer_doesnt_have = Drum.objects.exclude(id__in=drummer.drums.all().values_list('id'))
  sponsor_form = SponsorForm()
  return render(request, "drummers/detail.html", { 
    "drummer": drummer, 
    "sponsor_form": sponsor_form,
    "drums": drums_drummer_doesnt_have,
    })

def add_sponsor(request, drummer_id):
  form = SponsorForm(request.POST)
  if form.is_valid():
    new_sponsor = form.save(commit=False)
    new_sponsor.drummer_id = drummer_id
    new_sponsor.save()
  return redirect('detail', drummer_id=drummer_id)

class DrumList(ListView):
  model = Drum

class DrummerCreate(CreateView):
  model = Drummer
  fields = "__all__"
  success_url = "/drummers/"
    
class DrummerUpdate(UpdateView):
  model = Drummer
  fields = "__all__"
  success_url = "/drummers/"
  

class DrummerDelete(DeleteView):
  model = Drummer
  success_url = "/drummers/"
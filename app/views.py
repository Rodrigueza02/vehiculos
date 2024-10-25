from django.shortcuts import render, HttpResponseRedirect

# Create your views here.



from .models import vehicle
from .forms import VehicleForm

def create_view(request):
    context = {}
    form = VehicleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")

    context['form']= form
    return render(request, "create_view.html", context)


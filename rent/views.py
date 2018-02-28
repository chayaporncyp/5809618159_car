from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Car,Rent,Returncar
from .forms import RentForm,CarForm,ReturnForm

# Create your views here.
def home(request):
	print(HttpResponse('Hello World'))
	return HttpResponse('Hello World')

class CarListView(ListView):
    model = Car
    template_name='carlist.html'

class RentCar(CreateView):
	queryset = Rent()
	template_name = 'rentcar.html'
	form_class = RentForm
	success_url = '/admin'
class ReturnCar(CreateView):
	queryset = Returncar()
	template_name = 'returncar.html'
	form_class = ReturnForm
	success_url = '/admin'














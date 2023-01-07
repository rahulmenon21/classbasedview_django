from django.shortcuts import render
from django.views.generic import TemplateView,FormView,CreateView,ListView,DeleteView,UpdateView
from .models import *

# Create your views here.
def home(request):
    return render(request,'home.html')

class Python(TemplateView):
    template_name = 'python.html'

class Java(TemplateView):
    template_name = 'java.html'

class AddEmp(FormView):
    form_class = Empform
    template_name = 'Addemp.html'

class Adddata(CreateView):
    model = Employee
    fields = '__all__'
    success_url = '/'

class Emplist(ListView):
    model = Employee
    template_name = 'emplist.html'

class Delete(DeleteView):
    model = Employee
    success_url = '/emplist'

class Delete2(DeleteView):
    model = Employee
    template_name = 'delete2.html'
    success_url = '/elist.html'

class Edit(UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'edit.html'
    success_url = '/emplist'
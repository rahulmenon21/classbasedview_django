from django.urls import path
from .import views as v
from django.views.generic import TemplateView

urlpatterns = [
    path('',v.home),
    path('py',v.Python.as_view()),
    path('java',v.Java.as_view()),
    path('js',TemplateView.as_view(template_name='js.html')),
    path('addemp',v.AddEmp.as_view()),
    path('adddata',v.Adddata.as_view()),
    path('emplist',v.Emplist.as_view()),
    path('delete/<int:pk>',v.Delete.as_view()),
    path('delete2/<int:pk>',v.Delete2.as_view()),
    path('edit/<int:pk>',v.Edit.as_view())
]
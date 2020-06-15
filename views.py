from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from . import models

# Create your views here.
#
class IndexView(TemplateView):
    template_name = 'index.html'

#
#     def get_context_data(self,**kwargs):
#         context = super().get_context_data(**kwargs)
#         context['injectme'] = 'BASIC INJECTION!'
#         return context





class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    #returns a lsit of school_list

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_adv/school_detail.html'

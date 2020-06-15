from django.urls import path
from basic_adv import views
from .views import SchoolDetailView,SchoolListView


app_name = 'basic_adv'

urlpatterns = [
    path('',views.SchoolListView.as_view(),name='list'),
    path('<slug:slug>',views.SchoolDetailView.as_view(),name='detail')
]

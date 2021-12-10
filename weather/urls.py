from django.urls import path
from . import views

app_name = 'weather'

urlpatterns = [
    path('',views.index,name="index"),    
    #path('news', views.news, name="news"),
    path('<int:year>/<int:month>/<int:day>/<slug:details>', views.detail, name="details"),
    path('contact', views.contact, name="contact")
]

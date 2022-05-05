

from django.urls import path,include
from FourthModule import views

urlpatterns = [
    
path('',views.fourthHome,name="fourth"),
path('addtask',views.addtask,name="addtask"),

]

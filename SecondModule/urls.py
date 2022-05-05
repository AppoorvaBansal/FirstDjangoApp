
from SecondModule import views
from django.urls import path


urlpatterns = [
    
path('',views.secondModule,name='secondModule'),
path('delete/<user_id>',views.deleteUser,name='deleteUser'),
path('edit/<user_id>',views.editUser,name='editUser'),
path('about-us-only',views.aboutus,name='aboutus'),
path('addEvent',views.addEvent,name='addEvent')

]

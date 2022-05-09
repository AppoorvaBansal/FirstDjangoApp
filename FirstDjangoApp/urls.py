
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
from SecondModule import views as Second_view
from FirstModule import views as first_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/',include('FirstModule.urls')),
    path('second/',include('SecondModule.urls')),
    path('fourth/',include('FourthModule.urls')),
    path('about-us-only/',Second_view.aboutus,name='aboutus'),
    path('index/',Second_view.index,name='index'),
   # path('third/',include('ThirdModule.urls'))
]

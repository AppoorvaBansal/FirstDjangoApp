
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/',include('FirstModule.urls')),
    path('second/',include('SecondModule.urls')),
    path('fourth/',include('FourthModule.urls'))
   # path('third/',include('ThirdModule.urls'))
]

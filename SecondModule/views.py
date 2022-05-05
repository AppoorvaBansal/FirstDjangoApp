from email import message
from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render

from SecondModule.models import UserData
from SecondModule.forms import UserForm
from django.contrib import messages

# Create your views here.
def secondModule(request):
     if request.method=="POST":
          form=UserForm(request.POST or None)
          if form.is_valid():
               form.save()
          print("DONE2") 
          messages.success(request,("ADD SUCCESSFULLY!!"))
          return redirect("secondModule")
          
     else:
          allUserdata=UserData.objects.all
          return render(request,'SecondHome.html',{"allUser":allUserdata})

def deleteUser(request,user_id):
    Userdetail=UserData.objects.get(pk=user_id)
    Userdetail.delete()

    return redirect('secondModule')

def editUser(request,user_id):
      if request.method=="POST":
          UserDetail=UserData.objects.get(pk=user_id)
          form=UserForm(request.POST or None,instance=UserDetail)
          if form.is_valid():
               form.save()


          messages.success(request,("USER EDIT SUCCESSFULLY"))
          return redirect("secondModule")
      else:
          UserDetail=UserData.objects.get(pk=user_id)
          return render(request,'editUser.html',{"UserDetail":UserDetail})


#      allUserdata=UserData.objects.all

#     # context={'texthome':"WELCOME HOME PAGE"}
#      return render(request,'SecondHome.html',{"allUser":allUserdata})
#      #return HttpResponse("SECOND MODULE HOME PAGE")

# Create your views here.
def addEvent(request):
     context={'texthome':"WELCOME HOME PAGE"}
     return render(request,'addevent.html',context)
     #return HttpResponse("SECOND MODULE HOME PAGE")

def aboutus(request):
     context={'textabout':"ABOUT US PAGE"}
     return render(request,'SecondAboutUS.html',context)
     #return HttpResponse("SECOND MODULE ABOUT US PAGE")

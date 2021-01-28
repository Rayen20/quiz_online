from django.shortcuts import render, redirect 

from Examen.models import  Questions,Examen
from Examen.forms import ExamenForm ,QuestionForm


# Creer vos views.




# Create : créer un nouveau  examen.

def create(request): 


    if request.method == "POST":  
        form = ExamenForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = ExamenForm()  
    return render(request,'create.html',{'form':form})

# Createq : créer les questions d'un examen.

def createq(request, id):  
    ex = Examen.objects.get(id=id)  
    if request.method == "POST":
        form = QuestionForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = QuestionForm()  
              
         
         
    return render(request,'createq.html', {'form':form,'ex':ex})

# show : afficher tous les examens disponibles .

def show(request):  
    examen = Examen.objects.all()  
    return render(request,"show.html",{'examen':examen})  
# quiz : afficher le quiz donnée pour chaque examen .
def quiz(request, id):
   #  examenn = Examen.objects.get(id=id)
     q = Examen.objects.get(id=id)
     question = Questions.objects.all().filter(examen= id)
    #ex = Examen.objects.filter( examen__question='Tech' )
     return render(request,"quiz.html",{'question':question})   


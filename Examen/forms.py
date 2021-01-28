from django import forms  

from Examen.models import Examen ,Questions


class ExamenForm(forms.ModelForm):  
    class Meta:  
        model = Examen  
        fields =  [ 
            "titre", 
            "etat" ,
          
            
        ]

class QuestionForm(forms.ModelForm):  
    class Meta:  
        model = Questions 
        fields =  [ 
            "question",
            "option1",
            "option2",
            "option3",
            "option4",
            "corrans",
            "examen",
        ]  


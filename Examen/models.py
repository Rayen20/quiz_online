from django.db import models

# Creer vos modéles.



# Examen model.
class Examen(models.Model):  
   
   
    A = 'Activé'
    D = 'Desactivé'
    CHOICES_A = (
        (A, A),
        (D, D),
      
    )

	
    titre = models.CharField(max_length=255)
    
    etat = models.CharField(max_length=255,choices=CHOICES_A )  

   
    class Meta:  
        db_table = "examen"

# Questions model.

class Questions(models.Model):  
   
  
# Crea
	
    question = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    corrans = models.CharField(max_length=255)
    examen = models.ForeignKey(to=Examen, on_delete=models.CASCADE)
  
   

   
    
    class Meta:  
        db_table = "questions"


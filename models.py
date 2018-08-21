from __future__ import unicode_literals
import random

from django.db import models

class Joueur(models.Model):
    name = models.CharField("Nom",max_length=50)
    character_name = models.CharField("Nom du personnage", max_length=30)

    def __str__(self): 
        return self.name

class Piste(models.Model):
    letter = models.CharField("Lettre", max_length=5)
    title  = models.CharField("Titre", max_length=100)

    def __str__(self):
        return self.letter + " : " + self.title

class Enquete(models.Model):
    NIVEAU_CHOICES = (
            ('1', '1'),
            ('2', '2'),
            ('3', '3')
        )
    niveau = models.CharField('Niveau', max_length=1,choices=NIVEAU_CHOICES)
    joueur = models.ForeignKey(Joueur)
    piste  = models.ForeignKey(Piste)

    def status(self,points):
        self.dice = random.randint(1, 6)
        self.points = points
        if ((self.dice == 1) or ((self.dice + points - 1) == 1)):
            self.niveau = '1'
        elif ((self.dice + points - 1) >= 6):
            self.niveau = '3'
        else: 
            self.niveau = '2'

    def interception(self):
        self.interceptions = Interception.objects.filter(target = self.joueur.id, done = False)
        self.intercepted = False
        if (len(self.interceptions) > 0):
            for interception in self.interceptions:
                interception.done = True
                interception.save()
                # Reussi
                if interception.resultat == '0':
                   e = Enquete()
                   e.niveau = self.niveau
                   e.joueur = Joueur.objects.get(id = interception.origin.id)
                   e.piste  = self.piste
                   e.save()
                self.intercepted = self.intercepted or (interception.resultat == '0')
            
class Interception(models.Model):
    RESULTAT_TYPE = (
            ('0', 'Reussi'),
            ('1', 'Rate'),
            ('2', 'Rate, cible au courant')
        )
    origin = models.ForeignKey(Joueur,related_name="origin")
    target = models.ForeignKey(Joueur,related_name="target")
    resultat = models.CharField('Resultat', max_length=1,choices=RESULTAT_TYPE,null=True,blank=True)
    done = models.NullBooleanField('termine',default=False)

    def status(self):
        self.dice = random.randint(1, 6)
        if (self.dice == 1):
            self.resultat = '2'
        elif (self.dice  == 2):
            self.resultat = '1'
        else: 
            self.resultat = '0'



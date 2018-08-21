from django import forms

from .models import Enquete,Interception,Joueur

class EnqueteForm(forms.ModelForm):
    pointsChoices= ( (x,str(x)) for x in range(1,7))
    points = forms.ChoiceField(label = "Nombre de points pariés (y compris le 1er point de l'enquete)", choices = pointsChoices);

    class Meta:
        model = Enquete
        fields = ( 'joueur', 'piste')

class CategoryChoiceField(forms.ModelChoiceField):
     def label_from_instance(self, obj):
         return "Category: {}".format(obj.name)

class InterceptionForm(forms.ModelForm):
    field_order = [ 'type', 'origin', 'target', 'points' ]

    targetChoices= ( (x.id,x.character_name) for x in Joueur.objects.all())
    target = forms.ChoiceField(label = "Joueur cible", choices = targetChoices)

    class Meta:
        model = Interception
        fields = ( 'origin', )

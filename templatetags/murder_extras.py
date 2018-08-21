from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def getEnquete(context,joueur,piste):
    return " / ".join(context["enquete_list"].get((joueur,piste),""))


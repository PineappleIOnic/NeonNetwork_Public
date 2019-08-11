from django import template
from users.models import CustomUser

register = template.Library()

@register.filter(name='id_2_username')
def id_2_username(id): # Only one argument.
    try:
        id = str(id)
        obj = CustomUser.objects.get(pk=id)
        UserConv = str(obj.username)

    except CustomUser.DoesNotExist:
        raise Http404("No MyModel matches the given query.")

    return UserConv

@register.filter(name='username_2_id')
def username_2_id(username): # Only one argument.
    try:
        username = str(username)
        obj = CustomUser.objects.get(username=username)
        IdConv = str(obj.pk)

    except CustomUser.DoesNotExist:
        raise Http404("No MyModel matches the given query.")

    return IdConv

@register.filter(name='id_2_image')
def id_2_image(id): # Only one argument.
    try:
        print("ID IS: ",id)
        id = str(id)
        obj = CustomUser.objects.get(pk=id)
        UserConv = str(obj.docfile)

    except CustomUser.DoesNotExist:
        raise Http404("No MyModel matches the given query.")

    return UserConv

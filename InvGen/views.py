from django.shortcuts import render
from django.http import HttpResponse
import random
import string
from django.shortcuts import redirect
from .models import InviteCodes


# Dictionary for easy_code
EasyDict = ["ocean","neon","news","enrich","window","scarce","muffled","dad","form","state","home","interest","large","person","public","child","develop","day","find","why","against","time","dinkster","doge","nyan","work","clan","tribe","snail","sneak"]


from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')

# Create your views here.
def invite_gen(request):
    output = "neoninv"
    if not request.user.is_authenticated:
        return redirect('/')
    N = 4
    for x in range(N):
        output = output + "-" + (str(EasyDict[random.randint(0,(len(EasyDict) - 1))]))

    InviteDB = InviteCodes(inviteCode=output)
    InviteDB.save()
    return render(request, 'invite_gen.html', {'InvCode': output,})

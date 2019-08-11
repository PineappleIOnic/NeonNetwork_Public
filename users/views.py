from django.shortcuts import render
from .forms import InviteAuth

# Create your views here.

def invite_chk(request):
    form = InviteAuth()
    return render(request, 'invite_check.html', {'form': form})

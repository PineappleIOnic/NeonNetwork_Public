from django.views.generic import TemplateView
from users.models import CustomUser
from django.shortcuts import render, get_object_or_404, redirect
from InvGen.models import InviteCodes
from friendship.models import Friend

class HomeMobilePageView(TemplateView):
    template_name = 'pages/mobilehome.html'

def HomePageView(request):
        return render(request, 'pages/home.html')

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class NoPageView(TemplateView):
    template_name = 'pages/404.html'

class SettingsView(TemplateView):
    template_name = 'pages/settings.html'

class TermsView(TemplateView):
    template_name = 'pages/terms.html'

class invite_view(TemplateView):
    template_name = 'pages/invitecheck.html'


def profile_view(request, id):
    user = get_object_or_404(CustomUser, pk=id)
    return render(request, 'pages/profile.html', {"id":id, 'user':user})

def invite_check(request, invitecode):
    try:
        InviteCode = InviteCodes.objects.get(inviteCode=invitecode)
        InviteCode = InviteCodes.objects.get(inviteCode=invitecode).delete()
        return redirect('/accounts/signup/')
    except:
        return render(request, 'pages/invitewrong.html', {'invitecode':invitecode})

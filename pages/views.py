from django.views.generic import TemplateView

class HomeMobilePageView(TemplateView):
    template_name = 'pages/mobilehome.html'

class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class NoPageView(TemplateView):
    template_name = 'pages/404.html'

class SettingsView(TemplateView):
    template_name = 'pages/settings.html'

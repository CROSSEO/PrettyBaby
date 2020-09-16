from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class LandingPage(TemplateView):
    template_name = 'pretty_baby/index-2.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, {})


class Terms(TemplateView):
    template_name = 'pretty_baby/terms.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, {})


class Privacy(TemplateView):
    template_name = 'pretty_baby/privacy.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, {})

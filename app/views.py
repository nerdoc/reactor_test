from django.shortcuts import render
from django.views.generic import TemplateView


class ReactorView(TemplateView):
    template_name = "reactor.html"

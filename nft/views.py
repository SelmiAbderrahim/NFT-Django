from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import AvatarForm
from .utils import generate_avatars

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = AvatarForm()
        return context

    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context = generate_avatars(self.request, context)
        context["form"] = AvatarForm()

        return self.render_to_response(context)
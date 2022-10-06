from pipes import Template
from django.shortcuts import render
from django.views import View
# view class to handle requests
from django.http import HttpResponse
# class to handle sending a type of a response
from django.views.generic.base import TemplateView
from .models import Bird
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class BirdsList(TemplateView):
    template_name = "birds_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to get the query parameter we have to access it in the request.GET dictionary object        
        name = self.request.GET.get("name")
        # If a query exists we will filter by name 
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["birds"] = Bird.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["birds"] = Bird.objects.all()
            context["header"] = "Popular Birds"
        return context

class BirdsCreate(CreateView):
    model = Bird
    fields = ['name', 'img', 'bio']
    template_name = "birds_create.html"
    def get_success_url(self):
        return reverse('birds_detail', kwargs={'pk': self.object.pk})

class BirdsDetail(DetailView):
    model = Bird
    template_name = "birds_detail.html"

class BirdsUpdate(UpdateView):
    model = Bird
    fields = ['name', 'img', 'bio']
    template_name = "birds_update.html"
    def get_success_url(self):
        return reverse('birds_detail', kwargs={'pk': self.object.pk})

class BirdsDelete(DeleteView):
    model = Bird
    template_name = "birds_delete_confirmation.html"
    success_url = "/birds/"
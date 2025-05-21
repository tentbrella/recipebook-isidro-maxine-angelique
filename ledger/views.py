from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from ledger.models import Recipe, RecipeImage
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .forms import RecipeForm

class RecipeBookView(ListView):
    model = Recipe
    template_name = 'list.html'
    context_object_name = 'recipes'
    
class RecipeView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'detail.html'
    context_object_name = 'recipe'
    redirect_field_name = '/ledger/recipes/list'
    success_url = 'ledger:recipe'

class RecipeAddView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'create.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RecipeForm()
        return context
    def post(self, request, *args, **kwargs):
        form = RecipeForm(request.POST)
        if form.is_valid():
            art = Recipe()
            art.author = self.request.user.profile
            art.name = form.cleaned_data.get('name')
            art.save()
            return self.get(request, *args, **kwargs)
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)

class RecipeImageView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    template_name = 'create.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RecipeForm()
        return context
    def form_valid(self, form):
        pk = self.kwargs['pk']
        form.instance.thread = Recipe.objects.get(pk=pk)
        form.save()
        success_url = reverse_lazy("ledger:recipe", kwargs={'pk': pk})
        return redirect(success_url)

def index(request):
    return HttpResponse('Hello World! This came from the index view')

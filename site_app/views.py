from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import RegisterUserForm, RecipeForm
from .models import RecipeModel


def index(request):
    recipes = RecipeModel.objects.order_by('?')[:5]
    return render(request, 'site_app/index.html', {'recipes': recipes})


@login_required
def welcome(request):
    return render(request, 'welcome.html')


def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('welcome')
    else:
        form = RegisterUserForm()

    context = {'form': form}
    return render(request, 'register.html', context)


class UserLoginView(LoginView):
    template_name = 'login.html'  # Шаблон для отображения формы
    redirect_authenticated_user = True  # Перенаправить, если пользователь уже вошёл
    success_url = reverse_lazy('index')  # Перенаправление после входа


@login_required
def create_recipe(request):
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, request.FILES)

        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('index')
    else:
        recipe_form = RecipeForm()

    return render(request, 'site_app/create_recipe.html', {'recipe_form': recipe_form})


@login_required
def recipe_detail(request, pk):
    recipe = get_object_or_404(RecipeModel, pk=pk)
    return render(request, 'site_app/recipe_detail.html', {'recipe': recipe})


@login_required
def edit_recipe(request, pk):
    recipe = get_object_or_404(RecipeModel, pk=pk)

    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, request.FILES, instance=recipe)

        if recipe_form.is_valid():
            recipe = recipe_form.save()
            return redirect('recipe_detail', pk=recipe.id)
    else:
        recipe_form = RecipeForm(instance=recipe)

    return render(request, 'site_app/edit_recipe.html', {'recipe_form': recipe_form})


@login_required
def edit_recipe_list(request):
    recipes = RecipeModel.objects.filter(author=request.user)
    return render(request, 'site_app/edit_recipe_list.html', {'recipes': recipes})

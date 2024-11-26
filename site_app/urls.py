from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import index, register, welcome, create_recipe, UserLoginView, recipe_detail, edit_recipe, edit_recipe_list
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('welcome/', welcome, name='welcome'),
    path('create/', create_recipe, name='create_recipe'),
    path('recipe/<int:pk>/', recipe_detail, name='recipe_detail'),
    path('edit/', edit_recipe_list, name='edit_recipe_list'),
    path('edit_recipe/<int:pk>/', edit_recipe, name='edit_recipe'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

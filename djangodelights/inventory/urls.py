from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('ingredients/', views.IngredientsList.as_view(), name='ingredients_list'),
    path('ingredients/add', views.IngredientsAdd.as_view(), name ='ingredients_add'),
    path('ingredients/<slug:pk>/update', views.IngredientUpdate.as_view(), name ='ingredients_update'),
    path('menu/', views.MenuList.as_view(), name='menu'),
    path('menu/add_item', views.MenuItemAdd.as_view(), name='menu_item_add'),
    path('menu/add_recipe', views.MenuRecipeAdd.as_view(), name='recipe_add'),
    path('purchases/', views.PurchasesList.as_view(), name='purchases'),
    path('purchases/add', views.PurchaseAdd.as_view(), name='purchases_add'),
    path('report/', views.ReportView.as_view(), name = 'report'),
    path('accounts/login/', auth_views.LoginView.as_view(), name="login"),
    path("logout/", views.log_out, name="logout")
]

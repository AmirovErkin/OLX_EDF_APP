from django.urls import path
from .views import Home, adding_product, profile, shop_box, show_box, homes, vegas, car, jobs, animalss, other

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('profile/', profile, name='profile'),
    path('shopping/', shop_box, name='shop_box'),
    path('new/', adding_product, name='add'),
    path('show/<int:task_id>/', show_box, name='show'),
    path('all/', vegas, name='baby'),
    path('home/', homes, name='house'),
    path('car/', car, name='car'),
    path('job/', jobs, name='job'),
    path('animals/', animalss, name='animals'),
    path('other/', other, name='other'),
]

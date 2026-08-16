from . import views
from django.urls import path
urlpatterns =[
    path('index/<int:id>', views.index, name="index"),
    path('', views.home, name="home"),
    path('show/<int:id>', views.show, name="show"),
    path('feedback/', views.feedback, name="feedback"),
    path('register', views.register),
    path('show1', views.show1,  name="show1"),
    path('delete/<int:id>', views.destroy),
    path('compare/', views.compare, name="compare"),
    path('Comp_result', views.Comp_result),
]

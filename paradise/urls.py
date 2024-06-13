from django.urls import path
from . import views  


urlpatterns = [
    path('', views.index, name='index'),
    path('characters/', views.characters, name='characters'),
    path('quiz/', views.quiz, name='quiz'),
    path('merch/<int:id>/', views.merch_detail, name='merch_detail'),
    path('merch/delete/<int:id>/', views.delete_merch, name='delete_merch'),
    path('merch/add/', views.add_merch, name='add_merch'),  
    path('merch/edit/<int:id>/', views.edit_merch, name='edit_merch'),  
    path('merch/', views.merch, name='merch'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),
]

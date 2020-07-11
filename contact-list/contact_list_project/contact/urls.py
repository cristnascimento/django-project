from django.urls import path

from . import views

urlpatterns = [
    path('list', views.list, name='list'),
    path('add', views.add, name='add'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('view/<int:id>', views.view, name='view'),
    path('post', views.post, name='post'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('', views.index, name='index'),
]
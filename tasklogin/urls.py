
from django.urls import path,include
from tasklogin import views

urlpatterns = [
    path('add/',views.add,name='add'),
    path('show/',views.show,name='show'),
    path('edit/<int:PhoneNo>/',views.edit,name='edit'),
    path('update/<int:PhoneNo>/',views.update,name='update'),
    path('delete/<int:PhoneNo>/',views.destroy,name='delete')
]
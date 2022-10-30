from . import views
from django.urls import path,include

urlpatterns =[

    path('',views.translator_view,name='translator_view'),

]
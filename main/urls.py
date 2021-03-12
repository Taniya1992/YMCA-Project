
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import  *

urlpatterns = [
    path('',views.index,name ='home'),
        path('signup/', signup_view, name="signup"),
        path('addprogram/',addprogram, name="add program"),
        path('allprogram/',allprogram, name="all program"),
        path('alluser/',alluser, name="all user"),
        
        path('program/<str:myid>',program, name="program"),
        path('Registrations/',Registrations, name="Registrations"),
        path('program/<str:pn>/<str:pid>/programregister',programregister, name="programregister"),

        # path('logout/', logout_request, name="logout"),
]
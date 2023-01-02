
from django.urls import path
from .views import studlist,studDetails

urlpatterns = [
   
   path('studlist/', studlist.as_view()),
   path('studDetails/<int:pk>/', studDetails.as_view())
    
]

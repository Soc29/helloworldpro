from django.urls import path
from .views import helloworldfunc,IndexView


urlpatterns = [
    path('',IndexView.as_view()),
    path('helloworldapp/',helloworldfunc),
    
]

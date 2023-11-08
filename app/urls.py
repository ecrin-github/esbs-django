from django.urls import path
from app.views import *


urlpatterns = [
    path('send-email', EmailSender.as_view()),
    path('statistics', RmsStatistics.as_view())
]

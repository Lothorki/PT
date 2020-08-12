from django.urls import path, include
from mall import views
urlpatterns = [
	path('hello/', views.hello),
	path('hello2/', views.hello2),
]
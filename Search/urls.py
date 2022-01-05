from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from Search import views


# router = routers.DefaultRouter()
# router.register(r'results/<str:query>', views.SearchResultApi)

urlpatterns = [
    path('results/<str:query>', views.SearchResultApi)
]

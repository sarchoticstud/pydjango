from django.urls import path
# from api.views import Index
from api.views import article_list, article_details

urlpatterns = [
    # path("", Index),
    path('articles/', article_list),
    path('articles/<int:pk>/', article_details),
]

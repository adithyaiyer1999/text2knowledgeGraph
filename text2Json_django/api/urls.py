from django.urls import path
from . import views

urlpatterns = [
    path('join-text/', views.joinText, name='join-text'),
    path('call-openai/', views.callOpenAI, name='call-openai'),
    path('create-graph-from-text/', views.createGraphFromText, name='create-graph-from-text'),
    path('create-graph-from-pdf/', views.createGraphFromPdf, name='create-graph-from-pdf'),
    path('add-to-graph-from-text/', views.addToGraphFromText, name='add-to-graph-from-text'),
    path('search-graph-from-text/', views.searchGraphFromText, name='search-graph-from-text'),
]

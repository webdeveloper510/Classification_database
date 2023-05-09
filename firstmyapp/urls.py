from django.urls import path ,include
from .views import *
urlpatterns = [
     path('text/', Inputfunction.as_view()),
     path('technology-webscrap/',WebScrapDataView.as_view(),name='scrap'),
     path('mobile-technology-webscrap/',WebScrapingView.as_view(),name='scrap'),
     path('get_mobile/',Mobile_Technology_WavesView.as_view(),name='scrap'),
     path('get_tech/',TechnologiesView.as_view(),name='scrap'),
     path('cricketscraping/',CricketScrapingView.as_view(),name='scraps')
]


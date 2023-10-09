from django.urls import path

from .views import RawAPIView, RawExcelAPIView, ReportAPIView


app_name = 'stats'

urlpatterns = [
    path('raw/', RawAPIView.as_view()),
    path('report/', ReportAPIView.as_view()),
    path('fromexcel/', RawExcelAPIView.as_view())
]

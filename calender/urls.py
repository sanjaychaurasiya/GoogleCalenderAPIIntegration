from django.urls import path
from . import views


urlpatterns = [
    path('v1/calendar/init/', views.google_calendar_init_view, name='calender_permission'),
    path('v1/calendar/redirect/', views.google_calendar_redirect_view, name='google_redirect')
]
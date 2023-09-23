from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='all-meetups'),
    path('meetup/<slug:meetup_slug>/success', views.confirm_registration, name='confirm-registration'),
    path('meetup/<slug:meetup_slug>', views.meetup_details, name='meetup-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

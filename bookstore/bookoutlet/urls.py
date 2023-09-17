from django.urls import path

from . import views
urlpatterns = [
    path('', view=views.index, name='starting-age'),
    path('<slug:slug>', views.book_detail, name='book-detail')
]

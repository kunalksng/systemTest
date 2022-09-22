from django.urls import path
from . import views
urlpatterns =[
    path('contacts/',views.createContact.as_view()),
    path('contacts/<id>/',views.getSpecificContact.as_view()),
    path('xyz/',views.contactsCallList.as_view()),

]
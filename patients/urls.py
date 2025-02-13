from patients import views
from django.urls import path
urlpatterns = [
    path('<int:id>',views.patient_list)
]
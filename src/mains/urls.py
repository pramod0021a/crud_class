from django.urls import path
from . import views

app_name = 'mains'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('update/<int:id>', views.UpdateStudentView.as_view(), name='updatedata'),
    path('delete/<int:id>', views.DeleteStudentView.as_view(), name='deletedata'),
]
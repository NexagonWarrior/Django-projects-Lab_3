from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_student, name='add_student'),
    path('del/<int:student_id>/', views.delete_student, name='delete_student'),
    path('rev/<int:student_id>/', views.revise_student, name='revise_student'),
    path('finance/', views.finance_report, name='finance'),
    path('', views.group_list, name='group_list'),
    path('<str:group_name>/', views.group_detail, name='group_detail'),  # ← останнім
]

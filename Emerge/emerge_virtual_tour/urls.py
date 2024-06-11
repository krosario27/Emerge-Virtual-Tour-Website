from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("virtual-tour-landing/", views.virtual_tour_landing, name="virtual_tour_landing"),
    path("students/", views.students, name="students"),
    path("vr_sroom/", views.vr_sroom, name="vr_sroom"),
    path("vr_xblock/", views.vr_xblock, name="vr_xblock"),
    path('student/<int:id>/', views.student_detail, name='student_detail'),
]

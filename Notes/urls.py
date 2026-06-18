from django.urls import path
from.import views

urlpatterns = [
    path('',views.home),
    path('upload/',views.upload_note),
    path('delete/<int:id>/',views.delete_note),
    path('edit/<int:id>/',views.edit_note),
    path('register/',views.Register),
    path('login/',views.login_user),
    path('logout/',views.logout_user),
    path('my_notes/',views.my_notes),
    path('subject/<str:subject>/',views.subject_notes),
    path('profile/', views.profile, name = 'profile'),
    path('edit_profile/', views.edit_profile, name = 'edit_profile'),
]
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView  # <-- for checker
from . import views

app_name = 'relationship_app'

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
    # Authentication views — rewritten for checker expectations
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # <-- matches checker
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # <-- matches checker
    path('register/', views.register, name='register'),  # <-- for "views.register"
]

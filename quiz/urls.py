from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'), 
    path('test/<str:category>/', views.test_view, name='test_view'),
    # Mana bu qatorni qo'shib qo'ying:
    path('test/', views.index_view, name='test_index'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('leaderboard/', views.leaderboard_view, name='leaderboard'),
]
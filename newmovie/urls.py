from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),






    path('', views.home, name='home'),
    path('movie/', views.movie, name='movie'),
    path('user/<str:pk>', views.customer, name='user'),
    path('movie_id/<str:pk>', views.movie_id, name='movie_id'),
    path('accountsettings/', views.accountSettings, name='accountsettings'),


    path('add_movie/', views.add_movie, name='add_movie'),
    path('update_movie/<str:pk>/', views.updateMovie, name='update_movie'),
    path('delete_movie/<str:pk>/', views.deleteMovie, name='delete_movie'),

    path('update_user/<str:pk>/', views.updateUser, name='update_user'),
    path('delete_user/<str:pk>/', views.deleteUser, name='delete_user'),
    path('search/', views.searchBar, name='search_bar'),


    path('reset_password/',
             auth_views.PasswordResetView.as_view(template_name="newmovie/password_reset.html"),
             name="reset_password"),

        path('reset_password_sent/',
             auth_views.PasswordResetDoneView.as_view(template_name="newmovie/password_reset_sent.html"),
             name="password_reset_done"),

        path('reset/<uidb64>/<token>/',
             auth_views.PasswordResetConfirmView.as_view(template_name="newmovie/password_reset_form.html"),
             name="password_reset_confirm"),

        path('reset_password_complete/',
             auth_views.PasswordResetCompleteView.as_view(template_name="newmovie/password_reset_done.html"),
             name="password_reset_complete"),



    path('filter_movie_2021/', views.filtering_movie_2021, name='filter_movie_2021'),
    path('filter_movie_2020/', views.filtering_movie_2020, name='filter_movie_2020'),
    path('filter_movie_2019/', views.filtering_movie_2019, name='filter_movie_2019'),
    path('filter_movie_2018/', views.filtering_movie_2018, name='filter_movie_2018'),

    path('filter_movie_action/', views.filtering_movie_action, name='filter_movie_action'),
    path('filter_movie_drama/', views.filtering_movie_drama, name='filter_movie_drama'),
    path('filter_movie_triller/', views.filtering_movie_triller, name='filter_movie_triller'),
    path('filter_movie_comedy/', views.filtering_movie_comedy, name='filter_movie_comedy'),


    path('filter_movie_downloaded/', views.filtering_movie_downloaded, name='filter_movie_downloaded'),
    path('filter_movie_watched/', views.filtering_movie_watched, name='filter_movie_watched'),
    path('filter_movie_top_rank/', views.filtering_movie_top_rank, name='filter_movie_top_rank'),


]

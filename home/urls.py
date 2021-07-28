from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.register, name="register"),
    path('', views.base, name="base"),
    path('results/', views.results, name="results"),
    path('table/', views.table, name="table"),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name='password_reset.html'),
         name="reset_password"),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='password_reset_sent.html'),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password_reset_form.html'),
         name="password_reset_confirm"),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password_reset_done.html'),
         name="password_reset_complete"),
    path('pf/', views.render_pdf_view, name='test-view'),
]

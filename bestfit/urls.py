from django.contrib import admin

# from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.contrib.auth import views as auth_view
from online_quiz import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    # path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', views.LoginView.as_view(template_name='logout.html'), name='login'),
    path('secret/', views.secret_page, name='secret'),
    path('secret2/', views.SecretPage.as_view(), name='secret2'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('test/', views.test_page, name= 'test'),
    path('test/result', views.result, name= 'result'),
    path('profile/', views.profile, name='profile'),
    path('profileEdit/', views.profileEdit, name='profileEdit'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
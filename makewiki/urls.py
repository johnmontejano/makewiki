from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    # Admin Site
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', include('accounts.urls'), name="signUpView"),
    # Wiki App
    path('', include('wiki.urls')),
]

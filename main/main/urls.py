from django.contrib import admin
from django.urls import path
from notes.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', home , name="home_page"),
    path('login/', login_page , name="login_page"),
    path('logout/', logout_page , name="logout_page"),
    path('register/', signup , name="register"),
    path('notes/', notes , name="notes"),
    path('delete-note/<id>/', delete_note , name="delete_note"),
    path('view_notes/', view_notes , name="view_notes"),
    path('update-note/<id>/', update_note , name="update_note"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL,
                          document_root = settings.MEDIA_ROOT)
    
    

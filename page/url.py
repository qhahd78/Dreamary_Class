from . import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('page.urls')),
    pathpath('profile/<int:designer_id>', views.detail, name = "detail"),

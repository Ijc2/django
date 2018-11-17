
from django.urls import path
from usuario import views


urlpatterns = [
  path('list_usuario/', views.list_usuario, name='list_usuario'),
   path('list_proyecto/', views.list_proyecto, name='list_proyecto'),
    #path('admin/', admin.site.urls),
     #path('', home, name='home').

]

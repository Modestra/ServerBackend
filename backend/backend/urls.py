from django.contrib import admin
from django.urls import (path, include)
from rest_framework import (permissions, routers)
from djoser.views import UserViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from backend.views import *
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)
from RedOx.views import NoteApiView

get_user = AuthViewSet.as_view({"get": "list"})
set_user = AuthViewSet.as_view({"post": "set_user"})

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

app_name = "backend"

router = routers.DefaultRouter()
router.register(r'auth', AuthViewSet)
urlpatterns = [
    #Системные 
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    #backend
    path('user', get_user),
    path('create', set_user),

    # Подключение других проектов
    path('api/v1/', include(router.urls)),
    path('api/v2/', include('CheckNotes.urls')),
    path('api/v3/', include('RedOx.urls'))
]

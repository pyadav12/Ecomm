from django.contrib import admin
from django.urls import path,include
from . import views
# api
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
router = routers.DefaultRouter()
router.register(r'', views.UserViewSet)



urlpatterns = [
    path("",views.index,name="home"),
    path("contact",views.contact,name="contact"),
    path("Singup",views.Singup, name="Singup"),
    path("Login",views.Login, name="Login"),
    path("Logout",views.Logout, name="Logout"),
    path("cart",views.cart_detials, name="cart"),
    path("checkout",views.checkout, name="checkout"),
    path("order",views.Order_dtls, name="order"),

    path('rest/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

    # path('admin/', admin.site.urls),
    # path("",include('ecomm.urls'))

] 
# +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

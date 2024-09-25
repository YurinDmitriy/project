"""
URL configuration for myshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("main/", include("main.urls", namespace="main")),
    path("register/", user_views.register, name="register"),
    path("shop/", include("shop.urls", namespace="shop")),
    path("cart/", include("cart.urls", namespace="cart")),
    path("payment/", include("payment.urls", namespace="payment")),
    path("user_profile/", include("user_profile.urls", namespace="user_profile")),
    path("catalog/", include("goods.urls", namespace="catalog")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]

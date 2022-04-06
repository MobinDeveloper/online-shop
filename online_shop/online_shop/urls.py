"""online_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from azbankgateways.urls import az_bank_gateways_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('bankgateways/', az_bank_gateways_urls()),
    path('payment/', include('payment.urls')),
    path('rosetta/', include('rosetta.urls')),
    path('customers/', include('customers.urls')),
    path('orders/', include('orders.urls')),
    path('', include('products.urls')),
    path('contact/', include('contact.urls')),
    path('chat/', include('chat.urls')),
    prefix_default_language=False,
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('captcha/', include('captcha.urls')),
]

admin.site.site_header = "Web Mall Admin"
admin.site.site_title = "Web Mall"
admin.site.index_title = "Web Mall Admin"

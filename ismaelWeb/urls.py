from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from app import views
from django.contrib import admin
admin.autodiscover()
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ismaelWeb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='home'),

    
    url(r'^recetas/([^/]+)$', 'app.views.recetas', name='recetas'),
    url(r'^platos/([^/]+)$', 'app.views.detalles', name='detalles'),
    
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

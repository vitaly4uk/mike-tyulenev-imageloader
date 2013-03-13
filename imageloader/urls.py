from django.conf.urls import patterns, include, url

from gallery.views import ImageCreate, ImageDetail, ImageDelete, ImageList

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'imageloader.views.home', name='home'),
    # url(r'^imageloader/', include('imageloader.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^create/$', ImageCreate.as_view(), name='image-create'),
    url(r'^$', ImageList.as_view(), name='image-list'),
    url(r'^/(?P<pk>\d)/$', ImageDetail.as_view(), name='image-detail'),
    url(r'^/(?P<pk>\d)/delete/$', ImageDelete.as_view(), name='image-delete'),
)


from django.conf import settings

if settings.DEBUG:
    urlpatterns += patterns('',
            url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                'document_root': settings.MEDIA_ROOT,
                }),
            )

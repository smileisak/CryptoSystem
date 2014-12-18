from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CryptoSystem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'Affine.views.home',name='home'),
    url(r'^trigger', 'Affine.views.trigger',name='trigger'),
    url(r'^brute', 'Affine.views.brute',name='brute'),

)

from django.conf.urls import patterns, include, url
from django.contrib import admin
from TaSM_site.forms import RegistrationForm
from TaSM_site.views import user_list,product_list,about_page,home_page,top_rated,home1,home
from registration.backends.default.views import RegistrationView
from django.views.generic import RedirectView
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect
#from TaSM_site import views

urlpatterns = patterns('',
    # Examples:rl
    # url(r'^$', 'TaSM.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/','TaSM_site.views.home',name='home'),
    url(r'^products/(.*)','TaSM_site.views.product',name='product'),
     # url(r'accounts/register/$', 
     #     RegistrationView.as_view(form_class = RegistrationForm), 
     #     name = 'registration_register'),
    url(r'^accounts/register/complete/$', RedirectView.as_view(url= '/accounts/login/'),name='registration-successful-redirect'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    (r'^$', home_page),
    (r'^user/$', user_list),
    (r'^product_list/$', product_list),
    (r'^about/$', about_page),
    (r'^toprated/$', top_rated),
    (r'^home1/$',home1),

)

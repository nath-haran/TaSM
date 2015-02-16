from django.conf.urls import patterns, include, url
from django.contrib import admin
from TaSM_site.forms import RegistrationForm
from registration.backends.default.views import RegistrationView
#from TaSM_site import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TaSM.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/','TaSM_site.views.home',name='home'),
    url(r'^product/(.*)','TaSM_site.views.product',name='product'),
     # url(r'accounts/register/$', 
     #     RegistrationView.as_view(form_class = RegistrationForm), 
     #     name = 'registration_register'),
 
    url(r'^accounts/', include('registration.backends.default.urls')),
)

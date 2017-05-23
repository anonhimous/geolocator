from django.conf.urls import url
from django.contrib import admin


from accounts.views import LoginView, LogoutView
from search.views import SearchView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
    url(r'^search/', SearchView.as_view(), name='search'),

]

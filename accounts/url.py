from django.conf.urls import url
from . import views
app_name='accounts'

urlpatterns=[
    url(r'^signup/$',views.signup_view),   # i verified ... by default request is GET request ok!?

]
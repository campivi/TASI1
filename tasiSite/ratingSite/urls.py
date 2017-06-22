from django.conf.urls import url
from ratingSite.views import *

urlpatterns = [
    url(r'^$', index, name="corrector"),

]
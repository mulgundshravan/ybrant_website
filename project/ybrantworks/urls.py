from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings
 

urlpatterns = [
    path('', views.ybrantworks, name='ybrantworks'),
    path('datasolution', views.datasolution, name='datasolution'),
    path('bigdata', views.bigdata, name='bigdata'),
    path('machinelearning', views.machinelearning, name='machinelearning'),
    path('projectmang', views.projectmang, name='projectmang'),
    path('tableau', views.tableau, name='tableau'),
    path('webapp', views.webapp, name='webapp'),
    path('dataanaly', views.dataanaly, name='dataanaly'),
    path('business', views.business, name='business'),
    path('datamanag', views.datamanag, name='datamanage'),
    path('datawarehouse', views.datawarehouse, name='datawarehouse'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from perkins import views
from django.urls import path


app_name='perkins'
urlpatterns = [
    path('',views.headline),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('finalinspection/',views.finalinspection,name='finalinspection'),
    path('headline2/',views.headline2),
    path('diagram/',views.machinediagram),
    # path('file/',views.file)
]

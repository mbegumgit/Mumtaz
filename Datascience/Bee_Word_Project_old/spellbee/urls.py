from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path('bee/<int:beeword_key>',views.beeword,name='beeword'),
    path("update", views.scoretb_update, name="update"),
    path("<int:beeword_id>", views.beeword_id, name="score_view")

]
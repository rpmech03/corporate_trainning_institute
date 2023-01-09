from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('signup', views.signup,name="signup"),
    path('slogin', views.slogin,name="slogin"),
    path('tsignup', views.tsignup,name="signup"),
    path('tlogin', views.tlogin,name="slogin"),
    path('submittask', views.submittask,name="submittask"),
    path('viewremarks', views.viewremarks,name="viewremarks"),
    path('trainer', views.trainer,name="trainer")
    # path('shome', views.shome, name='shome'),
]

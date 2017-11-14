from questions.views import AboutView
from django.conf.urls import url
from questions import views
urlpatterns = [
	url(r'^about$', AboutView.as_view(), name='about'),
	url(r'^home$', AboutView.as_view(), name='base'),
	#
	url(r'^registration$', views.registration),
	url(r'^logged_out$', views.logged_out_view, name = 'logged_out'),
	url(r'^login$', views.login),
	url(r'^ask$', views.ask),
	url(r'^settings$', views.settings),
	url(r'^question$', views.question),
	url(r'.*',views.index),
]


"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from django.contrib import admin
admin.autodiscover()

import ask.views
import ask.urls_constants
import qa.views


urlpatterns = [
    path('admin/', admin.site.urls),
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # /
    path(r'^$', qa.views.new, name=ask.urls_constants.NEW_URL_NAME),
    # /login/
    path(r'^login/', ask.views.stub_ok, name=ask.urls_constants.LOGIN_URL_NAME),
    # /signup/
    path(r'^signup/', ask.views.stub_ok, name=ask.urls_constants.SIGNUP_URL_NAME),
    # /question/<123>/    # instead of <123> it must be a question_id
    path(r'^question/(?P<question_id>[0-9]+)/', qa.views.question_details, name=ask.urls_constants.QUESTION_DETAILS_URL_NAME),
    # /ask/
    path(r'^ask/', ask.views.stub_ok, name=ask.urls_constants.ASK_URL_NAME),
    # /popular/
    path(r'^popular/', qa.views.popular, name=ask.urls_constants.POPULAR_URL_NAME),
    # /admin/
    path(r'^admin/', include(admin.site.urls)),
]

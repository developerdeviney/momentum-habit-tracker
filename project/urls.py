"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.urls import include, path
from core import views as habit_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", habit_views.habit_list, name="habit_list"),
    path("core/habit/<int:pk>/", habit_views.habit_detail, name="habit_detail"),
    path("core/habit/create/", habit_views.create_habit, name="create_habit"),
    path("core/habit/edit/", habit_views.edit_habit, name="edit_habit"),
    path("core/habit/<int:pk>/", habit_views.delete_habit, name="delete_habit"),
    path("core/habit/<int:pk>/", habit_views.delete_daily_record, name="delete_record"),
    path("core/habit/<int:pk>/", habit_views.create_daily_record, name="create_record"),
    path("core/habit/search/", habit_views.habit_search, name="habit_search"),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

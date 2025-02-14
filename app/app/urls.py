"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from employeeApp.views import (
    EmployeeListView,
    EmployeeCreateView,
    EmployeeUpdateView,
    EmployeeDeleteView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", EmployeeListView.as_view(), name="employee-list"),
    path("create/", EmployeeCreateView.as_view(), name="employee-create"),
    path("edit/<uuid:pk>/", EmployeeUpdateView.as_view(), name="employee-edit"),
    path("delete/<uuid:pk>/", EmployeeDeleteView.as_view(), name="employee-delete"),
]

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from employeeApp.models import Employee
from employeeApp.forms import EmployeeForm
from django.urls import reverse_lazy

# Create your views here.


class EmployeeListView(ListView):
    model = Employee
    template_name = "employeeApp/employee_view.html"
    context_object_name = "employees"


class EmployeeCreateView(CreateView):
    model = Employee
    template_name = "employeeApp/employee_create.html"
    form_class = EmployeeForm
    context_object_name = "employee"
    success_url = reverse_lazy("employee-list")


class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = "employeeApp/employee_edit.html"
    form_class = EmployeeForm
    context_object_name = "employee"
    success_url = reverse_lazy("employee-list")


class EmployeeDeleteView(DeleteView):
    model = Employee  
    template_name = "employeeApp/employee_delete.html"
    success_url = reverse_lazy("employee-list")

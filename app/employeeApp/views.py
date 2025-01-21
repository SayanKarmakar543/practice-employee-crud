from django.views.generic import ListView
from employeeApp.models import Employee

# Create your views here.


class EmployeeListView(ListView):
    model = Employee
    template_name = "employeeApp/employee_view.html"
    context_object_name = "employees"

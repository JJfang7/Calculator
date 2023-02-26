from django.shortcuts import render
from django.http import HttpResponse
from .models import calculate

def index(request):
    savings, A_data, B_data = calculate(request)
    return render(request, 'form.html', {'A_salaries': A_data['A_salaries'],
                                         'A_hires': A_data['A_hires'],
                                         'A_percent': A_data['A_percent'],
                                         'B_salary': B_data['B_salary'] ,
                                         'B_hires': B_data['B_hires'],
                                         'B_percent': B_data['B_percent'],
                                         'A_costs' : A_data['A_costs'],
                                         'B_costs' : B_data['B_costs'],
                                         'Savings' : savings})

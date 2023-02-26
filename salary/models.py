from django.db import models
NUMBER_OF_GRADES = 3
DEFAULT_SALARY_A = [60001, 80000]
DEFAULT_SALARY_B = [45000]
DEFAULT_HIRES_A = [1, 1, 2]
DEFAULT_HIRES_B = [15, 2, 2]
DEFAULT_PERCENTAGE_A = [0, 10, 15]
DEFAULT_PERCENTAGE_B = 20

def calculate(request):
    # getting the data from request
    # converting them into int
    A_data ={
        'A_salaries': DEFAULT_SALARY_A,
        'A_hires': DEFAULT_HIRES_A,
        'A_percent': DEFAULT_PERCENTAGE_A,
        'A_costs' : []
    }
    B_data ={
        'B_salary': DEFAULT_SALARY_B,
        'B_hires': DEFAULT_HIRES_B,
        'B_percent': DEFAULT_PERCENTAGE_B,
        'B_costs' : []
    }
    if request.GET.getlist('Agrade'): 
        A_data['A_salaries'] = list(map(int,request.GET.getlist('Agrade')))
        A_data['A_percent'] = list(map(int,request.GET.getlist('Ap')))
        A_data['A_hires'] = list(map(int,request.GET.getlist('Ahires')))
        B_data['B_salary'] = list(map(int, request.GET.getlist('Bgrade')))
        B_data['B_percent'] = int(request.GET.get('Bp'))
        B_data['B_hires'] = list(map(int,request.GET.getlist('Bhires')))
        savings = []

        for i in range(1, NUMBER_OF_GRADES):
            B_data['B_salary'].append(A_data['A_salaries'][i])

        for i in range(0, NUMBER_OF_GRADES):
            if i == 0:
                A_cost = A_data['A_salaries'][i] * A_data['A_hires'][i]
            else:
                A_cost = A_data['A_salaries'][i] * A_data['A_percent'][i] // 100 * A_data['A_hires'][i]
            A_data['A_costs'].append(A_cost)

            B_cost = B_data['B_salary'][i] * B_data['B_percent'] // 100 * B_data['B_hires'][i]
            B_data['B_costs'].append(B_cost)

            savings.append(B_cost - A_cost)

        A_data['A_salaries'] = list(map(int,request.GET.getlist('Agrade')))[1:]
        B_data['B_salary'] = list(map(int, request.GET.getlist('Bgrade')))
        return savings, A_data, B_data
    
    else:
        return None, A_data, B_data
from django.shortcuts import render

# Create your views here.

def calculate(request, oprator, param1, param2):
    # a variable for holding result 
    result = 0

    if oprator == "add":
        result = param1 + param2
    elif oprator == "multiply":
        result = param1 * param2
    elif oprator == "divide":
        result = param1 / param2
    elif oprator == "subtract":
        result = param1 - param2

    # a dictionary to pass the template
    context = {
        "result": result,
        "oprator": oprator,
        "param1": param1,
        "param2" : param2
    }

    return render(request, 'calculator/index.html', context=context)
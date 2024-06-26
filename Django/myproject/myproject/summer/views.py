from django.http import HttpResponse
from django.shortcuts import render

def calc(request):
    if request.method == 'POST':
        a = int(request.POST.get('a'))
        b = int(request.POST.get('b'))
        code_word = request.POST.get('code_word')

        if code_word == 'sum':
            result = a + b
            operation = 'Addition'
        elif code_word == 'diff':
            result = a - b
            operation = 'Subtraction'
        elif code_word=='mul':
            result = a*b
            operation='Multiplication'
        elif code_word=='div':
            result=a/b
            operation='Division'
        
        else:
            result = None
            operation = 'Unknown'

        return render(request, 'results.html', {'result': result, 'operation': operation})
    else:
        return render(request, 'hello_world.html')

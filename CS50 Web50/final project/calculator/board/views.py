from datetime import date
from json.decoder import JSONDecodeError
from django.contrib.auth import authenticate, login, logout
from django.core import paginator
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
import json
import re
from .models import ans

# Create your views here.

def index(request):
    return render(request, "board/index.html", {})

def is_operator(s):
    operator = ['+', '-', '*', '/', '(', ')']
    return True if s in operator else False

def decision(now, top):
    # 1 means pop, -1 means append, 0 means '(' meets ')' and delete them all
    rate1 = ['+', '-']
    rate2 = ['*', '/']
    rate3 = ['(']
    rate4 = [')']
    if top in rate1:
        return -1 if now in rate2 or now in rate3 else 1
    elif top in rate2:
        return -1 if now in rate3 else 1
    elif top in rate3:
        return 0 if now in rate4 else -1
    else:
        return -1

def cal(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2

@csrf_exempt
def calculate(request):
    data = json.loads(request.body)
    s = []
    
    # Divide the string into numbers and operators
    num = ""
    data["s"] = re.sub(' ', '', data["s"])
    for i in range(len(data["s"])):
        if data["s"][i] == '-' and (i == 0 or data["s"][i - 1] == '('):
            num = "-"
            continue
        if is_operator(data["s"][i]):
            if num != '': 
                s.append(num)
            s.append(data["s"][i])
            num = ''
        else:
            num += data["s"][i]
    if num != '':
        s.append(num)

    # Deal with the numbers and operators
    num_stk = []
    oper_stk = []
    for i in s:
        if is_operator(i) == False:
            num_stk.append(float(i))
        else:
            while True:
                if len(oper_stk) == 0:
                    oper_stk.append(i)
                    break
                if decision(i, oper_stk[-1]) == -1:
                    oper_stk.append(i)
                    break
                elif decision(i, oper_stk[-1]) == 0:
                    oper_stk.pop()
                    break
                else:
                    op = oper_stk.pop()
                    num2 = num_stk.pop()
                    num1 = num_stk.pop()
                    if op == '/' and num2 == 0:
                        return JsonResponse({"error": "Divide 0"})
                    num_stk.append(cal(num1, num2, op))
    while len(oper_stk) != 0:
        op = oper_stk.pop()
        num2 = num_stk.pop()
        num1 = num_stk.pop()
        if op == '/' and num2 == 0:
            return JsonResponse({"error": "Divide 0"})
        num_stk.append(cal(num1, num2, op))
    a = ans(num=num_stk[0])
    a.save()
    return JsonResponse({"ans": f"{num_stk[0]}"})

def get_ans(request):
    t = ans.objects.all()
    t = t.order_by('-timestamp').all()
    return JsonResponse({"ans": f"{t[0].num}"})
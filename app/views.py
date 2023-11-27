from django.shortcuts import render
from app.forms import Front_times_form, Centered_form, No_teen_sum_form, xyz_form
import math

# Create your views here.
def front_times(request):
    #brittney okayed this
    form = Front_times_form(request.GET)
    if form.is_valid():
        result = ''
        word = form.cleaned_data['word']
        times = form.cleaned_data['times']
        length = form.cleaned_data['length']
        if length > len(word):
            length = len(word)
        amount = word[:length]
        
        for i in range(times):
            result = result + amount
        
        return render(request, 'front_times.html', {'word': word, 'times': times, 'length': length, 'result': result})
    else:
        return render(request, 'front_times.html')

def centered_average(request):
    form = Centered_form(request.GET)
    if form.is_valid():
        n1 = form.cleaned_data['n1']
        n2 = form.cleaned_data['n2']
        n3 = form.cleaned_data['n3']
        n4 = form.cleaned_data['n4']
        n5 = form.cleaned_data['n5']
        n6 = form.cleaned_data['n6']
        n7 = form.cleaned_data['n7']
        if n6 == None and n7 == None:
            nums = [n1, n2, n3, n4, n5]
        elif n6 != None:
            nums = [n1, n2, n3, n4, n5, n6]
        elif n6 != None and n7 != None:
            nums = [n1, n2, n3, n4, n5, n6, n7]
        max_num = nums[0]
        min_num = nums[0]
        sum = 0
        for i in nums:
            max_num = max(max_num, i)
            min_num = min(min_num, i)
            sum += i
            result = (sum - max_num - min_num) / (len(nums) - 2)
            result = f'{round(result, 0):.0f}'
        return render(request, 'center_average.html', {'n1': n1, 'n2': n2, 'n3': n3, 'n4': n4, 'n5': n5, 'n6': n6, 'n7': n7, 'result': result})
    else:
        return render(request, 'center_average.html')

def no_teen_sum(request):
    form = No_teen_sum_form(request.GET)
    if form.is_valid():
        a = form.cleaned_data['n1']
        b = form.cleaned_data['n2']
        c = form.cleaned_data['n3']
        numlist = [13, 14, 17, 18, 19]
        if a in numlist and b in numlist and c in numlist:
            number = 0
        elif a in numlist and b not in numlist and c not in numlist:
            number = (b + c)
        elif a not in numlist and b in numlist and c not in numlist:
            number = (a + c)
        elif a not in numlist and b not in numlist and c in numlist:
            number = (a + b)
        elif a not in numlist and b not in numlist and c not in numlist:
            number = (a + b + c)
        elif a in numlist and b in numlist and c not in numlist:
            number = (c)
        elif a in numlist and b not in numlist and c in numlist:
            number = (b)
        elif a not in numlist and b in numlist and c in numlist:
            number = (a)
        
        return render(request, 'no_teen_some.html', {'a': a, 'b': b, 'c': c, 'number': number})
    else:
        return render(request, 'no_teen_some.html')
    
def xyz_there(request):
    form = xyz_form(request.GET)
    if form.is_valid():
        word = form.cleaned_data['word']
        result = False
        for i in range(len(word) - 2):
            if word[i:i + 3] == "xyz" and (i == 0 or word[i - 1] != '.'):
                result = True
                break
        return render(request, 'xyz_there.html', {"word": word, 'result': result})
    else:
        return render(request, 'xyz_there.html')

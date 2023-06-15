from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from django.views.generic.base import RedirectView
from .models import User, Questions, Results, Class

# Create your views here.

favicon_view = RedirectView.as_view(url="/static/mi/brain.ico", permanent=True)

def index(request):
    return render(request, 'mi/index.html')

def dash(request):
    if request.method == 'POST':
        if not request.POST['name']:
            return render(request, "mi/dash.html", {
                'message': 'Please enter a name.'
            })
        if not request.POST['code']:
            return render(request, "mi/dash.html", {
                'message': 'Please enter a code.'
            })
        
        classname = request.POST['name']
        classcode = request.POST['code']

        noclass = False
        try:
            rows = Class.objects.get(classcode = classcode)
        except Class.DoesNotExist:
            noclass = True

        if noclass:
            newClass = Class(teacher = request.user, classcode = classcode, classname = classname)
            newClass.save()
            return HttpResponseRedirect(reverse("dash"))
        else:
            return render(request, "mi/dash.html", {
                'message': "Class with this code already exists. Try again with a different code."
            })
    else:
        class ClassItem:
            def __init__(self, name, code, results):
                self.name = name
                self.code = code
                self.results = results
        classes = []
        rows = Class.objects.filter(teacher = request.user)
        for row in rows:
            results = Results.objects.filter(code = row.classcode)
            classitem = ClassItem(row.classname, row.classcode, results)
            classes.append(classitem)
        
        return render(request, "mi/dash.html", {
            'classes': classes,
        })

def test_view(request):
    if request.method == 'POST':
        code = request.POST['code']
        name = request.POST['name']
        types = ["VERB","LOG","MUS","VIS","KIN","INTER","INTRA","NAT"]
        res = {
            'VERB' : 0,
            'LOG' : 0,
            'MUS' : 0,
            'VIS' : 0,
            'KIN' : 0,
            'INTER' : 0,
            'INTRA' : 0,
            'NAT' : 0
        }

        for i in range(8):
            values = []
            rows = Questions.objects.filter(type = types[i])
            for row in rows:
                ids = row.id
                idss = str(ids)
                val = request.POST[""+idss]
                vals = int(val)
                values.append(vals)
            res[types[i]] = sum(values)
            List = sorted(res, key=res.get, reverse=True)
            ress = {
                List[0] : res[List[0]],
                List[1] : res[List[1]],
                List[2] : res[List[2]],
                List[3] : res[List[3]],
                List[4] : res[List[4]],
                List[5] : res[List[5]],
                List[6] : res[List[6]],
                List[7] : res[List[7]]
            }

        if code != None or 0 or "" or " ":
            new_result = Results(name = name, code = code, VERB = res['VERB'], LOG = res['LOG'], MUS = res['MUS'], VIS = res['VIS'] , KIN = res['KIN'], INTER = res['INTER'], INTRA = res['INTRA'], NAT = res['NAT'])
            new_result.save()
        return render(request, "mi/results.html", {
            'res': ress
        })
    else:
        rows = Questions.objects.all()
        return render(request, 'mi/test.html', {
            'rows': rows
        })

def classes(request, code):
    if request.method != "GET":
        return JsonResponse({"error": "GET request required."}, status=400)

    result = "Yes"
    try:
        classitem = Class.objects.get(classcode = code)
    except Class.DoesNotExist:
        result = "None"

    return JsonResponse(result, safe=False)

def scores(request,code):
    if request.method != "GET":
        return JsonResponse({"error": "GET request required."}, status=400)
    """ results = ["VERB","LOG","MUS","VIS","KIN","INTER","INTRA","NAT"]  """
    results = [0,0,0,0,0,0,0,0]
    try:
        resultsitem = Results.objects.filter(code = code)
    except Results.DoesNotExist:
        return JsonResponse(result, safe=False)
    
    
    for result in resultsitem:
        resulter = []
        resulter.append(int(result.VERB))
        resulter.append(int(result.LOG))
        resulter.append(int(result.MUS))
        resulter.append(int(result.VIS))
        resulter.append(int(result.KIN))
        resulter.append(int(result.INTER))
        resulter.append(int(result.INTRA))
        resulter.append(int(result.NAT))
        up = 0
        for i in range(8):
            if (int(resulter[i]) >= int(resulter[up])):
                up = i
        results[up] += 1
        
    return JsonResponse(results, safe=False)
    

def test_code(request, code):
    rows = Questions.objects.all()

    try:
        classitem = Class.objects.get(classcode = code)
    except Class.DoesNotExist:
        return HttpResponseRedirect(reverse("test"))
    return render(request, 'mi/test.html', {
        'rows': rows,
        'code': code
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("dash"))
        else:
            try:
                useritem = User.objects.get(username = username)
            except User.DoesNotExist:
                return render(request, "mi/login.html", {
                    "message": "Invalid username."
                })
            return render(request, "mi/login.html", {
                "message": "Invalid password."
            })
    else:
        return render(request, "mi/login.html")

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "mi/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "mi/register.html", {
                "message": "User with this username already exists. Please log in."
            })
        
        login(request, user)
        return HttpResponseRedirect(reverse("dash"))
    else:
        return render(request, "mi/register.html")
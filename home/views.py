from home.models import Qsmart, Remarks, Suggestion, User
from django.http import request, FileResponse
from home.decorators import unauthenticated_user
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import Registerform
from django.contrib import messages
from django.contrib.auth import authenticate, login as dj_login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


def render_pdf_view(request):
    template_path = 'pdf_convert.html'
    if request.method == 'POST':
        name = str(request.POST.get('username'))
        sname = str(request.POST.get('sn'))
        qsmar = Qsmart.objects.all().filter(UserName=name).filter(Samplename=sname)
        context = {'qsmar': qsmar}
    else:
        context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if download:
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if display:
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


@unauthenticated_user
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            dj_login(request, user)
            return redirect('base')
        else:
            messages.info(request, 'Username or password is incorrect')

    return render(request, 'login.html')


@unauthenticated_user
def register(request):
    if request.method == 'POST':
        form = Registerform(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            emailc = form.cleaned_data.get('email')
            sn = User.objects.all()
            for k in sn:
                if k.email == emailc:
                    messages.info(
                        request, 'Change Email as it is already registered')
                    return render(request, 'register.html', {"form": form})
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            messages.success(request, 'Account was created for '+username)
            return redirect('login')
    else:
        form = Registerform()

    return render(request, 'register.html', {"form": form})


@ login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')


@ login_required(login_url='login')
def base(request):
    if request.method == 'GET':
        return render(request, 'base.html')
    if request.method == 'POST':
        name = str(request.POST.get('username'))
        id = str(request.POST.get('Sampleid'))
        sn = Qsmart.objects.all().filter(UserName=name)
        for su in sn:
            if id == su.Samplename:
                messages.info(
                    request, 'That sample name already exists enter a different one')
                return render(request, 'base.html')
        desc = request.POST.get('Sampledesc', False)
        factor_1 = float(request.POST.get('F1', False))
        factor_2 = float(request.POST.get('F2', False))
        factor_3 = float(request.POST.get('F3', False))
        factor_4_1 = float(request.POST.get('F41', False))
        factor_4_2 = float(request.POST.get('F42', False))
        factor_4_3 = float(request.POST.get('F43', False))
        factor_5 = float(request.POST.get('F5', False))
        factor_6 = float(request.POST.get('F6', False))
        factor_7 = float(request.POST.get('F7', False))
        factor_8 = float(request.POST.get('F8', False))
        factor_h = float(request.POST.get('hc', False))
        factor_9 = float(request.POST.get('F9', False))
        factor_10 = float(request.POST.get('F10', False))
        factor_4 = factor_4_1+factor_4_2+factor_4_3
        if factor_h == 0:
            factor_9u = factor_9/2
        else:
            factor_9u = factor_9

        rating = factor_1+factor_2+factor_3+factor_4+factor_5 + \
            factor_6+factor_7+factor_8+factor_9u+factor_10
        entry = Remarks.objects.all().filter(
            Range_min__lte=rating).filter(Range_high__gte=rating)
        sug = Suggestion.objects.all()
        for su in sug:
            if rating >= su.min and rating <= su.high:
                l = su.Support_suggested

        k = 'Falls under the category '+entry[0].category+'\n The status of Stability of slope : '+entry[0].StabilityslopeRemark+'Failures : ' + \
            entry[0].Failures+'. Remedial Measures/suggestion in border sense: ' + \
            entry[0].Remborder+'\n'+'. Support suggested is '+l
        Qsmart.objects.create(Samplename=id, Sampledesc=desc, UserName=name, Qremarks=k, Value_F1=factor_1, Value_F2=factor_2,
                              Value_F3=factor_3, Value_F4=factor_4, Value_F5=factor_5, Value_F6=factor_6, Value_F7=factor_7, Value_F8=factor_8, Value_F9=factor_9u, Value_F10=factor_10, QSMAR_rating=rating)
        messages.success(request, 'qsmar rating for ' +
                         id+' '+desc+' is : '+str(rating))
        return redirect('results')


@ login_required(login_url='login')
def results(request):
    if request.method == 'GET':
        return render(request, 'results.html')
    if request.method == 'POST':
        if 'allresults' in request.POST:
            name = str(request.POST.get('username'))
            qsmar = Qsmart.objects.all().filter(UserName=name)
            if qsmar.exists():
                return render(request, 'results.html', {"qsmar": qsmar})
            else:
                messages.info(request, 'No results')
                return render(request, 'results.html')
        if 'search' in request.POST:
            name = str(request.POST.get('username'))
            sname = str(request.POST.get('samplename'))
            qsmar = Qsmart.objects.all().filter(UserName=name).filter(Samplename=sname)
            if qsmar.exists():
                return render(request, 'results.html', {"qsmar": qsmar})
            else:
                messages.info(request, 'No such sample name found')
                return render(request, 'results.html')
        if 'delete' in request.POST:
            name = str(request.POST.get('username'))
            sname = str(request.POST.get('samplename'))
            qsmar = Qsmart.objects.all().filter(UserName=name).filter(Samplename=sname)
            if qsmar.exists():
                qsmar.delete()
                messages.info(request, 'Deleted '+sname)
                return render(request, 'results.html')
            else:
                messages.info(request, 'No such sample name found')
                return render(request, 'results.html')
        if 'table' in request.POST:
            name = str(request.POST.get('username'))
            sname = str(request.POST.get('sn'))
            qsmar = Qsmart.objects.all().filter(UserName=name).filter(Samplename=sname)
            if qsmar.exists():
                return render(request, 'table.html', {"qsmar": qsmar})
            else:
                messages.info(request, 'ERROR')
                return render(request, 'results.html')


@ login_required(login_url='login')
def table(request):
    return render(request, 'table.html')

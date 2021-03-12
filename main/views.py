
from django.shortcuts import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Profile ,Programs_category,Programs ,Register
from .forms import SignUpForm
from django.db.models import Q
from django.contrib.auth.models import User

 
def program(request,myid):
    Program_category = Programs_category.objects.get(Program_category_name=myid)
    context={
    'data': Program_category
    }
    profile = 'k'
    try:
        profile = Profile.objects.get(username1 = request.user.username )
    except :
        pass
    try:
        detail = Programs.objects.filter(Programs_category_name=myid)
        context={
        'detail':detail,
        'data': Program_category,
        'profile':profile

        }
    except:
        pass
    return render(request, 'program.html',context)


def Registrations(request):
    samedata = Register.objects.all()
    # print(samedata)
    context={
    'data': samedata
    }
    if request.method == 'POST':
        if 'searchname' in request.POST:
            searchname = request.POST["searchname"]
            query = Register.objects.filter(Q(Program_name__contains = searchname) | Q(User__contains = searchname))
            print(query)
            context={
            'data': query
            }

        else:
            pass
    else:
        pass
    return render(request, 'Registrations.html',context)


def programregister(request,pn,pid):
    Program_category = Programs.objects.get(id=pid )
    checkfor = Program_category.Program_name
    context={
    'data': Program_category
    }
    if request.method == 'POST':
        rr = Register()
        if 'User' in request.POST:
            rr.User = request.POST["User"]
            rr.Program_name = request.POST["pname"]
            rr.Price = request.POST["price"]
            rr.Date = request.POST["date"]
            rr.Time = request.POST["time"]
            rr.save()
        else:
            pass
    else:
        pass

    profile = 'k'
    try:
        profile = Profile.objects.get(username1 = request.user.username )
    except :
        pass
    check123 = '1'
    try:
        check123 = Register.objects.get(User = request.user.username ,Program_name = checkfor)
     
    except :
        pass

    context={
    'data': Program_category,
    'profile':profile,
    'check':check123
    }

    return render(request, 'programregister.html',context)


@login_required
def addprogram(request):
    profile_data = Programs.objects.all()
    context={
    'data': profile_data
    }
    try:
        detail = Programs_category.objects.all()
        context={
        'detail':detail,
        'data': profile_data

        }
    except:
        pass

    if request.method == 'POST':
        pd = Programs()
        if 'programname' in request.POST:
            pd.Programs_category_name = request.POST["category"]
            pd.Program_name = request.POST["programname"]
            pd.Price_for_ymca_Member = request.POST["Price_for_ymca_Member"]
            pd.Price_for_non_ymca_Member = request.POST["Price_for_non_ymca_Member"]
            pd.StartingDate = request.POST["StartingDate"]
            pd.EndingDate = request.POST["EndingDate"]
            pd.StartingTime = request.POST["StartingTime"]
            pd.EndingTime = request.POST["EndingTime"]
            pd.Location = request.POST["Location"]
            pd.Description = request.POST["Description"]
            pd.Participant_allowed = request.POST["Participant_allowed"]
            pd.save()
        else:
        	if request.method == 'POST' and request.FILES['programimage']:
        		if 'programcn' in request.POST  :
        			pc = Programs_category()
        			pc.Program_category_name = request.POST['programcn']
        			pc.Program_Description = request.POST['programcd']
        			pc.Program_logo = request.FILES['programimage']
        			pc.save()
        		else:
        			pass

    else:
        pass

    # if request.method == 'POST' and request.FILES['programimage']:
    #     if 'programcn' in request.POST  :
    #         pc = Programs_category()
    #         pc.Program_category_name = request.POST['programcn']
    #         pc.Program_Description = request.POST['programcd']
    #         pc.Program_logo = request.FILES['programimage']
    #         pc.save()
    #     else:
    #         pass
    # else:
    #     pass

    return render(request, 'addprogram.html',context)

@login_required
def allprogram(request):
    profile_data = Programs.objects.all()
    context={
    'data': profile_data
    }
    if request.method == 'POST' :
        if 'active' in request.POST  :
            qid = request.POST['id']
            print(qid)
            ps = Programs.objects.get(id=qid)
            ps.status = request.POST['active']
            ps.save()
            profile_data = Programs.objects.all()
            context={
            'data': profile_data
            }
        if 'cancel' in request.POST  :
            qid = request.POST['id']
            print(qid)
            pp = Programs.objects.get(id=qid)
            pp.status = request.POST['cancel']
            pp.save()
            profile_data = Programs.objects.all()
            context={
            'data': profile_data
            }

        else:
            pass
    else:
        pass

    return render(request, 'allprogram.html',context)
@login_required
def alluser(request):
    profile_data = Profile.objects.all()
    context={
    'data': profile_data
    }
    if request.method == 'POST' :
        if 'user123' in request.POST  :
            iduser = request.POST['user123']
            # pw = Profile.objects.get(username1=iduser)
            ppp = User.objects.get(username=iduser)
            ppp.delete()
            # pw.delete()
            try:
                 pq = Register.objects.filter(User=iduser)
                 for n in pq:
                    n.status='Cancel'
                    n.save()
            except:
                pass

            
        else:
            pass
    else:
        pass

    return render(request, 'allusers.html',context)

def index(request):
    program_data = Programs_category.objects.all()
    context={
    'data': program_data
    }
    try:
        detail = Profile.objects.get(username1 = request.user.username )
        context={
        'detail':detail,
        'data': program_data
        }
    except :
        pass
    return render(request, 'index.html',context)


def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.Position = form.cleaned_data.get('Apply_for')
        user.profile.Gender = form.cleaned_data.get('Gender')
        user.profile.Contact_Number = form.cleaned_data.get('Contact_Number')
        user.profile.Address = form.cleaned_data.get('Address')
        user.profile.username1 = form.cleaned_data.get('username')
        user.profile.email = form.cleaned_data.get('email')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
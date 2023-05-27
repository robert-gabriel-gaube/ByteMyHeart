from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.contrib.auth.hashers import make_password, check_password
from application.models import Report, User, DateOffer, Form
from application.forms import LoginForm, ReportForm, UserRegisterForm, BigRegisterForm

user = None
logInUser = None

class BigRegisterFormView(View):
    def get(self, request):
        bigform = BigRegisterForm()
        return render(request, "application/BigForm.html", {
            "bigform": bigform
        })
    def post(self, request):
        bigform = BigRegisterForm(request.POST)

        if bigform.is_valid():
            form=bigform.save()
            user.formId = form
            user.save()
            return HttpResponseRedirect("/")
        return render(request, "application/BigForm.html",{
            "bigform": bigform
        })

class UserRegisterFormView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, "application/Form.html", {
            "form": form
        })
    
    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            global user
            user=form.save()
            user.password=make_password(form.cleaned_data['password'])
            user.save()
            return HttpResponseRedirect("/interestform")
        return render(request, "application/Form.html", {
            "form": form
        })

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "application/LoginPage.html", {
            "form": form
        })  
    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            user=User.objects.get(username=form.cleaned_data['username'])
            if user is not None:
                if check_password(form.cleaned_data['password'], user.password):
                    global logInUser
                    logInUser=user
                
                    if(user.role == 1):
                        return HttpResponseRedirect("/user-main-page")
                    else:
                        return HttpResponseRedirect("/reports")
        return render(request, "application/LoginPage.html", {
            "form": form
        })
    
                   

class ReportsView(View):
    def get(self, request):
        reports = Report.objects.all

        return render(request, "application/reports.html", {
            'reports' : reports
        })
    
class ViewMyProfileView(View):
    def get(self, request):
        return render(request, "application/ViewMyProfile.html", {
            'form' : logInUser.formId
        })
    
    
class ReportsActionView(View):
    def get(self, request, pk, username, status):
        report = Report.objects.get(pk=pk)
        report.status = 'CSD'
        report.save()
        user = User.objects.get(username=username)
        user.isBanned = status
        user.save()

        return HttpResponseRedirect("/reports")

class ReportView(View):
    def get(self, request, pk):
        report = Report.objects.get(pk=pk)
        return render(request, "application/report.html", {
            'report' : report,
            'user' : report.receiverID
        })
    
class CreateReportView(View):
    def get(self, request):
        form = ReportForm()
        return render(request, "application/create_report.html", {
            'form': form
        })
    
    def post(self, request):
        form = ReportForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/user-main-page")

        return render(request, "application/create_report.html", {
            "form": form
        })

class UserMainPageView(View):
    def get(self, request):
        return render(request, "application/main_page_users.html",{
            'username': logInUser.username,
        })
    
class IndexPageView(View):
    def get(self, request):
        return render(request, "application/IndexPage.html")
    
class MatchView(View):
    def get(self, request, username):
        print(logInUser)
        if logInUser is None:
            return HttpResponseRedirect("/login")

        match = User.objects.get(username=username)
        offers1 = DateOffer.objects.filter(senderId=logInUser, receiverId=match)
        offers2 = DateOffer.objects.filter(receiverId=logInUser, senderId=match)

        offers = offers1 | offers2
        
        offers = offers.order_by('created_at')

        return render(request, "application/date_offer.html", {
            'offers': offers,
            'date': match,
            'loggedUser': logInUser
        })
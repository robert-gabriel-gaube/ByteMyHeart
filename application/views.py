from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from application.models import Report, User
from application.forms import ReportForm, UserRegisterForm, BigRegisterForm

user = None

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
            user=form.save(commit= False)
            return HttpResponseRedirect("/interestform")
        return render(request, "application/Form.html", {
            "form": form
        })
                

class ReportsView(View):
    def get(self, request):
        reports = Report.objects.all

        return render(request, "application/reports.html", {
            'reports' : reports
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
        return render(request, "application/main_page_users.html")
    
class IndexPageView(View):
    def get(self, request):
        return render(request, "application/IndexPage.html")
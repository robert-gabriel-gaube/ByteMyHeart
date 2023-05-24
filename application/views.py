from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from application.models import Report
from application.forms import UserRegisterForm, BigRegisterForm

user = None

class UserRegisterFormView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, "application/Form.html", {
            "form": form
        })
    
    def post(self, request):
        form = UserRegisterForm(request.post)

        if form.is_valid():
            user=form.save(commit= False)
            return HttpResponseRedirect("/")
        return render(request, "application/Form.html", {
            "form": form
        })
                

class ReportsView(View):
    def get(self, request):
        reports = Report.objects.all

        return render(request, "application/reports.html", {
            'reports' : reports
        })
from django.shortcuts import render
from django.views import View

from application.models import Report

class ReportsView(View):
    def get(self, request):
        reports = Report.objects.all

        return render(request, "application/reports.html", {
            'reports' : reports
        })
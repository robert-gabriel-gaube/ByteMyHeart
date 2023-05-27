from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.contrib.auth.hashers import make_password, check_password
from application.models import Report, User, DateOffer, Form
from application.forms import LoginForm, ReportForm, UserRegisterForm, BigRegisterForm, DateOfferForm, EditMyProfileForm

user = None
logInUser = None
matchingUsers = None
tournamentUsers = None
round = 0
done = 0

class BlockedView(View):
    def get(self, request):
        return render(request, "application/Blocked.html")

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
        if logInUser.isBanned:
            return HttpResponseRedirect("/blocked")
        if logInUser is None:
            return HttpResponseRedirect("/login")
        return render(request, "application/ViewMyProfile.html", {
            'form' : logInUser.formId
        })
    
class EditMyProfileView(View):
    def get(self, request):
        if logInUser.isBanned:
            return HttpResponseRedirect("/blocked")
        if logInUser is None:
            return HttpResponseRedirect("/login")
        form = EditMyProfileForm()
        return render(request, "application/EditMyProfile.html", {
            'form' : form
        })
    
    def post(self, request):

        form = EditMyProfileForm(request.POST)
    
        if form.is_valid():
            name = form.cleaned_data['name']
            print(name)
            if name != '':
                logInUser.formId.name = name
            logInUser.formId.save()
            logInUser.save()

            age = form.cleaned_data['age']
            if age != '':
                logInUser.formId.age = age
            logInUser.formId.save()
            logInUser.save()

            programming_language = form.cleaned_data['programming_language']
            if programming_language != '':
                logInUser.formId.programming_language = programming_language
            logInUser.formId.save()
            logInUser.save()

            university_specialization = form.cleaned_data['university_specialization']
            if university_specialization != '':
                logInUser.formId.university_specialization = university_specialization
            logInUser.formId.save()
            logInUser.save()

            course_fav1 = form.cleaned_data['course_fav1']
            if course_fav1 != '':
                logInUser.formId.course_fav1 = course_fav1
            logInUser.formId.save()
            logInUser.save()

            course_fav2 = form.cleaned_data['course_fav2']
            if course_fav2 != '':
                logInUser.formId.course_fav2 = course_fav2
            logInUser.formId.save()
            logInUser.save()

            course_fav3 = form.cleaned_data['course_fav3']
            if course_fav3 != '':
                logInUser.formId.course_fav3 = course_fav3
            logInUser.formId.save()
            logInUser.save()

            hobby1 = form.cleaned_data['hobby1']
            if hobby1 != '':
                logInUser.formId.hobby1 = hobby1
            logInUser.formId.save()
            logInUser.save()

            hobby2 = form.cleaned_data['hobby2']
            if hobby2 != '':
                logInUser.formId.hobby2 = hobby2
            logInUser.formId.save()
            logInUser.save()

            hobby3 = form.cleaned_data['hobby3']
            if hobby3 != '':
                logInUser.formId.hobby3 = hobby3
            logInUser.formId.save()
            logInUser.save()

            hobby4 = form.cleaned_data['hobby4']
            if hobby4 != '':
                logInUser.formId.hobby4 = hobby4
            logInUser.formId.save()
            logInUser.save()

            hobby5 = form.cleaned_data['hobby5']
            if hobby5 != '':
                logInUser.formId.hobby5 = hobby5
            logInUser.formId.save()
            logInUser.save()

            gender = form.cleaned_data['gender']
            if gender != '':
                logInUser.formId.gender = gender
            logInUser.formId.save()
            logInUser.save()

            interest = form.cleaned_data['interest']
            if interest != '':
                logInUser.formId.interest = interest
            logInUser.formId.save()
            logInUser.save()

            favorite_algorithm = form.cleaned_data['favorite_algorithm']
            if favorite_algorithm != '':
                logInUser.formId.favorite_algorithm = favorite_algorithm
            logInUser.formId.save()
            logInUser.save()

            favorite_data_structure = form.cleaned_data['favorite_data_structure']
            if favorite_data_structure != '':
                logInUser.formId.favorite_data_structure = favorite_data_structure
            logInUser.formId.save()
            logInUser.save()

            short_description = form.cleaned_data['short_description']
            if short_description != '':
                logInUser.formId.short_description = short_description
            logInUser.formId.save()
            logInUser.save()

            return HttpResponseRedirect("/view-my-profile")
        return render(request, "application/EditMyProfile.html", {
            'form' : form
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
        if logInUser.isBanned:
            return HttpResponseRedirect("/blocked")
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
        if logInUser.isBanned:
            return HttpResponseRedirect("/blocked")
        global round
        round = 0
        return render(request, "application/main_page_users.html",{
            'username': logInUser.username,
        })
    
class IndexPageView(View):
    def get(self, request):
        return render(request, "application/IndexPage.html")
    
class MatchView(View):
    def get(self, request, username):
        if logInUser.isBanned:
            return HttpResponseRedirect("/blocked")
        if logInUser is None:
            return HttpResponseRedirect("/login")

        match = User.objects.get(username=username)
        offers1 = DateOffer.objects.filter(senderId=logInUser, receiverId=match)
        offers2 = DateOffer.objects.filter(receiverId=logInUser, senderId=match)

        offers = offers1 | offers2
        
        display_form = False
        form = DateOfferForm()
        if offers:
            offers = offers.order_by('created_at')
            if offers.last().status == 'DEC':
                display_form = True
        else:
            display_form = True

        return render(request, "application/date_offer.html", {
            'offers': offers,
            'date': match,
            'loggedUser': logInUser,
            'display_form': display_form,
            'form': form
        })
    
    def post(self, request, username):
        form = DateOfferForm(request.POST)
        if form.is_valid():
            date_offer = form.save(commit=False)
            date_offer.senderId = logInUser
            date_offer.receiverId = User.objects.get(username=username)
            date_offer.save()
        return HttpResponseRedirect("/matches/match/" + username)
        
class SetDateOfferView(View):
    def get(self, request, pk, status):
        if logInUser.isBanned:
            return HttpResponseRedirect("/blocked")
        date_offer = DateOffer.objects.get(pk=pk)
        date_offer.status = status
        date_offer.save()
        return HttpResponseRedirect("/matches/match/" + date_offer.senderId.username)
    
class MatchesView(View):
    def get(self, request):
        if logInUser.isBanned:
            return HttpResponseRedirect("/blocked")
        if logInUser is None:
            return HttpResponseRedirect("/login")
        
        return render(request, "application/matches.html", {
            'matches': logInUser.matchId.all()
        })
    
class ViewProfileView(View):
    def get(self, request, username):
        if logInUser.isBanned:
            return HttpResponseRedirect("/blocked")
        if logInUser is None:
            return HttpResponseRedirect("/login")

        user = User.objects.get(username=username)
        return render(request, "application/ViewMyProfile.html", {
            'form': user.formId
        })
class MatchLogicView(View):
    def get(self, request, choice):
        if logInUser.isBanned:
            return HttpResponseRedirect("/blocked")
        global round
        global matchingUsers
        global tournamentUsers
        if round == -1:
            round = 0
        elif round == 0:
            if choice == 1:
                tournamentUsers[0] = matchingUsers[0]
            else:
                tournamentUsers[0] = matchingUsers[1]
            round = 1
            tournamentUsers[7] = matchingUsers[2]
            tournamentUsers[8] = matchingUsers[3]
        elif round == 1:
            if choice == 1:
                tournamentUsers[1] = matchingUsers[2]
            else:
                tournamentUsers[1] = matchingUsers[3]
            round = 2
            tournamentUsers[7] = matchingUsers[4]
            tournamentUsers[8] = matchingUsers[5]
        elif round == 2:
            if choice == 1:
                tournamentUsers[2] = matchingUsers[4]
            else:
                tournamentUsers[2] = matchingUsers[5]
            round = 3
            tournamentUsers[7] = matchingUsers[6]
            tournamentUsers[8] = matchingUsers[7]
        elif round == 3:
            if choice == 1:
                tournamentUsers[3] = matchingUsers[6]
            else:
                tournamentUsers[3] = matchingUsers[7]
            round = 4
            tournamentUsers[7] = tournamentUsers[0]
            tournamentUsers[8] = tournamentUsers[1]
        elif round == 4:
            if choice == 1:
                tournamentUsers[4] = tournamentUsers[0]
            else:
                tournamentUsers[4] = tournamentUsers[1]
            round = 5
            tournamentUsers[7] = tournamentUsers[2]
            tournamentUsers[8] = tournamentUsers[3]
        elif round == 5:
            if choice == 1:
                tournamentUsers[5] = tournamentUsers[2]
            else:
                tournamentUsers[5] = tournamentUsers[3]
            round = 6
            tournamentUsers[7] = tournamentUsers[4]
            tournamentUsers[8] = tournamentUsers[5]

        elif round == 6:
            if choice == 1:
                tournamentUsers[6] = tournamentUsers[4]
            else:
                tournamentUsers[6] = tournamentUsers[5]
            round = 7

        return HttpResponseRedirect("/match")
    


class MatchView(View):
    def get(self, request):
        if logInUser.isBanned:
            return HttpResponseRedirect("/blocked")
        if logInUser is None:
            return HttpResponseRedirect("/login")
        global round
        global matchingUsers
        global tournamentUsers
        global done
        if round == 0:
            matchingUsers = User.objects.all()
            matchingUsers = matchingUsers.exclude(username=logInUser.username)
            matchingUsers = matchingUsers.exclude(role=0)
            done = 0

            for user in logInUser.matchId.all():
                matchingUsers = matchingUsers.exclude(username=user.username)

            tournamentUsers = [None] * 9
            tournamentUsers[7] = matchingUsers[0]
            tournamentUsers[8] = matchingUsers[1]

        elif round == 7:
            logInUser.matchId.add(tournamentUsers[6])
            logInUser.save()
            done = 1
            round = 0


        return render(request, "application/match.html", {
            'player1': matchingUsers[0],
            'player2': matchingUsers[1],
            'player3': matchingUsers[2],
            'player4': matchingUsers[3],
            'player5': matchingUsers[4],
            'player6': matchingUsers[5],
            'player7': matchingUsers[6],
            'player8': matchingUsers[7],
            'winner1': tournamentUsers[0],
            'winner2': tournamentUsers[1],
            'winner3': tournamentUsers[2],
            'winner4': tournamentUsers[3],
            'finalist1': tournamentUsers[4],
            'finalist2': tournamentUsers[5],
            'champion': tournamentUsers[6],
            'choice1': tournamentUsers[7],
            'choice2': tournamentUsers[8],
            'done': done
        })

        

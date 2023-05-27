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
        if logInUser is None:
            return HttpResponseRedirect("/login")
        else:
            if logInUser.role == 0:
                reports = Report.objects.all

                return render(request, "application/reports.html", {
                    'reports' : reports
                })
        
class ViewMyProfileView(View):
    def get(self, request):
        if logInUser is None:
            return HttpResponseRedirect("/login")
        else:
            if logInUser.role == 1:
                if logInUser.isBanned:
                    return HttpResponseRedirect("/blocked")
                if logInUser is None:
                    return HttpResponseRedirect("/login")
                return render(request, "application/ViewMyProfile.html", {
                    'form' : logInUser.formId
                })
        
class EditMyProfileView(View):
    def get(self, request):
        if logInUser is None:
            return HttpResponseRedirect("/login")
        else:
            if logInUser.role == 1:
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
            
            age = form.cleaned_data['age']
            if age != '':
                logInUser.formId.age = age
            
            programming_language = form.cleaned_data['programming_language']
            if programming_language != '':
                logInUser.formId.programming_language = programming_language
            
            university_specialization = form.cleaned_data['university_specialization']
            if university_specialization != '':
                logInUser.formId.university_specialization = university_specialization
            
            course_fav1 = form.cleaned_data['course_fav1']
            if course_fav1 != '':
                logInUser.formId.course_fav1 = course_fav1
            
            course_fav2 = form.cleaned_data['course_fav2']
            if course_fav2 != '':
                logInUser.formId.course_fav2 = course_fav2
            
            course_fav3 = form.cleaned_data['course_fav3']
            if course_fav3 != '':
                logInUser.formId.course_fav3 = course_fav3
            
            hobby1 = form.cleaned_data['hobby1']
            if hobby1 != '':
                logInUser.formId.hobby1 = hobby1
            
            hobby2 = form.cleaned_data['hobby2']
            if hobby2 != '':
                logInUser.formId.hobby2 = hobby2
            
            hobby3 = form.cleaned_data['hobby3']
            if hobby3 != '':
                logInUser.formId.hobby3 = hobby3
            
            hobby4 = form.cleaned_data['hobby4']
            if hobby4 != '':
                logInUser.formId.hobby4 = hobby4
            
            hobby5 = form.cleaned_data['hobby5']
            if hobby5 != '':
                logInUser.formId.hobby5 = hobby5
            
            gender = form.cleaned_data['gender']
            if gender != '':
                logInUser.formId.gender = gender
            
            interest = form.cleaned_data['interest']
            if interest != '':
                logInUser.formId.interest = interest
            
            favorite_algorithm = form.cleaned_data['favorite_algorithm']
            if favorite_algorithm != '':
                logInUser.formId.favorite_algorithm = favorite_algorithm
            
            favorite_data_structure = form.cleaned_data['favorite_data_structure']
            if favorite_data_structure != '':
                logInUser.formId.favorite_data_structure = favorite_data_structure
            
            short_description = form.cleaned_data['short_description']
            if short_description != '':
                logInUser.formId.short_description = short_description
            
            print(logInUser.formId.name)
            
            logInUser.save()

            return HttpResponseRedirect("/view-my-profile")
        return render(request, "application/EditMyProfile.html", {
            'form' : form
        })
    
    
class ReportsActionView(View):
    def get(self, request, pk, username, status):
        if logInUser is None:
            return HttpResponseRedirect("/login")
        else:
            if logInUser.role ==0:
                report = Report.objects.get(pk=pk)
                report.status = 'CSD'
                report.save()
                user = User.objects.get(username=username)
                user.isBanned = status
                user.save()

                return HttpResponseRedirect("/reports")

class ReportView(View):
    def get(self, request, pk):
        if logInUser is None:
            return HttpResponseRedirect("/login")
        else:
            if logInUser.role == 0:
                report = Report.objects.get(pk=pk)
                return render(request, "application/report.html", {
                    'report' : report,
                    'user' : report.receiverID
                })
            
class CreateReportView(View):
    def get(self, request):
        if logInUser is None:
            return HttpResponseRedirect("/login")
        else:
            if logInUser.role == 1:
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
        if logInUser is None:
            return HttpResponseRedirect("/login")
        else:
            if logInUser.role == 1:
                if logInUser.isBanned:
                    return HttpResponseRedirect("/blocked")
                global round
                round = 0
                return render(request, "application/main_page_users.html",{
                    'username': logInUser.username,
                })
            else:
                return HttpResponseRedirect("/")
        
class IndexPageView(View):
    def get(self, request):
        return render(request, "application/IndexPage.html")
    
class ViewMatchView(View):
    def get(self, request, username):
        if logInUser is None:
            return HttpResponseRedirect("/login")
        else:
            if logInUser.role == 1:
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
        if logInUser is None:
            return HttpResponseRedirect("/login")
        else:
            if logInUser.role == 1:
                if logInUser.isBanned:
                    return HttpResponseRedirect("/blocked")
                date_offer = DateOffer.objects.get(pk=pk)
                date_offer.status = status
                date_offer.save()
                return HttpResponseRedirect("/matches/match/" + date_offer.senderId.username)
        
class MatchesView(View):
    def get(self, request):
        if logInUser is None:
            return HttpResponseRedirect("/login")
        else:
            if logInUser.role == 1:
                if logInUser.isBanned:
                    return HttpResponseRedirect("/blocked")
                if logInUser is None:
                    return HttpResponseRedirect("/login")
                
                return render(request, "application/matches.html", {
                    'matches': logInUser.matchId.all()
                })
            
class ViewProfileView(View):
    def get(self, request, username):
        if logInUser is None:
            return HttpResponseRedirect("/login")
        else:
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
        if logInUser is None:
            return HttpResponseRedirect("/login")
        else:
            if logInUser.role == 1:
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
    
from .match_data import hobby_categories, algorithm_categories, data_structure_categories

def getCategory(hobby):
    idx = 0
        
    for category in hobby_categories:
        for subcategory in category:
            if hobby.lower() == subcategory.lower():
                return idx
        idx += 1
    return -1

def getHobbyCategories(user):
    userCategories = []
    for hobby in [user.formId.hobby1, user.formId.hobby2, user.formId.hobby3, user.formId.hobby4, user.formId.hobby5]:
        userCategories.append(getCategory(hobby))
    return userCategories

def ageFormula(age1, age2):
    age_diff = age1 - age2
    if age_diff > -4 and age_diff < 6:
        return 1.0
    elif age_diff >= 30:
        return 0.0
    else:
        return 1.0 - (abs(age_diff) - 5) / 25.0

def algorithmFormula(algorithm1, algorithm2):
    categoryA1 = -1
    categoryA2 = -1
    idx = 0
    for category in algorithm_categories:
        for subcategory in category:
            if algorithm1.lower() in subcategory.lower() or subcategory.lower() in algorithm1.lower():
                categoryA1 = idx
            if algorithm2.lower() in subcategory.lower() or subcategory.lower() in algorithm2.lower():
                categoryA2 = idx
        idx += 1

    if categoryA1 == -1 or categoryA2 == -1:
        return 0.5
    elif categoryA2 == categoryA1:
        return 1.0
    else:
        return 0.0

def dataStructureFormula(dataStructure1, dataStructure2):
    idx = 0
    categoryDS1 = -1
    categoryDS2 = -1

    for category in data_structure_categories:
        for subcategory in category:
            if dataStructure1.lower() in subcategory.lower() or subcategory.lower() in dataStructure1.lower():
                categoryDS1 = idx
            if dataStructure2.lower() in subcategory.lower() or subcategory.lower() in dataStructure2.lower():
                categoryDS2 = idx
        idx += 1
    if categoryDS1 == -1 or categoryDS2 == -1:
        return 0.5
    elif categoryDS2 == categoryDS1:
        return 1.0
    else:
        return 0.0

def getMatchable(availableUsers):
    logedUserCategories = getHobbyCategories(logInUser)
    
    ageScores = []
    hobbyScores = []
    algorithmScores = []
    dataStructureScores = []
    matchabilityScores = []

    for user in availableUsers:
        likeHobby = 0
        userCategories = getHobbyCategories(user)
        for category in logedUserCategories:
            if category != -1 and category in userCategories:
                likeHobby += 1
        hobbyScores.append(likeHobby / 5)
        ageScores.append(ageFormula(logInUser.formId.age))
        algorithmScores.append(algorithmFormula(logInUser.formId.favorite_algorithm, user.formId.favorite_algorithm))
        dataStructureScores.append(dataStructureFormula(logInUser.formId.favorite_data_structure, user.formId.favorite_data_structure))
        matchabilityScores.append(hobbyScores[-1] * 0.5 + ageScores[-1] * 0.2 + algorithmScores[-1] * 0.2 + dataStructureScores[-1] * 0.1)
        
    for i in range(len(matchabilityScores)):
        for j in range(i + 1, len(matchabilityScores)):
            if matchabilityScores[i] < matchabilityScores[j]:
                matchabilityScores[i], matchabilityScores[j] = matchabilityScores[j], matchabilityScores[i]
                availableUsers[i], availableUsers[j] = availableUsers[j], availableUsers[i]

    return availableUsers

class MatchView(View):
    def get(self, request):
        if logInUser is None:
            return HttpResponseRedirect("/login")
        else:
            if logInUser.role == 1:
                if logInUser.isBanned:
                    return HttpResponseRedirect("/blocked")
               
        global round
        global matchingUsers
        global tournamentUsers
        global done

        filteredUsers = []
        if round == 0:
            matchingUsers = User.objects.all()
            matchingUsers = matchingUsers.exclude(username=logInUser.username)
            matchingUsers = matchingUsers.exclude(role=0)
            matchingUsers = matchingUsers.exclude(isBanned=True)
            done = 0

            for user in logInUser.matchId.all():    
                matchingUsers = matchingUsers.exclude(username=user.username)
        
            for user in matchingUsers:
                if user.formId.gender == logInUser.formId.interest:
                    filteredUsers.append(user)

            matchingUsers = filteredUsers

            if len(matchingUsers) < 8:
                return render(request, "application/error.html")


            matchingUsers = getMatchable(matchingUsers)
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
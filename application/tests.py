import datetime
from django.http import HttpResponse
from django.test import TestCase
from .models import DateOffer, Report, User, Form
from django.contrib.auth.hashers import make_password

class ReportsTest(TestCase):
    def setUp(self):
        form = Form(
            name='Robert',
            age=20,
            programming_language='C++',
            university_specialization='CTI',
            course_fav1="IC",
            course_fav2="TS",
            course_fav3="PAA",
            hobby1='singing',
            hobby2='cleaning',
            hobby3='eating',
            hobby4='sleeping',
            hobby5='writing',
            gender='M',
            interest='M',
            favorite_algorithm='rabin-karp',
            favorite_data_structure='Binary Trees',
            short_description='I like programming'
        )
        form.save()

        user = User(
            username='CandyButcher',
            password=make_password("123456"),
            matchId=None,
            formId=form
        )

        user.save()

        report = Report (
            receiverID=user,
            description="Toxic person"
        )

        report.save()
    
    def testReportIsInDatabase(self):
        report = Report.objects.get(description='Toxic person')
        
        self.assertEqual(report.status, "OPN")

class ReportsShowTest(TestCase):
    def setUp(self):
        form = Form(
            name='Robert',
            age=20,
            programming_language='C++',
            university_specialization='CTI',
            course_fav1="IC",
            course_fav2="TS",
            course_fav3="PAA",
            hobby1='singing',
            hobby2='cleaning',
            hobby3='eating',
            hobby4='sleeping',
            hobby5='writing',
            gender='M',
            interest='M',
            favorite_algorithm='rabin-karp',
            favorite_data_structure='Binary Trees',
            short_description='I like programming'
        )
        form.save()

        user = User(
            username='CandyButcher',
            password=make_password("123456"),
            matchId=None,
            formId=form
        )

        user.save()

        report1 = Report (
            receiverID=user,
            description="Toxic person"
        )

        report1.save()

        report2 = Report (
            receiverID=user,
            description="Toxic person as well"
        )

        report2.save()


    def test_reports_page_contains_specific_number_of_li(self):
        expected_li_count = 2 

        response = self.client.get('/reports')
        self.assertEqual(response.status_code, 200) 

        content = response.content.decode('utf-8')

        ul_start_index = content.find('<ul>')
        ul_end_index = content.find('</ul>')  

        ul_content = content[ul_start_index:ul_end_index]  
        ul_content = ul_content.replace('<ul>', '').replace('</ul>', '')
        
        self.assertEqual(ul_content.count('<li id="OPN">'), expected_li_count) 

class ReportsActionTest(TestCase):
    def setUp(self):
        form = Form(
            name='Robert',
            age=20,
            programming_language='C++',
            university_specialization='CTI',
            course_fav1="IC",
            course_fav2="TS",
            course_fav3="PAA",
            hobby1='singing',
            hobby2='cleaning',
            hobby3='eating',
            hobby4='sleeping',
            hobby5='writing',
            gender='M',
            interest='M',
            favorite_algorithm='rabin-karp',
            favorite_data_structure='Binary Trees',
            short_description='I like programming'
        )
        form.save()


        user = User(
            username='CandyButcher',
            password=make_password("123456"),
            matchId=None,
            formId=form
        )

        user.save()

        report = Report (
            receiverID=user,
            description="Toxic person"
        )

        report.save()

    def test_reports_action_page(self):
        report = Report.objects.get(pk=1)
        self.assertEqual(report.status, "OPN")

        user = User.objects.get(username='CandyButcher')
        self.assertEqual(user.isBanned, False)

        response = self.client.get('/reports/action/1/CandyButcher/1')
        self.assertEqual(response.status_code, 302)

        report = Report.objects.get(pk=1)
        self.assertEqual(report.status, "CSD")

        user = User.objects.get(username='CandyButcher')
        self.assertEqual(user.isBanned, True)

    def test_urls_of_reports_action_page(self):
        response = self.client.get('/reports/action/1/CandyButcher/1')
        self.assertEqual(response.status_code, 302)

        response = self.client.get('/reports/action/1/CandyButcher/0')
        self.assertEqual(response.status_code, 302)

        try:
            response = self.client.get('/reports/action/1/CandyButcher/2')
            gotPage = 1
        except:
            gotPage = 0

        self.assertEqual(gotPage, 0)

    def test_a_href_in_report_page(self):
        response = self.client.get('/reports/action/1/CandyButcher/1')
        self.assertEqual(response.status_code, 302)

        response = self.client.get('/reports')
        self.assertEqual(response.status_code, 200)

        content = response.content.decode('utf-8')

        a_start_index = content.find('<a')
        a_end_index = content.find('</a>')

        a_content = content[a_start_index:a_end_index]
        self.assertEqual(a_content[:11], '<a href="#"')

class CreateReportTest(TestCase):
    def setUp(self):
        form = Form(
            name='Robert',
            age=20,
            programming_language='C++',
            university_specialization='CTI',
            course_fav1="IC",
            course_fav2="TS",
            course_fav3="PAA",
            hobby1='singing',
            hobby2='cleaning',
            hobby3='eating',
            hobby4='sleeping',
            hobby5='writing',
            gender='M',
            interest='M',
            favorite_algorithm='rabin-karp',
            favorite_data_structure='Binary Trees',
            short_description='I like programming'
        )
        form.save()


        user = User(
            username='CandyButcher',
            password=make_password("123456"),
            matchId=None,
            formId=form
        )

        user.save()
    
    def test_create_report_page(self):
        response = self.client.get('/create-report/')
        self.assertEqual(response.status_code, 200)

    def test_create_report_page_post(self):
        response = self.client.post('/create-report/', {
            'description': 'Toxic person',
            'receiverID': 1
        })
        self.assertEqual(response.status_code, 302)

        report = Report.objects.get(pk=1)
        self.assertEqual(report.status, "OPN")
        self.assertEqual(report.receiverID.username, "CandyButcher")


class UserRegisterFormTest(TestCase):
    def test_user_register_form_page(self):
        response = self.client.get('/register')
        self.assertEqual(response.status_code, 200)

    def test_user_register_form_page_post(self):
        response = self.client.post('/register', {
            'username': 'Fermecatu',
            'password': '123456',
        })
        self.assertEqual(response.status_code, 302)
        user=User.objects.get(username='Fermecatu')
        self.assertIsNotNone(user)
        response = self.client.post('/interestform', {  
            'name': 'Andrei',
            'age': 20,
            'programming_language':'C',
            'university_specialization':'ETTI',
            'course_fav1':"IC",
            'course_fav2':"TS",
            'course_fav3':"CD",
            'hobby1':'coding',
            'hobby2':'editing',
            'hobby3':'analyzing',
            'hobby4':'sleeping',
            'hobby5':'cooking',
            'gender':'M',
            'interest':'F',
            'favorite_algorithm':'viterbi',
            'favorite_data_structure':'Graphs',
            'short_description':'I like programming'})
        self.assertEqual(response.status_code, 302)
        form=Form.objects.get(name='Andrei')
        self.assertIsNotNone(form)
        user=User.objects.get(username='Fermecatu')
        self.assertEquals(user.formId.name, 'Andrei')

class UserLoginFormTest(TestCase):
    def test_user_login_form_page(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_user_login_form_page_post(self):
        user = User(
            username='Fermecatu',
            password=make_password("123456"),
            matchId=None,
            formId=None
        )
        user.save()
        response = self.client.post('/login', {
            'username': 'Fermecatu',
            'password': '123456',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/user-main-page')
    def test_admin_login_form_page_post(self):
        user = User(
            username='admin',
            password=make_password("admin"),
            matchId=None,
            formId=None,
            role=0
        )
        user.save()
        response = self.client.post('/login', {
            'username': 'admin',
            'password': 'admin',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/reports')

    def test_user_login_form_page_post_wrong_password(self):
        user = User(
            username='Fermecatu',
            password=make_password("123456"),
            matchId=None,
            formId=None
        )
        user.save()
        response = self.client.post('/login', {
            'username': 'Fermecatu',
            'password': '1234567',
        })
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, HttpResponse)

class DateOfferModelTest(TestCase):
    def setUp(self):
        user1 = User(
            username='Fermecatu',
            password=make_password("123456"),
            matchId=None,
            formId=None
        )
        user1.save()
        user2 = User(
            username='CandyButcher',
            password=make_password("123456"),
            matchId=None,
            formId=None
        )
        user2.save()
        date_offer = DateOffer(
            senderId=user1,
            receiverId=user2,
            status="OPN",
            date_idea="Go to the cinema",
            date_time=datetime.datetime.now(),
            date_location="Cinema City"
        )
        date_offer.save()

    def test_date_offer_created(self):
        date_offer = DateOffer.objects.get(pk=1)
        self.assertEqual(date_offer.status, "OPN")
        self.assertEqual(date_offer.senderId.username, "Fermecatu")
        self.assertEqual(date_offer.receiverId.username, "CandyButcher")
        
    def test_change_offer_to_accepted(self):
        date_offer = DateOffer.objects.get(pk=1)
        date_offer.status = "ACC"
        date_offer.save()
        self.assertEqual(date_offer.status, "ACC")
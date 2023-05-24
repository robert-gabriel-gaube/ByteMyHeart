from django.test import TestCase
from .models import Report, User, Form
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
from django.test import TestCase,Client
from django.contrib.auth.models import User
from django.utils import timezone
from . import models
from django.urls import reverse
# Create your tests here.



class TaskCreateViewsTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.user=User.objects.create_user(username="test", password="test")
        cls.create_path=reverse("to_do:create_view")
        return super().setUpClass()

    def test_login_check(self):
        client_1=Client()
        resp_1=client_1.get(self.create_path)
        resp_2=client_1.get(reverse("to_do:create_function"))
        print(resp_1.status_code, " is the status code")
        print(dir(resp_1))
        self.assertEqual(resp_1.url,reverse("to_do:login_redirect", ), )
        self.assertEqual(resp_2.url,reverse("to_do:login"))

    def test_cbv_create_view(self):
            """
            Test the class-based Create View
            """

            client_1=Client()
            authorised=client_1.login(username="test", password="test")
            self.assertTrue(authorised)

            data={"title":"Test Title","description":"Test Description" ,"due_date":timezone.now()}
            client_1.post(path=self.create_path,data=data)
            self.assertEqual(models.Task.objects.count(),1)
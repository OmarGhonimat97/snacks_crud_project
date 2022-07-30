from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Snack

# Create your tests here.


class SnackTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test', email='test@test.com',
            password='test@12345'
        )
        self.snack = Snack.objects.create(
            name="Test",
            description='test',
            purchaser=self.user,
        )

    def test_list_status(self):
        url = reverse("snacks_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_template(self):
        url = reverse("snacks_list")
        response = self.client.get(url)

        self.assertTemplateUsed(response, 'snacks_list.html')

    def test_str_method(self):
        self.assertEqual(str(self.snack), 'Test')

    def test_detail_view(self):
        url = reverse('snack_detail', args=[self.snack.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snack_detail.html')

    def test_create_view(self):
        url = reverse('snack_create')
        data = {
            "name": "Test Create",
            "purchaser": self.user.id
        }
        response = self.client.post(path=url, data=data, follow=True)
        self.assertTemplateUsed(response, 'snack_detail.html')
        self.assertRedirects(response, reverse('snack_detail', args=[2]))
        self.assertEqual(len(Snack.objects.all()), 2)

    def test_update_view(self):
        url = reverse('snack_update', args=[self.snack.id])
        data = {
            "name": "Test Update",
            "purchaser": self.user.id,
            "description": "test",
        }
        response = self.client.post(path=url, data=data, follow=True)
        self.assertTemplateUsed(response, 'snack_detail.html')
        self.assertRedirects(response, reverse('snack_detail', args=[1]))
        self.assertEqual(self.snack.name, 'Test')

    def test_delete_view(self):
        url = reverse('snack_delete', args=[self.snack.id])

        response = self.client.post(path=url, follow=True)

        self.assertTemplateUsed(response, "snacks_list.html")
        self.assertRedirects(response, reverse("snacks_list"))

    def test_string_repr(self):
        snack = Snack(name="test")
        self.assertEqual(str(snack), snack.name)

    def test_fields(self):
        self.assertEqual(self.snack.name, 'Test')
        self.assertEqual(self.snack.purchaser, self.user)
        self.assertEqual(self.snack.description, 'test')

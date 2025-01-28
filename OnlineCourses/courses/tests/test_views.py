from django.test import TestCase, Client
from django.urls import reverse
from courses.models import ContactMessage
from courses.forms import ContactForm


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/home.html')
        self.assertIn('current_year', response.context)

    def test_contact_view_get(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/contact.html')
        self.assertIsInstance(response.context['form'], ContactForm)

    def test_contact_view_post_valid(self):
        data = {
            'name': 'Test User',
            'email': 'testuser@example.com',
            'reason': 'support',
            'message': 'This is a test message.'
        }
        response = self.client.post(reverse('contact'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/contact.html')
        self.assertContains(response, "Wiadomość wysłana! Odpowiem najszybciej jak to możliwe.")
        self.assertTrue(ContactMessage.objects.filter(email='testuser@example.com').exists())

    def test_contact_view_post_invalid(self):
        data = {
            'name': 'Test User',
            'email': 'invalid-email',
            'reason': 'support',
            'message': 'This is a test message.'
        }
        response = self.client.post(reverse('contact'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/contact.html')
        self.assertFalse(ContactMessage.objects.filter(email='invalid-email').exists())
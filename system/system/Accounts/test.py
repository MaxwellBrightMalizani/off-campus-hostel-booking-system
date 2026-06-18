from django.test import TestCase, Client
from django.urls import reverse
from .models import CustomUser


class RegistrationTests(TestCase):

    def setUp(self):
        self.client       = Client()
        self.register_url = reverse('accounts:register')

    def test_student_registers_with_student_id(self):
        """A student can register when a student_id is provided."""
        self.client.post(self.register_url, {
            'email':      'student@nrc.ac.mw',
            'first_name': 'Jane',
            'last_name':  'Banda',
            'user_type':  'student',
            'student_id': 'NRC2024001',
            'password1':  'StrongPass123!',
            'password2':  'StrongPass123!',
        })
        self.assertEqual(CustomUser.objects.count(), 1)
        user = CustomUser.objects.first()
        self.assertEqual(user.user_type, 'student')
        self.assertEqual(user.student_id, 'NRC2024001')

    def test_student_registration_fails_without_student_id(self):
        """A student cannot register without a student_id."""
        response = self.client.post(self.register_url, {
            'email':      'student2@nrc.ac.mw',
            'first_name': 'John',
            'last_name':  'Phiri',
            'user_type':  'student',
            'student_id': '',
            'password1':  'StrongPass123!',
            'password2':  'StrongPass123!',
        })
        self.assertEqual(CustomUser.objects.count(), 0)
        self.assertContains(response, "Student ID is required")

    def test_owner_registers_without_student_id(self):
        """A hostel owner can register without a student_id."""
        self.client.post(self.register_url, {
            'email':      'owner@example.com',
            'first_name': 'Grace',
            'last_name':  'Msiska',
            'user_type':  'owner',
            'student_id': '',
            'password1':  'StrongPass123!',
            'password2':  'StrongPass123!',
        })
        self.assertEqual(CustomUser.objects.count(), 1)
        user = CustomUser.objects.first()
        self.assertEqual(user.user_type, 'owner')
        self.assertIsNone(user.student_id)

    def test_duplicate_email_rejected(self):
        """Registering with an already-used email should fail."""
        CustomUser.objects.create_user(
            email='taken@nrc.ac.mw', password='Pass123!', user_type='student', student_id='S001'
        )
        response = self.client.post(self.register_url, {
            'email':      'taken@nrc.ac.mw',
            'first_name': 'Duplicate',
            'last_name':  'User',
            'user_type':  'student',
            'student_id': 'S002',
            'password1':  'StrongPass123!',
            'password2':  'StrongPass123!',
        })
        self.assertEqual(CustomUser.objects.count(), 1)


class LoginLogoutTests(TestCase):

    def setUp(self):
        self.client    = Client()
        self.login_url = reverse('accounts:login')
        self.user = CustomUser.objects.create_user(
            email='test@nrc.ac.mw',
            password='StrongPass123!',
            user_type='student',
            student_id='NRC999',
        )

    def test_login_with_correct_credentials(self):
        response = self.client.post(self.login_url, {
            'email':    'test@nrc.ac.mw',
            'password': 'StrongPass123!',
        })
        self.assertRedirects(response, reverse('listings:home'))

    def test_login_with_wrong_password_shows_error(self):
        response = self.client.post(self.login_url, {
            'email':    'test@nrc.ac.mw',
            'password': 'WrongPassword!',
        })
        self.assertContains(response, "Invalid email or password")

    def test_logout_redirects_to_login(self):
        self.client.login(email='test@nrc.ac.mw', password='StrongPass123!')
        response = self.client.get(reverse('accounts:logout'))
        self.assertRedirects(response, reverse('accounts:login'))

    def test_unauthenticated_user_redirected_to_login(self):
        """Accessing login page while logged out should show the login form."""
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Login")


class RoleTests(TestCase):

    def setUp(self):
        self.student = CustomUser.objects.create_user(
            email='s@nrc.ac.mw', password='pass', user_type='student', student_id='S1'
        )
        self.owner = CustomUser.objects.create_user(
            email='o@example.com', password='pass', user_type='owner'
        )

    def test_is_student_returns_true_for_student(self):
        self.assertTrue(self.student.is_student())
        self.assertFalse(self.student.is_owner())

    def test_is_owner_returns_true_for_owner(self):
        self.assertTrue(self.owner.is_owner())
        self.assertFalse(self.owner.is_student())

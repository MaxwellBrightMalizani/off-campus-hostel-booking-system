from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    """
    Custom user model using email as the unique identifier.
    user_type controls what each user can do in the system.
    """

    class UserType(models.TextChoices):
        STUDENT = 'student', 'Student'
        OWNER   = 'owner',   'Hostel Owner'
        ADMIN   = 'admin',   'Admin'

    # Remove username — email is the login field
    username = None

    email = models.EmailField('email address', unique=True)

    user_type = models.CharField(
        max_length=10,
        choices=UserType.choices,
        default=UserType.STUDENT,
    )

    # Required for students only; null/blank for owners
    student_id = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text="Required for students only.",
    )

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    # --- Role helpers used by decorators and templates ---

    def is_student(self):
        return self.user_type == self.UserType.STUDENT

    def is_owner(self):
        return self.user_type == self.UserType.OWNER

    def is_admin_user(self):
        return self.is_superuser or self.user_type == self.UserType.ADMIN

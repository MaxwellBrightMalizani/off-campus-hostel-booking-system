from functools import wraps
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages


def student_required(view_func):
    """
    Allows access only to authenticated users with user_type == 'student'.
    Usage:
        @student_required
        def my_view(request): ...
    """
    @wraps(view_func)
    @login_required
    def _wrapped(request, *args, **kwargs):
        if not request.user.is_student():
            messages.error(request, "This page is accessible to students only.")
            return redirect('listings:home')
        return view_func(request, *args, **kwargs)
    return _wrapped


def owner_required(view_func):
    """
    Allows access only to authenticated users with user_type == 'owner'.
    Usage:
        @owner_required
        def my_view(request): ...
    """
    @wraps(view_func)
    @login_required
    def _wrapped(request, *args, **kwargs):
        if not request.user.is_owner():
            messages.error(request, "This page is accessible to hostel owners only.")
            return redirect('listings:home')
        return view_func(request, *args, **kwargs)
    return _wrapped

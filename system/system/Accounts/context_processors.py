def user_role(request):
    """
    Injects role-checking booleans into every template context.
    Used by base.html to show/hide navbar links per role.
    """
    if request.user.is_authenticated:
        return {
            'is_student_user': request.user.is_student(),
            'is_owner_user':   request.user.is_owner(),
        }
    return {
        'is_student_user': False,
        'is_owner_user':   False,
    }

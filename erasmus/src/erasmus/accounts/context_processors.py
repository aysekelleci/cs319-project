from .models import User
from .models import ErasmusUser, Student, Coordinator, BoardMember


def get_user_type(request):
    user_type = None
    if request is None:
        return user_type


    Students = Student.objects.all()
    Coordinators = Student.objects.all()
    user = request.user
    if user.is_authenticated:
        erasmus_user = ErasmusUser.objects.filter(user=user).first()
        if erasmus_user is not None:
            if Coordinator.objects.filter(user=erasmus_user).first():
                user_type = "Coordinator"
            elif Student.objects.filter(user=erasmus_user).first():
                user_type = "Student"
            else:
                user_type = "Board Member"

    return {'user_ty': user_type}



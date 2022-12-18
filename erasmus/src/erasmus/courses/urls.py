from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from . import views
from django.urls import path, include

app_name = 'communication'

urlpatterns = [

    path('courses/', views.CourseView.as_view(), name="courses"),
    path('add-to-courses/<int:course_id>', views.AddCourseView.as_view(), name="add-course"),
    path('remove-from-courses/<int:course_id>', views.DeleteCourseView.as_view(), name="remove-course"),
    path('add-unapproved-course/', views.AddUnapprovedCourse.as_view(), name="add-unapproved-course"),
    path('add-bilkent-course/', views.AddBilkentCourse.as_view(), name="add-bilkent-course"),
    path('documents/', views.DocumentView.as_view(), name="documents"),
    path('waiting-courses/', views.GetWaitingCoursesView.as_view(), name="waiting-courses"),
    path('approve-course/<int:course_id>', views.ApproveCoursesView.as_view(), name="approve-courses"),
    path('reject-course/<int:course_id>', views.RejectCourseView.as_view(), name="reject-courses"),
    path('merge-course/<int:course_id1>/<int:course_id2>/<int:course_id3>/<int:course_id4>/<int:course_id5>/<int:course_id6>/'
         '<int:course_id7>/<int:course_id8>/<int:course_id9>/<int:course_id10>',
         views.MergeCourseView.as_view(), name="merge-courses"),
    path('create-document/', views.CreatePreApprovalView.as_view(), name="create-document"),
 #   path('create-document/', views.CreateLearningAgreementView.as_view(), name="create-document"),
    path('upload-documents/<int:from_student_profile>/<int:viewed_student_id>', views.UploadDocumentView.as_view(), name="upload-documents"),
    path('create-document/', views.CreatePreApprovalView.as_view(), name="create-document"),
    path('delete-document/<int:document_id>', views.DeleteDocumentView.as_view(), name="delete-document"),
    path('', include('communication.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

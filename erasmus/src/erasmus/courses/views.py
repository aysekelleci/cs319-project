import docx
import pytz
import os
from datetime import datetime

from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files import File
from courses.forms import CourseForm, DocumentForm
from .models import Course, Document, MergedCourse, MUST_COURSE, ELECTIVE_COURSE, PREAPPROVAL_FORM, STATIC_DOCUMENTS_FOLDER
from accounts.models import UserCourse, Student, ErasmusUser, Coordinator, ToDo, BoardMember

import os
from django.conf import settings
from django.http import HttpResponse, Http404

def download(request, path):
    # get the download path
    download_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(download_path):

        with open(download_path, 'rb') as fh:

            response = HttpResponse(fh.read(), content_type="application/document")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(download_path)
            return response
    raise Http404

class CourseView(LoginRequiredMixin,View):
    def get(self, request):
        student = None
        user = request.user
        approved_unmerged_courses = None
        approved_merged_course_dict = None
        user_unmerged_courses = None
        user_merged_course_dict = None
        erasmus_user = ErasmusUser.objects.get(user=user)
        if Coordinator.objects.filter(user=erasmus_user).first():
            user_type = "Coordinator"

        elif Student.objects.filter(user=erasmus_user).first():
            user_type = "Student"
            student = Student.objects.filter(user=erasmus_user).first()
            # get preapproved courses for the university the student will be attending
            _approved_courses = Course.objects.filter(university=student.university, approved=True)
            _approved_merged_courses = {course.merged_course for course in _approved_courses if course.is_merged is True}
            approved_merged_course_dict = getMergedCoursesDict(_approved_courses, _approved_merged_courses)
            approved_unmerged_courses = [course for course in _approved_courses if course.is_merged is False]

            _courses_user = [user_course.course for user_course in UserCourse.objects.filter(user=student)]
            _merged_courses = {course.merged_course for course in _courses_user if course.is_merged is True}
            user_merged_course_dict = getMergedCoursesDict(_courses_user, _merged_courses)
            user_unmerged_courses = [course for course in _courses_user if course.is_merged is False]

            rejected_courses = Course.objects.filter(university=student.university, is_rejected=True)
        else:
            user_type = "Board Member"

        context = {'user': user, 'approved_unmerged_courses': approved_unmerged_courses,
                   "approved_merged_course_dict": approved_merged_course_dict, "user_type": user_type, 'student': student,
                   'user_unmerged_courses': user_unmerged_courses, 'user_merged_course_dict': user_merged_course_dict,
                   'rejected_courses': rejected_courses}

        return render(request, 'courses/courses.html', context)
def getMergedCoursesDict(courses, merged_courses):
    merged_course_dict = {}
    for merged_course in merged_courses:
        one_merged_course_contents = []  # each list contains the courses composing one merged course
        for course in courses:
            if ( course.is_merged and (course.merged_course.pk is merged_course.pk) ):
                one_merged_course_contents.append(course)
        merged_course_dict[merged_course] = one_merged_course_contents
    return merged_course_dict

class AddCourseView(LoginRequiredMixin, View):
    def get(self, request, course_id):
        course = get_object_or_404(Course, pk=course_id)  # Check whether given course object exists
        user = request.user
        erasmus_user = ErasmusUser.objects.get(user=user)
        student = Student.objects.get(user=erasmus_user)  # get which student wants to add approved course
        try:
            course_item = UserCourse.objects.get(user=student,
                                                 course=course)  # control whether course item already added
        except:
            course_item = None
        if course_item is not None:
            messages.error(request, "This course already added to course list.")
            return redirect("/courses")

        else:
            course = UserCourse.objects.create(user=student, course=course)
            messages.success(request, "This course was added to your course list.")
            return redirect("/courses")


class DeleteCourseView(LoginRequiredMixin,View):
    def get(self, request, course_id):
        user = request.user
        erasmus_user = ErasmusUser.objects.get(user=user)
        student = Student.objects.get(user=erasmus_user)  # get which student wants to add approved course
        course = get_object_or_404(Course, pk=course_id)

        try:
            course_item = UserCourse.objects.get(user=student, course=course)  # control whether course item already added
        except:
            course_item = None
        if course_item is not None:
            course_item.delete()
            messages.success(request, "This item removed from course list.")
        return redirect("/courses")


class AddUnapprovedCourse(LoginRequiredMixin, View):

    def get(self, request):
        username = request.user.username

        new_course = None

        course_form = CourseForm()

        return render(request,
                      'courses/add_unapproved_course.html',
                      {'new_course': new_course,
                       'course_form': course_form,
                       'username': username})

    def post(self, request):
        user = request.user
        username = user.username
        erasmus_user = ErasmusUser.objects.get(user=user)
        student = Student.objects.filter(user=erasmus_user).first()

        course_form = CourseForm(data=request.POST)
        if course_form.is_valid():
            # Create course object but don't save to database yet
            new_course = course_form.save(commit=False)

            # Save the course to the database
            new_course.save()

            # Create a course specific for the user as well
            new_user_course = UserCourse(course=new_course, user=student)
            new_user_course.save()

            # add a todo item for the coordinator to evaluate the unapproved course
            coordinator_todo = ToDo(header=f"Evaluate new unapproved course of {erasmus_user.name}", user=student.coordinator.user,
                                    link="waiting-courses/")
            coordinator_todo.save()

        else:
            messages.info(request, "Course Form is not valid")
            return redirect("add_unapproved_course")

        return render(request,
                      'courses/add_unapproved_course.html',
                      {'new_course': new_course,
                       'course_form': course_form,
                       'username': username})


class DocumentView(LoginRequiredMixin, View):
    def get(self, request):
        documents = Document.objects.all()
        user = request.user

        context = {'documents': documents}
        return render(request, 'courses/documents.html', context)


class UploadDocumentView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        student = None
        document_form = DocumentForm()
        erasmus_user = ErasmusUser.objects.filter(user=user).first()
        if erasmus_user is not None:
            student = Student.objects.filter(user=erasmus_user).first()
        if student is None:
            redirect("/login")

        context = {'student': student, 'document_form': document_form}
        return render(request, 'courses/upload-documents.html', context)

    def post(self, request):
        student = None
        user = request.user
        erasmus_user = ErasmusUser.objects.filter(user=user).first()
        if erasmus_user is not None:
            student = Student.objects.filter(user=erasmus_user).first()
        if student is None:
            redirect("/login")

        else:
            document_form = DocumentForm(request.POST, request.FILES)

            if document_form.is_valid():
                new_document = document_form.save(commit=False)
                new_document.user = student

                # Save the document to the database
                new_document.save()

            else:
                messages.info(request, "Comment form is not valid")
                return redirect("/courses")

            messages.info(request, "Document is added")
            context = {'student': student, 'document_form': document_form, 'new_document': new_document}
            return render(request, 'courses/upload-documents.html', context)

class DownloadDocument(View):
    def get(self, request, document_id):
        document = get_object_or_404(Document, pk=document_id)


class DeleteDocumentView(LoginRequiredMixin, View):
    def get(self, request, document_id):
        user = request.user
        erasmus_user = ErasmusUser.objects.filter(user=user).first()
        if erasmus_user is not None:
            student = Student.objects.filter(user=erasmus_user).first()
            document = get_object_or_404(Document, pk=document_id, user=student)

            document.delete()

        return redirect("/documents")



class GetWaitingCoursesView(LoginRequiredMixin, View):
    def get(self, request):
        unapproved_courses = UserCourse.objects.filter(course__approved__exact=False, course__is_rejected__exact=False)
        user = request.user
        erasmus_user = ErasmusUser.objects.filter(user=user).first()
        coordinator = Coordinator.objects.filter(user=erasmus_user).first()
        if coordinator is None:
            redirect("accounts/profile")

        else:
            context = {'coordinator': coordinator, 'unapproved_courses': unapproved_courses}
            return render(request, 'courses/waiting_courses.html', context)


class ApproveCoursesView(LoginRequiredMixin, View):
    def get(self, request, course_id):
        unapproved_courses = Course.objects.filter(approved=False)
        user = request.user
        erasmus_user = ErasmusUser.objects.filter(user=user).first()
        coordinator = Coordinator.objects.filter(user=erasmus_user).first()
        if coordinator is None:
            return redirect("accounts/profile")

        else:
            course = Course.objects.filter(pk=course_id).first()
            if course is not None:
                course.approved = True
                course.save()

        return redirect("/waiting-courses/")


class RejectCourseView(LoginRequiredMixin, View):
    def get(self, request, course_id):
        unapproved_courses = Course.objects.filter(approved=False)
        user = request.user
        erasmus_user = ErasmusUser.objects.filter(user=user).first()
        coordinator = Coordinator.objects.filter(user=erasmus_user).first()
        if coordinator is None:
            return redirect('accounts/profile')

        else:
            course = Course.objects.filter(pk=course_id).first()
            if course is not None:
                course.is_rejected = True
                course.save()

        return redirect('/waiting-courses/')

class MergeCourseView(LoginRequiredMixin, View):
    def get(self, request, bilkent_eq_id, course_id1, course_id2, course_id3, course_id4, course_id5,
            course_id6, course_id7, course_id8, course_id9, course_id10):

        if not Course.objects.filter(pk=course_id1).exists() and not Course.objects.filter(pk=course_id2).exists():
            # get the bilkent equivalent course
            bilkent_equivalent = Course.objects.filter(pk=bilkent_eq_id).first()

            # create a "parent" merged course instance
            merged_course = MergedCourse(bilkent_equivalent=bilkent_equivalent)
            merged_course.save()

            course_ids = [course_id1, course_id2, course_id3, course_id4, course_id5, course_id6, course_id7, course_id8,
                          course_id9, course_id10]

            # merge up to 10 courses by designating their parent course as the created MergedCourse instance
            for course_id in course_ids:
                course = Course.objects.filter(pk=course_id).first()
                if course is not None:
                    course.is_merged = True
                    course.merged_course = merged_course
                    course.save()

            return redirect("add_unapproved_course")
        else:
            messages.info(request, "You need to choose at least two courses to merge.")
            return redirect("add_unapproved_course")

from abc import ABC, abstractmethod
class CreateDocumentView(LoginRequiredMixin, View, ABC):
    @abstractmethod
    def fill_necessary_information(self, student):
        pass
    def get(self, request):
        user = request.user
        erasmus_user = ErasmusUser.objects.filter(user=user).first()
        student = Student.objects.filter(user=erasmus_user).first()

        document_name, date, document_type = self.fill_necessary_information(student)

        with open(document_name, 'rb') as f:
            new_pre_approval = Document(document_name='Unsigned ' + document_type.lower() + ' of ' + erasmus_user.name,
                                        date=date, is_signed=False, user=student,
                                        document_type=document_type)
            new_pre_approval.document = File(f, name=os.path.basename(f.name))
            new_pre_approval.save()

        return redirect("/courses")

class CreatePreApprovalView(CreateDocumentView):
    def fill_necessary_information(self, student):
        # read the template pre-approval form and its tables
        document = docx.api.Document('courses/static/pre_approval_form.docx')
        student_info_table = document.tables[0]
        host_uni_table = document.tables[1]
        courses_table = document.tables[2]
        coordinator_table = document.tables[3]

        student_info_table.cell(0, 1).text = student.user.name.split()[:-1]  # name
        student_info_table.cell(0, 3).text = str(student.user.bilkent_id)  # bilkent id number
        student_info_table.cell(1, 1).text = student.user.name.split()[-1]  # surname
        student_info_table.cell(1, 3).text = student.user.department  # department

        host_uni_table.cell(0, 1).text = student.university.university_name  # host university name
        host_uni_table.cell(0, 3).text = student.academic_year  # academic year
        host_uni_table.cell(1, 3).text = student.semester  # semester

        courses = UserCourse.objects.filter(user=student)

        for i, user_course in enumerate(courses):
            course = user_course.course
            bilkent_equivalent = course.bilkent_equivalent
            courses_table.cell(2 + i, 1).text = course.code  # course code
            courses_table.cell(2 + i, 2).text = course.course_name  # course name
            courses_table.cell(2 + i, 3).text = str(course.course_credit)  # course credit
            if bilkent_equivalent is not None:
                if bilkent_equivalent.course_type == MUST_COURSE:  # bilkent course name
                    courses_table.cell(2 + i, 4).text = bilkent_equivalent.code + " " + \
                                                        bilkent_equivalent.course_name
                elif bilkent_equivalent.course_type == ELECTIVE_COURSE:
                    courses_table.cell(2 + i, 4).text = bilkent_equivalent.elective_group_name
                courses_table.cell(2 + i, 5).text = str(bilkent_equivalent.course_credit)  # bilkent course credit
                if bilkent_equivalent.course_type == ELECTIVE_COURSE:  # bilkent elective course code
                    courses_table.cell(2 + i, 6).text = bilkent_equivalent.code

        coordinator_table.cell(1, 1).text = student.coordinator.user.name  # coordinator name

        turkey_timezone = pytz.timezone("Turkey")
        date = datetime.now(turkey_timezone)
        document_name = STATIC_DOCUMENTS_FOLDER + 'pre_approval_form' + date.strftime("%d-%m-%Y-%H-%M-%S") + ".docx"
        document.save(document_name)

        return document_name, date, PREAPPROVAL_FORM


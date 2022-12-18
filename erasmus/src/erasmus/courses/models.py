import os

from django.db import models
# Create your models here.


MUST_COURSE = "Must"
ELECTIVE_COURSE = "Elective"
LEARNING_AGREEMENT = "Learning Agreement"
PREAPPROVAL_FORM = "Pre-Approval Form"
COURSE_TRANSFER_FORM = "Course Transfer Form"
OTHER_DOCUMENT = "Other"

STATIC_DOCUMENTS_FOLDER = "static/documents/documents/"

COURSE_TYPE_CHOICES = (
    (MUST_COURSE, MUST_COURSE), (ELECTIVE_COURSE, ELECTIVE_COURSE)
)


class University(models.Model):
    university_name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    lowest_grade = models.CharField(max_length=20)
    highest_grade = models.CharField(max_length=20)
    passing_grade = models.CharField(max_length=20)
    inverted_scale = models.BooleanField(default=False)
    department = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.university_name)

class BilkentCourse(models.Model):
    course_name = models.CharField(max_length=100, blank=True)
    course_code = models.CharField(max_length=20, blank=True)
    course_credit = models.FloatField()
    course_type = models.CharField(max_length=30, choices=COURSE_TYPE_CHOICES)
    elective_group_name = models.CharField(max_length=100, blank=True)
    course_coordinator_name = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return '{}'.format(self.course_code + ": " + self.course_name)



class MergedCourse(models.Model):
    approved = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    bilkent_equivalent = models.ForeignKey(BilkentCourse, on_delete=models.SET_NULL, null=True)

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, default="")
    course_credit = models.FloatField()
    university = models.ForeignKey(University, on_delete=models.CASCADE, null=True, related_name='courses')
    bilkent_equivalent = models.ForeignKey(BilkentCourse, on_delete=models.SET_NULL, null=True)
    approved = models.BooleanField(default=False)
    merged_course = models.ForeignKey(MergedCourse, on_delete=models.SET_NULL, blank=True, null=True)
    is_merged = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.code + ": " + self.course_name)


DOCUMENT_TYPE_CHOICES = (
    (LEARNING_AGREEMENT, LEARNING_AGREEMENT),
    (PREAPPROVAL_FORM, PREAPPROVAL_FORM),
    (COURSE_TRANSFER_FORM, COURSE_TRANSFER_FORM),
    (OTHER_DOCUMENT, OTHER_DOCUMENT),
)


class Document(models.Model):
    document_name = models.CharField(max_length=50)
    document = models.FileField(upload_to=STATIC_DOCUMENTS_FOLDER)
    date = models.DateTimeField(auto_now_add=True)
    is_signed = models.BooleanField(default=False) # whether student signed
    is_signed_coordinator = models.BooleanField(default=False)
    user = models.ForeignKey('accounts.Student', on_delete=models.CASCADE, related_name='documents', default=1)
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPE_CHOICES, default=4)

    def get_file_format(self):
        _, file_format = os.path.splitext(self.document.name)
        return file_format[1:]








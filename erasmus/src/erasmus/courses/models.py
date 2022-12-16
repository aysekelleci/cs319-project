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
    department = models.CharField(max_length=200) # fixme supposed to be a list of strings

    def __str__(self):
        return '{}'.format(self.university_name)


class MergedCourse(models.Model):
    course_type = models.CharField(max_length=30)
    bilkent_equivalent = models.ForeignKey("Course", on_delete=models.SET_NULL, blank=True,
                                           null=True)


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_codes = models.CharField(max_length=20)
    course_credit = models.FloatField()
    university = models.ForeignKey(University, on_delete=models.CASCADE, null=True, related_name='courses')
    bilkent_equivalent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    approved = models.BooleanField(default=False)
    course_type = models.CharField(max_length=30, choices=COURSE_TYPE_CHOICES)
    elective_group_name = models.CharField(max_length=100, blank=True)
    course_coordinator_name = models.CharField(blank=True, max_length=100)
    merged_course = models.ForeignKey(MergedCourse, on_delete=models.SET_NULL, blank=True, null=True)
    is_merged = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.course_codes + ": " + self.course_name)


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
    is_signed = models.BooleanField(default=False)
    user = models.ForeignKey('accounts.Student', on_delete=models.CASCADE, related_name='documents', default=1)
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPE_CHOICES, default=4)
    #signers
    #size
    #type







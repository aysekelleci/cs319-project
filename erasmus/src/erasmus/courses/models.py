from django.db import models

# Create your models here.


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
    university = models.ForeignKey(University, on_delete=models.CASCADE, null=True )
    bilkent_equivalent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    approved = models.BooleanField(default=False)
    course_type = models.CharField(max_length=30)
    course_coordinator_name = models.CharField(blank=True, max_length=100)
    merged_course = models.ForeignKey(MergedCourse, on_delete=models.SET_NULL, blank=True, null=True)
    is_merged = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.course_codes + ": " + self.course_name)



class Document(models.Model):
    document_name = models.CharField(max_length=50)
    document = models.FileField(upload_to='documents/')
    date = models.DateTimeField(auto_now_add=True)
    # is_signed = models.BooleanField(default=False)
    # user = models.ForeignKey('accounts.Student', on_delete=models.CASCADE, related_name='student_user')

    #signers
    #size
    #type







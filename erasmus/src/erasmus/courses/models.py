from django.db import models
# Create your models here.


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_codes = models.CharField(max_length=20)
    course_credit = models.FloatField()
    #university = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE,  default=DEFAULT_CATEGORY_ID)
    #bilkent_equivalent = models.ForeignKey(Course)
    approved = models.BooleanField(default=False)
    #grade = models.CharField(max_length=20)
    courseType = models.CharField(max_length=30)
    course_coordinator_name = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return '{}'.format(self.course_codes + ": " + self.course_name)




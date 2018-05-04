from django.db import models


class Complaint(models.Model):
    c_name = models.CharField(max_length=250)
    c_id = models.CharField(max_length=250)
    date = models.CharField(max_length=250)
    directed_to = models.CharField(max_length=250)
    c_category = models.CharField(max_length=5)

    def __str__(self):
        return '%s' %(self.c_name) + '- size:' + '%s' %(self.c_id) + '%s' %(self.date) + '%s' %(self.directed_to)






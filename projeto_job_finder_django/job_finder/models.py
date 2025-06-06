from django.db import models


class Jobs(models.Model):
    title = models.TextField(blank=True, null=True)
    salary = models.TextField(blank=True, null=True)
    company = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    new_job = models.IntegerField(blank=True, null=True)
    createdat = models.TextField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.TextField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jobs'
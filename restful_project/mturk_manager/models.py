from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Account_Mturk(models.Model):
    name = models.CharField(max_length=200, qnique=True)
    key_access = models.CharField(max_length=200)
    key_secret = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Mturk Account"


class Project(models.Model):
    version = models.IntegerField()
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    account_mturk = models.ForeignKey(
        Account_Mturk,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    datetime_visited = models.DateTimeField(default=timezone.now)
    datetime_created = models.DateTimeField(auto_now_add=True)

    settings_batch = models.ForeignKey(
        'Settings_Batch',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    blocked_workers = models.ManyToManyField('Worker')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Settings_Batch(models.Model):

    name = models.CharField(max_length=200)

    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    reward = models.IntegerField(default=0)
    count_assignments = models.IntegerField(default=1)
    count_assignments_max_per_worker = models.IntegerField(
        null=True, blank=True)
    # całkowity czas na trwanie zadania jako aktywnego na rynku
    lifetime = models.IntegerField(default=604800)
    # czas na zrobienie zdania po zaakceptowaniu przez workera
    duration = models.IntegerField(default=3600)
    amount_budget_max = models.IntegerField(null=True, blank=True)
    template_worker = models.ForeignKey(
        "Template_Worker",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    keywords = models.ManyToManyField("Keyword")
    qualifications = models.ManyToManyField("Qualification")  # ważne pole!!!
    message_reject = models.ForeignKey(
        "Message_Reject", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.project} -- {self.name}"


class Batch(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    use_sandbox = models.BooleanField()
    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class HIT(models.Model):
    STATUS = (
        (1, "Reviewed"),
        (2, "NotReviewed"),
    )

    id_hit = models.CharField(max_length=200, unique=True)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_expiration = models.DateTimeField(db_index=True)
    # parameters = models.TextField() postaram się obyć bez tego pola
    status = models.IntegerField(choices=STATUS)
    count_assignments_additional = models.IntegerField(default=0)
    count_assignments_dead = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.batch.name} -- {self.id_hit}"


class Assignment(models.Model):
    STATUS = (
        (1, "Approved"),
        (2, "Pending"),
        (3, "Submitted"),
        (4, "Rejected")
    )

    id_assignment = models.CharField(max_length=200)
    hit = models.ForeignKey("HIT", on_delete=models.CASCADE)
    worker = models.ForeignKey("Worker", on_delete=models.SET_NULL, null=True)
    status = models.IntegerField(choices=STATUS)
    datetime_created = models.DateTimeField()
    datetime_submit = models.DateTimeField(null=True, blank=True)
    datetime_accept = models.DateTimeField(null=True, blank=True)
    answer = models.TextField()

    def __str__(self):
        return f"{self.id_assignment} ({self.status})"


class Message_Reject(models.Model):
    name = models.CharField(max_length=200)
    message = models.CharField(max_length=1024)

    def __str__(self):
        return self.name


class Worker(models.Model):
    class Meta:
        ordering = ["id_worker"]

    id_worker = models.CharField(max_length=200, unique=True)
    global_block = models.BooleanField(default=False)

    def __str__(self):
        return self.id_worker

class Keyword(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Qualification(models.Model):

class Template_Worker(models.Model):
    height_frame = models.IntegerField() # dodać default value
    content = models.TextField()
    json_dict_parameters = models.TextField() # pole które wyłapuje wszystkie parametry z templatki czyli szuka patternu ${variable}

    def fetch_parameters(self):
        #TODO Napisać funkcję, która wyciąga wszystkie parametry z pola content i wstawia jako klucze w json_dict_parameters
        pass


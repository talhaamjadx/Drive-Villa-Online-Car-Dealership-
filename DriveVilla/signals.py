from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from DriveVillaPrototype1.utils import generate_random_string
from DriveVilla.models import Question, Answer
from users.models import CustomUser
from DriveVilla import tasks
from os import path

@receiver(pre_save, sender= Question)
def add_slug_to_question(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug  = slugify(instance.content)
        random_string = generate_random_string()
        instance.slug = slug + "-" + random_string

@receiver(pre_save, sender= Answer)
def add_slug_to_answer(sender, instance, *args, **kwargs):
    if instance and not instance.ans_slug:
        slug  = slugify(instance.content)
        random_string = generate_random_string()
        instance.ans_slug = slug + "-" + random_string

@receiver(pre_save, sender= CustomUser)
def update_on_startup(sender, instance, *args, **kwargs):
    if instance and not path.exists("model/Model/"+instance.username+".hdf5"):
        tasks.createUser.delay('hello', instance.username)
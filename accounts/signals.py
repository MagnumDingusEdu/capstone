from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import UserAccount, Student


@receiver(post_save, sender=UserAccount)
def create_associated_student(sender, instance: UserAccount, created, **kwargs):
    if created:
        if instance.is_student():
            Student.objects.create(
                user=instance,
                student_name=instance.first_name + " " + instance.last_name,
            )

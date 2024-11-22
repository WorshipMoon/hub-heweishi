from django.db import models


# Create your models here.
class TimeStampedMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class VpnLink(TimeStampedMixin):
    link = models.URLField()
    note = models.TextField()
    code = models.CharField(max_length=50)
    status = models.SmallIntegerField(
        default=2,
        choices=[(0, "禁用"), (1, "启用")],
        help_text="状态",
    )
    expiration_time = models.DateTimeField()
    level = models.IntegerField()

    def __str__(self):
        # return f"{self.note} - {self.expiration_time}"
        return self.note

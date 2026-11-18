from django.db import models


class StateModelManager(models.Manager):
    """
        Custom Manager for Active Entries
    """

    def get_queryset(self):
        from .models import StateModel
        return super().get_queryset().filter(status=StateModel.StateChoices.ACTIVE)


class SecondStateModelManager(models.Manager):
    """
        Custom Manager for Active Entries
    """

    def get_queryset(self):
        from .models import StateModel
        return super().get_queryset().filter(status=StateModel.StateChoices.INACTIVE)

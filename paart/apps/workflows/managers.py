from django.contrib.contenttypes.models import ContentType
from django.db import models


class WorkflowInstanceManager(models.Manager):
    def get_for(self, content_object):
        content_type = ContentType.objects.get_for_model(content_object)
        return self.model.objects.filter(content_type=content_type, object_id=content_object.pk)

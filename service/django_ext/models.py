from django.db import models
from django.db.models import ManyToManyField, ForeignKey


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self, fields=None, exclude=None, return_many_to_many=False):
        opts = self._meta
        data = {}
        for f in opts.concrete_fields + opts.many_to_many:
            if fields and f.name not in fields:
                continue
            if exclude and f.name in exclude:
                continue
            if isinstance(f, ManyToManyField):
                if self.pk is None or not return_many_to_many:
                    continue
            if isinstance(f, ForeignKey):
                data[f.name + '_id'] = f.value_from_object(self)
            else:
                data[f.name] = f.value_from_object(self)
        return data

    class Meta:
        abstract = True
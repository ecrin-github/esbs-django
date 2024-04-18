from django.contrib import admin

from mdm.models.data_object.data_objects import DataObjects
from mdm.models.data_object.object_contributors import ObjectContributors
from mdm.models.data_object.object_datasets import ObjectDatasets
from mdm.models.data_object.object_dates import ObjectDates
from mdm.models.data_object.object_descriptions import ObjectDescriptions
from mdm.models.data_object.object_identifiers import ObjectIdentifiers
from mdm.models.data_object.object_instances import ObjectInstances
from mdm.models.data_object.object_relationships import ObjectRelationships
from mdm.models.data_object.object_rights import ObjectRights
from mdm.models.data_object.object_titles import ObjectTitles
from mdm.models.data_object.object_topics import ObjectTopics

from mdm.models.study.studies import Studies
from mdm.models.study.study_contributors import StudyContributors
from mdm.models.study.study_features import StudyFeatures
from mdm.models.study.study_identifiers import StudyIdentifiers
from mdm.models.study.study_relationships import StudyRelationships
from mdm.models.study.study_titles import StudyTitles
from mdm.models.study.study_topics import StudyTopics

# Register your models here.
admin.site.register(DataObjects)
admin.site.register(ObjectContributors)
admin.site.register(ObjectDatasets)
admin.site.register(ObjectDates)
admin.site.register(ObjectDescriptions)
admin.site.register(ObjectIdentifiers)
admin.site.register(ObjectInstances)
admin.site.register(ObjectRelationships)
admin.site.register(ObjectRights)
admin.site.register(ObjectTitles)
admin.site.register(ObjectTopics)

admin.site.register(Studies)
admin.site.register(StudyContributors)
admin.site.register(StudyFeatures)
admin.site.register(StudyIdentifiers)
admin.site.register(StudyRelationships)
admin.site.register(StudyTitles)
admin.site.register(StudyTopics)

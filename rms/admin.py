from django.contrib import admin

from rms.models.dtp.dtas import DataTransferAccesses
from rms.models.dtp.dtp_datasets import DtpDatasets
from rms.models.dtp.dtp_notes import DtpNotes
from rms.models.dtp.dtp_objects import DtpObjects
from rms.models.dtp.dtp_people import DtpPeople
from rms.models.dtp.dtp_prereqs import DtpPrereqs
from rms.models.dtp.dtp_studies import DtpStudies
from rms.models.dtp.dtps import DataTransferProcesses

from rms.models.dup.duas import DataUseAccesses
from rms.models.dup.dup_notes import DupNotes
from rms.models.dup.dup_objects import DupObjects
from rms.models.dup.dup_people import DupPeople
from rms.models.dup.dup_prereqs import DupPrereqs
from rms.models.dup.dup_secondary_use import DupSecondaryUse
from rms.models.dup.dup_studies import DupStudies
from rms.models.dup.dups import DataUseProcesses


# Register your models here.
admin.site.register(DataTransferAccesses)
admin.site.register(DtpDatasets)
admin.site.register(DtpNotes)
admin.site.register(DtpObjects)
admin.site.register(DtpPeople)
admin.site.register(DtpPrereqs)
admin.site.register(DtpStudies)
admin.site.register(DataTransferProcesses)

admin.site.register(DataUseAccesses)
admin.site.register(DupNotes)
admin.site.register(DupObjects)
admin.site.register(DupPeople)
admin.site.register(DupPrereqs)
admin.site.register(DupSecondaryUse)
admin.site.register(DupStudies)
admin.site.register(DataUseProcesses)

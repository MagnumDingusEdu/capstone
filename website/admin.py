from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Scholarship, ScholarshipConstraint, Constraint, Notice, NoticeCategory, ScholarshipCategory, \
    MCMApplication, Grievance


class ScholarshipConstraintInlineAdmin(admin.StackedInline):
    model = ScholarshipConstraint
    extra = 1


class ScholarshipSummernoteAdmin(SummernoteModelAdmin):
    summernote_fields = ('eligibility_criteria',)


@admin.register(Scholarship)
class ScholarshipAdmin(ScholarshipSummernoteAdmin, admin.ModelAdmin):
    inlines = [ScholarshipConstraintInlineAdmin]
    list_display = (
        'name',
        'scholarship_type',
        'category',
    )
    list_filter = ('category', 'created_at', 'updated_at', 'scholarship_type')
    raw_id_fields = ('constraints',)
    search_fields = ('name', 'constraints', 'eligibility_criteria')
    date_hierarchy = 'created_at'


@admin.register(Constraint)
class ConstraintAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'attachment',
        'date',
    )
    list_filter = ('date', 'category')


class NoticeInline(admin.StackedInline):
    model = Notice
    extra = 0


@admin.register(NoticeCategory)
class NoticeCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'collapsed'
    )
    list_filter = ('collapsed',)
    inlines = [NoticeInline]


@admin.register(ScholarshipCategory)
class ScholarshipCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(MCMApplication)
class MCMApplicationAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    summernote_fields = ('remarks',)
    list_display = (
        'student',
        'scholarship',
        'status',
        'contact_number',
        'alternate_contact_number',
        'state_of_residence',
        'class_12_marks',
        'current_cgpa_or_rank',
        'family_income_per_mcm_application',
        'family_income_per_affidavit',
        'family_income_per_certificate',
        'bank_balance',
        'fdr_balance',
        'itr_annual_year_current',
        'itr_annual_year_last',
        'itr_annual_year_last_last',
        'immovable_property',
        'single_girl_child',
        'applied_for_mcp_special',
        'mcp_special_reason',
        'applied_for_other_scholarship',
        'other_scholarship_details',
        'previous_year_scholarship',
        'previous_year_scholarship_details',
        'previous_year_scholarship_amount',
        'income_certificate',
        'supporting_documents',
    )
    list_filter = (
        'status',
        'student',
        'scholarship',
        'immovable_property',
        'single_girl_child',
        'applied_for_mcp_special',
        'applied_for_other_scholarship',
        'previous_year_scholarship',
    )

    readonly_fields = ('student', 'scholarship', 'id')
    search_fields = ('student__user__first_name', 'student__user__last_name', 'scholarship__name')


@admin.register(Grievance)
class GrievanceAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    summernote_fields = ('remarks',)
    list_display = (
        'subject',
        'date_opened',
        'resolved',
    )
    list_filter = ('date_opened', 'resolved')

    readonly_fields = ('id',)

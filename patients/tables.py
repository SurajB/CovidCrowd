import django_tables2 as tables

from .models import Report, Patient


class ReportsTable(tables.Table):
    review = tables.TemplateColumn(
        template_name="patients/_review_btn.html",
        verbose_name="Actions",
        orderable=False,
    )
    diagnosed_date = tables.DateTimeColumn(format='d/M/Y')

    class Meta:
        model = Report
        template_name = "django_tables2/bootstrap4.html"
        fields = (
            "id",
            "diagnosed_date",
            "detected_state",
            "detected_city",
            "age",
            "gender",
            "current_status",
        )
        attrs = {"class": "table table-responsive"}


class PatientsTable(tables.Table):
    detail = tables.TemplateColumn(
        template_name="patients/_show_patient_details_btn.html",
        verbose_name="Details",
        orderable=False,
    )
    diagnosed_date = tables.DateTimeColumn(format='d/M/Y')

    class Meta:
        model = Patient
        template_name = "django_tables2/bootstrap4.html"
        fields = (
            "id",
            "diagnosed_date",
            "detected_state",
            "detected_city",
            "age",
            "gender",
            "current_status",
        )
        attrs = {"class": "table table-responsive"}

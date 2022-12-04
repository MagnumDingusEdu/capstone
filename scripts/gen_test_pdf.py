# python manage.py runscript gen_test_pdf

from django.conf import settings
from django.template.loader import render_to_string
import pdfkit
from website.models import (
    Scholarship,
    NoticeCategory,
    ScholarshipCategory,
    Notice,
    MCMTietApplication,
    MCMOtherApplication,
    MCMAlumniApplication,
    Grievance,
    Constraint,
    ReceivedScholarship,
)

def run():

    try:
        m = MCMAlumniApplication.objects.get(id=3)
        # m = MCMOtherApplication.objects.get(id=3)


        css = settings.BASE_DIR / "node_modules" / "bootstrap" / "dist" / "css" / "bootstrap.css"
        template_name = "pdfs/mcm_alumni.html"
        rendered = render_to_string(template_name, {
            "application": m,
        })
        options = {
            'page-size': 'Letter',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'custom-header': [
                ('Accept-Encoding', 'gzip')
            ],
            'no-outline': None
        }
        pdfkit.from_string(rendered, settings.MEDIA_ROOT / "pdfs" / "out.pdf", css=css, options=options)


    except Exception as e:
        print(e)
        print("Not foun lol")




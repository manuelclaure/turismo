import requests
from django.conf import settings
from django.http import HttpResponse
class BaseJasperReport(object):
    report_name = ''
    filename = ''
    xgestion = '2021'



    def __init__(self):
        self.auth = (settings.JASPER_USER, settings.JASPER_PASSWORD)
        super(BaseJasperReport, self).__init__()

    def get_report(self):
        url = '{url}/jasperserver/rest_v2/reports/reports/{report_name}.pdf'.format(url=settings.JASPER_URL, report_name=self.report_name)
        req = requests.get(url, params=self.get_params(), auth=self.auth)
        return req.content

    def get_params(self):
        """
        Este metodo sera implementado por cada uno de nuestros reportes
        """
        raise NotImplementedError

    def render_to_response(self):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(self.filename)
        response.write(self.get_report())
        return response
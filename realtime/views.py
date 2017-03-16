from django.http import HttpResponse
from django.views.generic import TemplateView

from .tasks import generate_csv

class CeleryRealtimeTemplateView(TemplateView):
    template_name = 'real-time.html'

    def post(self, request, *args, **kwargs):
        task_id = generate_csv.delay()
        return HttpResponse(task_id)
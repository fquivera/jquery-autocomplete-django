from django.views.generic import View, CreateView
from django.http import HttpResponse
from django.db.models import Q
import simplejson

from .models import Person, Project
from .forms import ProjectForm

class PersonCompleteView(View):

    def get(self, request,  *args, **kwargs):
        self.q = self.request.REQUEST.get("term")
        if self.q:
            qset = (
                    Q(id_card__istartswith=self.q) |
                    Q(name__icontains=self.q) |
                    Q(last_name__icontains=self.q)
                   )
            self.person = Person.objects.filter(qset).distinct()
        else:
            self.person = []

        person_list = []

        for p in self.person:
            value = '%s, (%s, %s)' % (p.id_card, p.name, p.last_name)
            p_dict = {'id': p.id, 'label': value, 'value': value}
            person_list.append(p_dict)

        return HttpResponse(simplejson.dumps(person_list))

class ProjectAddView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project_form.html'

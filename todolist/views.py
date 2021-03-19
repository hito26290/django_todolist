from django.shortcuts import render
from todolist.models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddTask
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

@login_required

def index(request):

    if request.method == 'POST':
        task = Task()
        form = AddTask(request.POST)
        if form.is_valid():
            task.content = request.POST['new_task']
            task.user = request.user
            task.save()

        


    all_task = Task.objects.filter(user__exact=request.user)
    form = AddTask()

    context = {
        'all_task': all_task,
        'form': form,
    }

    return render(request, 'index.html', context=context)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ('content',)
    success_url = reverse_lazy('index')

    def get_queryset(self):
        base_qs = super(TaskUpdate, self).get_queryset()
        return base_qs.filter(user=self.request.user)


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('index')

    def get_queryset(self):
        base_qs = super(TaskDelete, self).get_queryset()
        return base_qs.filter(user=self.request.user)
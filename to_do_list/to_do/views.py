from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, FormView, ListView

from . import forms, models

# Create your views here.


class CreateTaskView(LoginRequiredMixin, CreateView):
    model = models.Task
    template_name = "to_do/create.html"
    login_url = reverse_lazy("to_do:login_redirect")
    redirect_url = reverse_lazy("to_do:list_view")

    form_class = forms.TaskForm

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.owner = self.request.user
        self.object.save()
        messages.success(self.request, "Task Added Successfully")
        return response

    def form_invalid(self, form):
        messages.error(
            self.request, "Unable to save task.Please check the form for errors.")

        return super().form_invalid(form)


def create_task_view(request: HttpRequest):
    """
    A function based view that saves a task. It accomplishes the same
    function as the class-based view above

    1. Check if the user is authenticated, and redirect to login page if they aren't
    2. Check the request method
        1. If the request method is POST, create a `TaskForm` instance with the dat from Psot and check validity
            1. If the form is valid, save it and add message to request and redictect to the `list_view`
            2. If form is invalid, add message to request
        2. If it is any other method, intialise a new form instance

    3. Return the rendered response with the approproaite for passed into the context


    """
    if not request.user.is_authenticated:
        return HttpResponseRedirect(redirect_to="to_do:login_redirect", )

    if request.method == "POST":
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request, "Task Added Successfully")
            return HttpResponseRedirect("to_do.list_view")
        else:
            messages.error(
                request, "Unable to save task.Please check the form for errors.")
    else:
        form = forms.TaskForm()
    return render(request, "to_do/create.html", context={"form": form})


class ListTasksView(LoginRequiredMixin, ListView):
    model = models.Task
    template_name = "to_do/list.html"
    login_url = reverse_lazy("to_do:login")

    def get_queryset(self):
        return super().get_queryset().filter(owner__id=self.request.user.id)


class DetailTaskView(LoginRequiredMixin, DetailView):
    model = models.Task
    template_name = "to_do/detail.html"


class UserCreationView(FormView):
    form_class = forms.UserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("to_do:login")

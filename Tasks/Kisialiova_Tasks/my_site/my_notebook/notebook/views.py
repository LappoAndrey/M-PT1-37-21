from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse, redirect, get_object_or_404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView
from django.contrib import messages
from .models import Note
from .forms import NoteForm


class NoteHomepageView(LoginRequiredMixin, ListView):
    template_name = 'notes/homepage.html'
    model = Note

    def get_queryset(self):
        user = self.request.user
        qs = Note.objects.filter(user=user)
        qs = Note.filters_data(self.request, qs)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_form'] = NoteForm()
        context['pinned_qs'] = self.object_list.filter(pinned=True)
        context['qs'] = self.object_list.filter(pinned=False)[:30]
        return context


@login_required
def validate_new_note_view(request):
    form = NoteForm(request.POST or None)
    if form.is_valid():
        note = form.save(commit=False)
        note.user = request.user
        note.save()
        messages.success(request, 'New message added')
    return redirect(reverse('notes:home'))


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    form_class = NoteForm
    success_url = reverse_lazy('notes:home')
    template_name = 'notes/form.html'
    model = Note

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['back_url'] = self.success_url
        context['form_title'] = f'Processing {self.object.title}'
        return context

    def form_valid(self, form):
        messages.success(self.request, f'Note has been updated!')
        return super().form_valid(form)


@login_required
def pinned_view(request, pk):
    instance = get_object_or_404(Note, id=pk)
    instance.pinned = not instance.pinned
    instance.save()
    return HttpResponseRedirect(reverse('notes:home'))


@login_required
def delete_note_view(request, pk):
    instance = get_object_or_404(Note, id=pk)
    instance.delete()
    messages.warning(request, 'Deleted')
    return redirect(reverse('notes:home'))

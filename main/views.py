import json

from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Profile, UploadedFile
from .agent.agent import PDFContext

class FileUploadView(CreateView):
    model = UploadedFile
    fields = ['file']
    template_name = 'file_upload.html'

    def form_valid(self, form):
        # Get the profile using the primary key from the URL
        profile_pk = self.kwargs['pk']
        profile = get_object_or_404(Profile, pk=profile_pk)

        # Associate the uploaded file with the profile
        form.instance.user = profile

        # Save the uploaded file
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect to the user's profile after successful file upload
        return reverse_lazy('user_profile', kwargs={'pk': self.kwargs['pk']})


class PromptView(View):
    def post(self, request, *args, **kwargs):
        profile_pk = self.kwargs['pk']
        profile = get_object_or_404(Profile, pk=profile_pk)
        files = UploadedFile.objects.filter(user=profile)
        prompt = request.POST.get('prompt_field', 'hi')
        response = PDFContext(profile).prompt(prompt=prompt)

        return render(request, 'user_profile.html', {'user': profile, 'files': files, 'answer': response})

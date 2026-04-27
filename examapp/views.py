from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ExamFormSubmissionForm


@login_required
def dashboard(request):
	return render(request, 'examapp/dashboard.html')


@login_required
def fill_exam_form(request):
	if request.method == 'POST':
		form = ExamFormSubmissionForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('submission_success')
	else:
		form = ExamFormSubmissionForm()
	return render(request, 'examapp/fill_exam_form.html', {'form': form})


@login_required
def submission_success(request):
	return render(request, 'examapp/submission_success.html')

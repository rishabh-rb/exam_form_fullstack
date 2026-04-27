from django.db import models


class ExamFormSubmission(models.Model):
	YEAR_CHOICES = [
		('1', 'First Year'),
		('2', 'Second Year'),
		('3', 'Third Year'),
		('4', 'Fourth Year'),
	]

	full_name = models.CharField(max_length=120)
	course = models.CharField(max_length=120)
	year = models.CharField(max_length=1, choices=YEAR_CHOICES)
	address = models.TextField()
	phone_number = models.CharField(max_length=15)
	submitted_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.full_name} - {self.course}"

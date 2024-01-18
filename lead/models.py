from django.db import models
from django.contrib.auth.models import User
from django.db.models import TextChoices
from phonenumber_field.modelfields import PhoneNumberField

class PriorityChoices(TextChoices):
    LOW = 'low', 'Low'
    MEDIUM = 'medium', 'Medium'
    HIGH = 'high', 'High'

class StatusChoices(TextChoices):
    NEW = 'new', 'New'
    IN_PROGRESS = 'in_progress', 'In Progress'
    COMPLETE = 'complete', 'Complete'
    LOST = 'lost', 'Lost'
    WON = 'won', 'Won'

class Lead(models.Model):
    """
    Lead model represents a potential business opportunity or lead.
    It stores information about the lead such as contact details, company, budget, and its current status and priority.
    """
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=True)
    company = models.CharField(max_length=200, blank=True, null=True, default='Unknown Company')
    description = models.TextField(blank=True, null=True, default='No description provided')
    budget = models.IntegerField(blank=True, null=True, default=0)
    website = models.URLField(blank=True, null=True, default='http://www.example.com')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leads')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    priority = models.CharField(max_length=20, choices=PriorityChoices.choices, default=PriorityChoices.LOW)
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.NEW)
    def __str__(self):
        return f'{self.name}'
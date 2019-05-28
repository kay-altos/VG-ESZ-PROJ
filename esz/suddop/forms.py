from django import forms
from django.db import models
from django.forms import ModelForm
from .models import *
from staicsitecontent.models import *
from django.db.models import Q
from django.contrib.admin.widgets import FilteredSelectMultiple
#
class FinancingTypeForm(forms.ModelForm):
    class Meta(object):
        """docstMeta."""
        model = FinancingType
        fields = '__all__'

class SuddopConstantsForm(forms.ModelForm):
    class Meta(object):
        """docstMeta."""
        model = SuddopConstants
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta(object):
        """docstMeta."""
        model = Category
        fields = '__all__'

class ContractSignForm(forms.ModelForm):
    contract_id = forms.CharField(required=True)
    class Meta(object):
        """docstMeta."""
        model = ContractSign
        fields = '__all__'
#

class ContractForm(forms.ModelForm):
    class Meta(object):
        """docstMeta."""
        model = Contract
        fields = '__all__'
#
class EducationYearForm(forms.ModelForm):
    class Meta(object):
        """docstMeta."""
        model = EducationYear
        fields = '__all__'
#
class ContractTypeForm(forms.ModelForm):
    class Meta(object):
        """docstMeta."""
        model = ContractType
        fields = '__all__'
#
class ContractStatusForm(forms.ModelForm):
    class Meta(object):
        """docstMeta."""
        model = ContractStatus
        fields = '__all__'
#
class ApplicantPassportForm(forms.ModelForm):
    class Meta(object):
        """docstMeta."""
        model = ApplicantPassport
        fields = '__all__'

class ApplicantForm(forms.ModelForm):
    class Meta(object):
        """docstMeta."""
        model = Applicant
        fields = '__all__'
        #exclude = ["ApplicantPassport"]
        widgets = {
        #'ApplicantEmail': forms.Select(attrs={'placeholder': 'Создайте контакт','readonly':'readonly'}),
        #'ApplicantPhone': forms.Select(attrs={'placeholder': 'Создайте контакт','readonly':'readonly'}),

        }
#
class ApplicantPhonesForm(forms.ModelForm):
    class Meta(object):
        """docstMeta."""
        model = ApplicantPhones
        fields = '__all__'
#
class ApplicantEmailsForm(forms.ModelForm):
    class Meta(object):
        """docstMeta."""
        model = ApplicantEmails
        fields = '__all__'
#
'''
class GenderForm(forms.ModelForm):
    class Meta(object):
        """docstMeta."""
        model = Gender
        fields = '__all__'
'''
#
class CenterForm(forms.ModelForm):
    class Meta(object):
        """docstMeta."""
        model = Center
        fields = '__all__'
#
class ProgramForm(forms.ModelForm):
    class Meta(object):
        """docstMeta."""
        model = Program
        fields = '__all__'
#
class TeacherForm(forms.ModelForm):
    class Meta(object):
        """docstMeta."""
        model = Teacher
        fields = '__all__'
#
class GroupForm(forms.ModelForm):
    class Meta(object):
        """docstMeta."""
        model = Group
        fields = '__all__'
#
'''
class StudentDocsForm(forms.ModelForm):
    class Meta(object):
        """docstMeta."""
        model = StudentDocs
        fields = '__all__'
'''
#
class StudentForm(forms.ModelForm):
    class Meta(object):
        """docstMeta."""
        model = Student
        fields = '__all__'
        widgets = {
        #'Group': forms.ModelMultipleChoiceField(widget=FilteredSelectMultiple("Group", is_stacked=False),queryset=models.Group.objects.all()),

        }
#
class EducationFormForm(forms.ModelForm):
    class Meta(object):
        """docstMeta."""
        model = EducationForm
        fields = '__all__'
#

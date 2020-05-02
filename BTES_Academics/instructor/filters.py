import django_filters
from students.models import *


class StudentFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super(StudentFilter, self).__init__(*args, **kwargs)
        self.filters['user__first_name'].label = 'First Name'
        self.filters['user__email'].label = 'Email'

    class Meta:
        model = Student
        fields = ['regId', 'user__first_name', 'user__email']


# ArticleFilter.base_filters['author'].label = 'Author Exact Lookup'
# StudentFilter.base_filters['user__first_name'].lable = 'First Name'

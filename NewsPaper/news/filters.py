import django_filters
from django import forms

from .models import Post, Category


class PostFilter(django_filters.FilterSet):

    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Название содержит',
    )

    categories = django_filters.ModelChoiceFilter(
        field_name='categories',
        queryset=Category.objects.all(),
        label='Категория',
    )

    start_date = django_filters.DateFilter(
        field_name='created_at',
        lookup_expr='gte',
        label='Дата выпуска после',
        widget=forms.DateInput(attrs={'type': 'date'}),
    )

    class Meta:
        model = Post
        fields = {}

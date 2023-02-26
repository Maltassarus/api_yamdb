from django_filters import CharFilter, FilterSet, NumberFilter


class TitleFilter(FilterSet):
    category = CharFilter(
        field_name='category__slug',
        lookup_expr='icontains'
    )
    genre = CharFilter(
        field_name='genre__slug',
        lookup_expr='icontains'
    )
    name = CharFilter(
        field_name='name',
        lookup_expr='contains'
    )
    year = NumberFilter(
        field_name='year',
        lookup_expr='exact'
    )

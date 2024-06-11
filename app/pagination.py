from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    # Note: removing pagination in settings.py changes the structure of the API response (hence why very large page_size is used here instead)
    page_size = 1000000000
    page_size_query_param = 'page_size'
    max_page_size = 1000000000

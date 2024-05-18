from rest_framework.generics import ListAPIView
from rest_framework.exceptions import ParseError
from datetime import datetime, timedelta
from .models import Article
from .serializers import ArticleSerializer


class ArticlesView(ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Article.objects.all()

        tag = self.request.query_params.get("tag")
        timestamp_start_str = self.request.query_params.get("timestamp_start")
        name_search = self.request.query_params.get("q")

        # filter by tag
        if tag:
            queryset = queryset.filter(tags__name=tag)

        # filter by time range
        if timestamp_start_str:
            try:
                # Parse timestamp_end from the query parameters
                timestamp_start = datetime.fromisoformat(timestamp_start_str)
            except ValueError:
                raise ParseError(
                    "Invalid timestamp_end format. Use ISO format: YYYY-MM-DDTHH:MM:SS")

            queryset = queryset.filter(
                created_at__lte=timestamp_start)
        else:
            # Default to the last 90 days if no timestamp_end is provided
            timestamp_end = datetime.now()
            timestamp_start = timestamp_end - timedelta(days=90)
            queryset = queryset.filter(
                created_at__range=(timestamp_start, timestamp_end))

        # filter by name
        if name_search:
            queryset = queryset.filter(
                title__icontains=name_search.lower()
            )

        return queryset

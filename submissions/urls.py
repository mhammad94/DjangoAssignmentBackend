from django.urls import path
from graphene_django.views import GraphQLView
from submissions.schema import schema

urlpatterns = [
    # Only a single URL to access GraphQL
    path("submissions", GraphQLView.as_view(graphiql=True, schema=schema)),
]
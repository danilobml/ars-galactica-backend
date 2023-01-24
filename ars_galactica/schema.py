import graphene
from graphene_django import DjangoObjectType

from ars_galactica.api.models import Paintings


class PaintingType(DjangoObjectType):
    class Meta:
        model = Paintings
        fields = ("id", "title", "price", "type", "year", "available")


class Query(graphene.ObjectType):
    all_paintings = graphene.List(PaintingType)
    painting_by_title = graphene.Field(
        PaintingType, title=graphene.String(required=True))

    def resolve_all_paintings(root, info):
        return Paintings.objects.all()

    def resolve_painting_by_title(root, info, title):
        try:
            return Paintings.objects.get(title=title)
        except Paintings.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)

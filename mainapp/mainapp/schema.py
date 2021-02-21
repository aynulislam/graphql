import graphene
from graphene_django import DjangoObjectType


from books.models import Category, Product


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "products")

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ("id", "name", "notes", "category")

class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_products(root, info):
        return Product.objects.select_related("category").all()

    def resolve_category_by_name(root,info,name):
        try:
            return Category.objects.get(name = name)
        except Category.DoesNotExist:
            return None
schema = graphene.Schema(query=Query)
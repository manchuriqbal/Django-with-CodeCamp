from django.http import Http404

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import ProductSerializer
from .models import Product


class LatestProductList(APIView):
    def get(self, requset, format = None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many = True)

        return Response(serializer.data)
    
class ProductDeatilsView(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug = category_slug).get(slug =product_slug)
        except Product.DoesNotExist:
            raise Http404
        
    def get(self, request, category_slug, product_slug, format = None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


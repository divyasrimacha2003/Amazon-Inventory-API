from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import InventoryItem
from .serializers import InventorySerializer
from rest_framework.permissions import IsAuthenticated

class InventoryList(APIView):
    permission_classes = [IsAuthenticated] # Ensures JWT Security

    def get(self, request):
        # Optimized query for high performance
        items = InventoryItem.objects.all().select_related('category')
        serializer = InventorySerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

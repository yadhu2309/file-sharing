from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

class HandleFileUpload(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = FileListSerializer(data=data)
            if serializer.is_valid():
                serializer.save()

                return Response({'data':serializer.data},status=200)
            
            return Response(serializer.errors,status=400)
        except Exception as e:
            print(e)
   

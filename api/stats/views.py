import json

from django.db.models import Avg, Min, Max
from pandas import read_excel
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RawSerializer, RawExcelSerializer, ReportSerizlier
from .models import RawModel


class RawAPIView(APIView):
    def post(self, request):
        serializer = RawSerializer(data=request.data)
        if serializer.is_valid():
            author = request.user
            serializer.save(author=author)
            return Response(
                data=serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ReportAPIView(APIView):
    def post(self, request):
        month = request.data.get('month')
        serializer = ReportSerizlier(data=request.data)
        if serializer.is_valid():
            q = RawModel.objects.filter(month=month).aggregate(
                Avg('iron_con'), Min('iron_con'), Max('iron_con'),
                Avg('silicon_con'), Min('silicon_con'), Max('silicon_con'),
                Avg('aluminum_con'), Min('aluminum_con'), Max('aluminum_con'),
                Avg('calcium_con'), Min('calcium_con'), Max('calcium_con'),
                Avg('sulfure_con'), Min('sulfure_con'), Max('sulfure_con'),
            )
            q['month'] = month
            return Response(data=q, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RawExcelAPIView(APIView):
    def post(self, request):
        serializer = RawExcelSerializer(data=request.data)
        if serializer.is_valid():
            file = serializer.validated_data['file']
            dataframe = read_excel(file).to_json(orient='index')
            data = json.loads(dataframe)['0']
            data['month'] = data['month'].encode().decode()
            raw_serializer = RawSerializer(data=data)
            if raw_serializer.is_valid():
                author = request.user
                raw_serializer.save(author=author)
                return Response(
                    raw_serializer.data, status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    raw_serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

from django.shortcuts import render
from .serializers import userSerializer,ShipmentSerializer
from .models import Users,Shipment
from .authentication import UserAuthentication
from .permissions import IsAdmin,IsConsumer,IsOwner
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

class Register(APIView):
    def post(self,request):
        ser=userSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)
    def get(self,request):
        records=Users.objects.all()
        ser=userSerializer(records,many=True)
        return Response(ser.data)
class ShipmentPost(APIView):
    permission_classes=[AllowAny]
    def get(self,request):
        records=Shipment.objects.all()
        ser=ShipmentSerializer(records,many=True)
        return Response(ser.data)
    def post(self,request):
        ser=ShipmentSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)
    
# Generating the JWT Token

class Token(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        auth=UserAuthentication()
        user,_=auth.authenticate(request)
        if user is not None:
            token=RefreshToken.for_user(user)
            return Response({"access":str(token.access_token)})
        
# Getting records by using queryparams
class Query(APIView):
    permission_classes=[AllowAny]
    def get(self,request):
        category=request.query_params.get('category','').strip()
        if  not category:
            return Response({"details":"required query paramenter"},status=status.HTTP_400_BAD_REQUEST)
        records=Shipment.objects.filter(shipmentCategory__icontains=category)
        ser=ShipmentSerializer(records,many=True)
        return Response(ser.data)
    
# Getting and updating the data
class Api1(APIView):
    permission_classes=[IsOwner,IsAuthenticated]
    def get(self,request):
        records=Shipment.objects.filter(shipmentUser=request.user)
        ser=ShipmentSerializer(records,many=True)
        return Response(ser.data)
        #return Response(str(request.user))
    def put(self,request,shipmentId):
        try:
            record=Shipment.objects.get(shipmentId=shipmentId,shipmentUser=request.user)
        except Shipment.DoesNotExist:
            return Response({"details":"No record found by this shipment id !!"},status=status.HTTP_400_BAD_REQUEST) 
        ser=ShipmentSerializer(record,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)
    def get(self,request,shipmentId):
        try:
            record=Shipment.objects.get(shipmentId=shipmentId)
        except Shipment.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        ser=ShipmentSerializer(record)
        return Response(ser.data)
    def delete(self,request,shipmentId):
        try:
            record=Shipment.objects.get(shipmentId=shipmentId,shipmentUser=request.user)
        except Shipment.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        record.delete()
        return Response(status=status.HTTP_200_OK) 


    
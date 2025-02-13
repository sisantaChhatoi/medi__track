from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import  api_view
from django.shortcuts import get_object_or_404
from patients.models import Patient
from patients.serializers import PatientSerializer


# Create your views here.
@api_view(['GET,POST'])
def patient_list(request,pk):

    if request.method == 'GET':
        patient = Patient.objects.get(pk=pk)
        patients_serializer = PatientSerializer(patient)
        Response(patients_serializer.data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
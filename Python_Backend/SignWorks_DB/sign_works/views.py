from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CustomerList, Permits
from .serializers import CustomerListSerializer, PermitsSerializer

@api_view(['GET'])
def customer_list(request): #Views to just view customers.
    customers = CustomerList.objects.all()
    serializer = CustomerListSerializer(customers, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def entrylist(request):
    customers = CustomerListSerializer(data=request.data)
    if customers.is_valid():
        print("valid")
        customers.save()
    else:
        print("Not valid")
        print(customers.errors)
        print(customers.error_messages)
    return Response(customers.data)


@api_view(['POST'])
def status(request):
    customer_serializer = CustomerListSerializer(data=request.data)
    if not customer_serializer.is_valid():
        return Response({'error': f'Invalid Customer Data: {customer_serializer.errors}'}, status=status.HTTP_400_BAD_REQUEST)

    customer_data = customer_serializer.save()
    print(f'Customer: {customer_data.job_no}')

    #date_submitted = Permits.objects.values('date_submitted')

    permits_data = {
        'job_no': customer_data.job_no,
        'date_submitted': request.data.get('date_submitted'),
        'status': request.data.get('permit_status', 'Not Submitted'),
        'date_approved': None,
    }

    permit_serializer = PermitsSerializer(data=permits_data)
    if permit_serializer.is_valid():
        permit_serializer.save()
        return Response({'message': 'Upload Successful!'}, status=status.HTTP_201_CREATED)
    else:
        print(f'Invalid Data: {permit_serializer.errors}')
        return Response({'errors': f'Invalid data: {permit_serializer.errors}'}, status=status.HTTP_400_BAD_REQUEST)








   # customers = CustomerList.objects.all()
    #data = []

    #for customer in customers:
     #   customer_data = CustomerListSerializer(customer).data
      #  customer_data['permit_status'] = PermitsSerializer(customer.permit_status.all(), many=True).data
       # data.append(customer_data)

    #return Response(data)
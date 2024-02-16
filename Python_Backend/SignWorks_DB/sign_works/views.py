from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from .models import CustomerList, Permits
from .serializers import CustomerListSerializer, PermitsSerializer

@api_view(['GET'])
def customer_list(request): #Views to just view customers.
    customers = CustomerList.objects.all()
    serializer = CustomerListSerializer(customers, many=True)
    return Response(serializer.data)



@api_view(['POST']) # Used to enter a customer to the database
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

@api_view(['GET']) # Used to retrieve job_no and customer for posting permit_status
def get_jobs(request):
    jobs = CustomerList.objects.values('job_no', 'customer')

    #Convert the queryset to a list of dictionaries
    jobs_list = [{'job_no': job['job_no'], 'customer': job['customer']} for job in jobs]
    return Response(jobs_list)



@api_view(['POST']) #used to post plan status
def permit_status(request):
    permit_data = PermitsSerializer(data=request.data, many=True)
    if permit_data.is_valid():
        print("Valid")
        permit_data.save()
    else:
        print("Not Valid")
        print(permit_data.errors)
        print(permit_data.error_messages)
    return Response(permit_data.data)


# To view the status page
@api_view(['GET'])
def status_view(request):
    status = Permits.objects.all()
    status_data = []
    for state in status:
        status_data.append({
            'job_no': state.job_no,
            'client': state.client,
            'city': state.city,
            'date_submitted': state.date_submitted,
            'status': state.status,
            'date_approved': state.date_approved,
        })
    serializer = PermitsSerializer(data=status_data, many=True)
    serializer.is_valid()
    return Response(serializer.data)


#Not being used
@api_view(['GET'])
def customer_detail(request, job_no, customer):
    try:
        clients = CustomerList.objects.filter(job_no=job_no, customer=customer)
        serializer = CustomerListSerializer(clients, many=True)

        serialized_data = serializer.data[0] if serializer.data else {}
        return Response(serialized_data)
    except CustomerList.DoesNotExist:
        return Response({'error': 'Client not found'}, status=status.HTTP_404_NOT_FOUND)


#To update customer list
@api_view(['PUT'])
def customer_update(request, job_no):
    client_data = request.data

    try:
        jobNo = CustomerList.objects.get(pk=job_no)
    except CustomerList.DoesNotExist:
        return Response({'message': 'Client not found.'}, status=status.HTTP_404_NOT_FOUND)

    required_fields = ['date', 'customer', 'contact_person', 'job_description', 'price_amount', 'permit_status',
                       'date_completed', 'invoice_no', 'payment_method']
    for field in required_fields:
        if field not in client_data:
            return Response({'message': f'{field.capitalize()} field is required.'}, status=status.HTTP_400_BAD_REQUEST)

    client_serializer = CustomerListSerializer(jobNo, data=client_data)

    if client_serializer.is_valid():
        print("Valid")
        client_serializer.save()
        return Response({'message': 'Client details updated successfully!'}, status=status.HTTP_200_OK)
    else:
        print("Not Valid")
        print(client_serializer.errors)
        print(client_serializer.error_messages)
        return Response({'message': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)


#To update plans status
@api_view(['PUT'])
def status_update(request, job_no):
    job = request.data

    try:
        jobNo = Permits.objects.get(pk=job_no)
    except Permits.DoesNotExist:
        return Response({'message': 'Job number not found'}, status=status.HTTP_404_NOT_FOUND)

    required_fields = ['job_no', 'client', 'city', 'date_submitted', 'status', 'date_approved']
    for field in required_fields:
        if field not in job:
            return Response({'message': f'{field.capitalize()} field is required'}, status=status.HTTP_400_BAD_REQUEST)

    status_serializer = PermitsSerializer(jobNo, data=job)

    if status_serializer.is_valid():
        print("Valid")
        status_serializer.save()
        return Response({'message': 'Status updated successfully.'}, status=status.HTTP_200_OK)
    else:
        print("Not Valid")
        print(status_serializer.errors)
        print(status_serializer.error_messages)
        return Response({'message': 'Invalid Request'}, status=status.HTTP_400_BAD_REQUEST)












from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from .models import CustomerList, Plans, Permits
from .serializers import CustomerListSerializer, PlansSerializer, PermitsSerializer

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
def plan_status(request):
    plan_data = PlansSerializer(data=request.data, many=True)
    if plan_data.is_valid():
        print("Valid")
        plan_data.save()
    else:
        print("Not Valid")
        print(plan_data.errors)
        print(plan_data.error_messages)
    return Response(plan_data.data)


# To view the status page
@api_view(['GET'])
def plan_status_view(request):
    status = Plans.objects.all()
    status_data = []
    for state in status:
        status_data.append({
            'job_no': state.job_no,
            'client': state.client,
            'city': state.city,
            'date_submitted': state.date_submitted,
            'planning_dept': state.planning_dept,
            'status': state.status,
            'description': state.description,
            'date_approved': state.date_approved,
        })
    serializer = PlansSerializer(data=status_data, many=True)
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
def plan_status_update(request, job_no):
    job = request.data

    try:
        jobNo = Plans.objects.get(pk=job_no)
    except Plans.DoesNotExist:
        return Response({'message': 'Job number not found'}, status=status.HTTP_404_NOT_FOUND)

    required_fields = ['job_no', 'client', 'city', 'date_submitted', 'status', 'date_approved']
    for field in required_fields:
        if field not in job:
            return Response({'message': f'{field.capitalize()} field is required'}, status=status.HTTP_400_BAD_REQUEST)

    status_serializer = PlansSerializer(jobNo, data=job)

    if status_serializer.is_valid():
        print("Valid")
        status_serializer.save()
        return Response({'message': 'Status updated successfully.'}, status=status.HTTP_200_OK)
    else:
        print("Not Valid")
        print(status_serializer.errors)
        print(status_serializer.error_messages)
        return Response({'message': 'Invalid Request'}, status=status.HTTP_400_BAD_REQUEST)


#To enter permit information
@api_view(['POST', 'GET', 'PUT'])
def permits(request, job_no=None):
    if request.method == 'POST':
        permit_data = PermitsSerializer(data=request.data, many=True)
        if permit_data.is_valid():
            print("Permit is valid")
            permit_data.save()
        else:
            print("Permit is not valid")
            print(permit_data.errors)
            print(permit_data.error_messages)
        return Response(permit_data.data)

    elif request.method == 'GET':
        if job_no is not None:
            try:
                permit_instance = Permits.objects.get(job_no=job_no)
                serializer = PermitsSerializer(permit_instance)
                return Response(serializer.data)
            except Permits.DoesNotExist:
                return Response({'message': 'Job number not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            permit_status = Permits.objects.all()
            status_data = []
            for permit in permit_status:
                status_data.append({
                    'job_no': permit.job_no,
                    'client': permit.client,
                    'date_submitted': permit.date_submitted,
                    'building_dept': permit.building_dept,
                    'status': permit.status,
                    'description': permit.description,
                    'bldg_permit_no': permit.bldg_permit_no,
                    'date_approved': permit.date_approved,
                })
            serializer = PermitsSerializer(data=status_data, many=True)
            serializer.is_valid()
            return Response(serializer.data)


    elif request.method == 'PUT':
        permit_data = request.data
        if job_no is None:
            return Response({'message': 'Job number is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            permit_instance = Permits.objects.get(job_no=job_no)
        except Permits.DoesNotExist:
            return Response({'message': 'Job number not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PermitsSerializer(permit_instance, data=permit_data)
        if serializer.is_valid():
            print("Valid Serializer")
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)














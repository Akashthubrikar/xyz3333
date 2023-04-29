from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Candidate
from .serializers import CandidateSerializer
from rest_framework import status



@api_view(['GET','POST'])
def candidate_list(request):
    if request.method=="GET":
        paginator = PageNumberPagination()  #intiating pagination
        paginator.page_size = 10
        city = request.query_params.get('city', None) #getting querries from end point
        tech_skills = request.query_params.get('tech_skills', None)

        candidates = Candidate.objects.all()
        if city:
            candidates = candidates.filter(city=city) #set queeryset to fetch city filter
        if tech_skills:
            candidates = candidates.filter(tech_skills__icontains=tech_skills) #set querryset to fetch tech_skill filter
        else:
            candidates = Candidate.objects.all()[0:50] #set querryset to fetch 50 records
        result_page = paginator.paginate_queryset(candidates, request)
        serializer = CandidateSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
        # Check if request is a POST request
    if request.method == 'POST':
        # Check if data is valid
        
        data = request.data
        if not data:
            return Response(status=status.HTTP_204_NO_CONTENT)

        # If single record, create and save
        if isinstance(data, dict):
            candidate = Candidate(**data)
            candidate.save()
            return Response(status=status.HTTP_201_CREATED)
        
        # If multiple records, create and save each one
        if isinstance(data, list):
            candidates = []
            for record in data:
                candidate = Candidate(**record)
                candidates.append(candidate)
            Candidate.objects.bulk_create(candidates)
            return Response({'success': f'{len(candidates)} candidate records created'})
    
    return Response(status=status.HTTP_400_BAD_REQUEST)
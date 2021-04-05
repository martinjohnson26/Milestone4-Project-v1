from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Programme

# Create your views here.


def all_programmes(request):
    """ Displays all programmes and allows search and sorting functions """

    programmes = Programme.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('programmes'))
            
            queries = Q(fixture__icontains=query) | Q(date__icontains=query)
            programmes = programmes.filter(queries)


    context = {
        'programmes': programmes,
        'search_term': query,
    }

    return render(request, 'programmes/programmes.html', context)


def programme_info(request, programme_id):
    """ Displays individual programme info """

    programmes = get_object_or_404(Programme, pk=programme_id)

    context = {
        'programme': Programme,
    }

    return render(request, 'programmes/programme_info.html', context)

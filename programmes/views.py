from django.shortcuts import render, get_object_or_404
from .models import Programme

# Create your views here.


def all_programmes(request):
    """ Displays all programmes and allows search and sorting functions """

    programmes = Programme.objects.all()

    context = {
        'programmes': programmes,
    }

    return render(request, 'programmes/programmes.html', context)


def programme_info(request, programme_id):
    """ Displays individual programme info """

    programmes = get_object_or_404(Programme, pk=programme_id)

    context = {
        'programme': Programme,
    }

    return render(request, 'programmes/programme_info.html', context)

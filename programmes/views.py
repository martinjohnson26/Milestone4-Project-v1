from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Programme, Category
from .forms import ProgrammeForm

# Create your views here.


def all_programmes(request):
    """ Displays all programmes and allows search and sorting functions """

    programmes = Programme.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                programmes = programmes.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            programmes = programmes.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            programmes = programmes.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('programmes'))

            queries = Q(sku__icontains=query) | Q(fixture__icontains=query)
            programmes = programmes.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'programmes': programmes,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'programmes/programmes.html', context)


def programme_info(request, programme_id):
    """ Displays individual programme info """

    programme = get_object_or_404(Programme, pk=programme_id)

    context = {
        'programme': programme,
    }

    return render(request, 'programmes/programme_info.html', context)


def add_programme(request):
    """ Add a programme to the store """
    if request.method == 'POST':
        form = ProgrammeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added programme!')
            return redirect(reverse('add_programme'))
        else:
            messages.error(request, 'Failed to add programme.Please ensure the form is valid.')

    else:
        form = ProgrammeForm()

    template = 'programmes/add_programme.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_programme(request, programme_id):
    """ Edit a programme in the store """
    programme = get_object_or_404(Programme, pk=programme_id)
    if request.method == 'POST':
        form = ProgrammeForm(request.POST, request.FILES, instance=programme)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated programme!')
            return redirect(reverse('programme_detail', args=[programme.id]))
        else:
            messages.error(request, 'Failed to update programme. Please ensure the form is valid.')
    else:
        form = ProgrammeForm(instance=programme)
        messages.info(request, f'You are editing {programme.fixture}')

    template = 'programmes/edit_programme.html'
    context = {
        'form': form,
        'programme': programme,
    }

    return render(request, template, context)

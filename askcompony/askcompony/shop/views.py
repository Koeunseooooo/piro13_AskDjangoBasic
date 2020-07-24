from venv import logger

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Item
from .models import ItemForm


def archives_year(request, year):
    return HttpResponse('{}년도에 대한 내용'.format(year))


def item_list(request):
    qs = Item.object.all()

    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(name__icontatins=q)

    logger.debug('query : {}'.format(q))

    return render(request, 'shop/item_list.html', {
        'item_list': qs,
        'q': q,
    })


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'shop/item_detail.html', {
        'item': item,
    })

#
# def item_new(request,item=None):
#     if request.method == 'POST':
#         form=ItemForm(request.POST, request.FILES)
#         if form.is_valid():
#             item=form.save()
#             return redirect(item)
#     else:
#         form=ItemForm()
#
#     return render(request, 'shop/item_form.html',{
#         'error_list' : error_list,
#         'initial':initial,
#     })

item_new = CreateView.as_view(model=Item,form_class=ItemForm)
item_edit = UpdateView.as.view(model=Item,form_class=ItemForm)
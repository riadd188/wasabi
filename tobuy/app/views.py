from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Item
from .forms import ItemForm
from django.utils import timezone

# class IndexView(View):
#     def get(self, request, *args, **kwargs):
#         item_data = Item.objects.order_by('-id')
#         return render(request, 'app/index.html', {
#             'item_data': item_data
#         })

class IndexView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        item_data = Item.objects.order_by('-id')
        # for item in item_data:
        #     print(item.place)

        # 何も必要なものがない場合，isexist_itemがtrue
        isexist_need = False
        for item in item_data:
            if item.need:
                isexist_need = True
                break

        PLACES = (
            (1, 'パントリー'),
            (2, 'キッチン・冷蔵庫'),
            (3, '洗面台下'),
            (4, 'トイレ'),
            (5, 'リビング・たんす'),
            (6, '下駄箱'),
            (7, 'その他'),
        )
        # PLACES = {
        #     1: 'キッチン下',
        #     2: '冷蔵庫横',
        #     3: '洗面台下',
        #     4: '下駄箱',
        #     5: 'その他',
        # }
        
        return render(request, 'app/index.html', {
            'item_data': item_data,
            'isexist_need': isexist_need,
            'PLACES': PLACES
        })
        

class RestockView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        item_restock = Item.objects.get(id=self.kwargs['pk'])
        item_restock.need = False
        item_restock.save()
        return redirect('index')

class AddListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        item_restock = Item.objects.get(id=self.kwargs['pk'])
        item_restock.need = True
        item_restock.save()
        return redirect('index')

class AddItemView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = ItemForm(request.POST or None)
        return render(request, 'app/post_form.html', {
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = ItemForm(request.POST or None)

        if form.is_valid():
            item_data = Item()
            item_data.registerer = request.user
            item_data.item = form.cleaned_data['item']
            item_data.memo = form.cleaned_data['memo']
            item_data.place = form.cleaned_data['place']
            item_data.created = timezone.now()
            item_data.save()
            return redirect('index')
        
        return render(request, 'app/post_form.html', {
            'form': form
        })

class DeleteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        item_data = Item.objects.get(id=self.kwargs['pk'])
        return render(request, 'app/item_delete.html', {
            'item_data': item_data
        })

    def post(self, request, *args, **kwargs):
        item_data = Item.objects.get(id=self.kwargs['pk'])
        item_data.delete()
        return redirect('index')

class EditView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        item_data = Item.objects.get(id=self.kwargs['pk'])
        form = ItemForm(
            request.POST or None,
            initial={
                'item': item_data.item,
                'place': item_data.place,
                'memo': item_data.memo
            }
        )

        return render(request, 'app/post_form.html', {
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = ItemForm(request.POST or None)

        if form.is_valid():
            item_data = Item.objects.get(id=self.kwargs['pk'])
            item_data.item = form.cleaned_data['item']
            item_data.place = form.cleaned_data['place']
            item_data.memo = form.cleaned_data['memo']
            item_data.created = timezone.now()
            item_data.save()
            return redirect('index')
        
        return render(request, 'app/post_form.html', {
            'form': form
        })

# Create your views here.

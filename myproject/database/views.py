from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import PageForm
from .models import Database
from datetime import datetime
from zoneinfo import ZoneInfo
from django.shortcuts import render



class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        datetime_now = datetime.now(
            ZoneInfo("Asia/Tokyo")
        ).strftime("%Y年%m月%d日 %H:%M:%S")
        return render(
            request, "database/index.html", {"datetime_now": datetime_now})


class PageCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = PageForm()
        return render(request, "database/page_form.html", {"form": form})
    
    def post(self, request):
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("database:index")
        return render(request, "database/page_form.html", {"form": form})
    

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render
from .models import Database

class PageListView(LoginRequiredMixin, View):
    def get(self, request):
        # クエリパラメータ取得（デフォルト：最終更新降順）
        sort = request.GET.get("sort", "updated_at")
        order = request.GET.get("order", "desc")

        # 並び替えの適用
        if order == "asc":
            page_list = Database.objects.all().order_by(sort)
        else:
            page_list = Database.objects.all().order_by(f"-{sort}")

        # ソート可能な列の定義
        columns = {
            "updated_at": "最終更新",
            "name": "名前",
            "toughness": "タフネス",
            "power": "パワー",
            "muscle_mass": "筋肉量",
            "intelligence": "賢さ",
            "resistance": "耐性",
            "speed": "スピード",
        }

        return render(
            request,
            "database/page_list.html",
            {
                "page_list": page_list,
                "sort": sort,
                "order": order,
                "columns": columns,
            },
        )

    

class PageDetailView(LoginRequiredMixin, View):
    def get(self, request, id):
        page = get_object_or_404(Database, id=id)
        return render(request, "database/page_detail.html", {"page": page})
    

class PageUpdateView(LoginRequiredMixin, View):
    def get(self, request, id):
        page = get_object_or_404(Database, id=id)
        form = PageForm(instance=page)
        return render(request, "database/page_update.html", {"form": form})
    
    def post(self, request, id):
        page = get_object_or_404(Database, id=id)
        form = PageForm(request.POST, request.FILES, instance=page)
        if form.is_valid():
            form.save()
            return redirect("database:page_detail", id=id)
        return render(request, "database/page_update.html", {"form": form})
    

class PageDeleteView(LoginRequiredMixin, View):
    def get(self, request, id):
        page = get_object_or_404(Database, id=id)
        return render(request, "database/page_confirm_delete.html", {"page": page})
    
    def post(self, request, id):
        page = get_object_or_404(Database, id=id)
        page.delete()
        return redirect('database:page_list')


index = IndexView.as_view()
page_create = PageCreateView.as_view()
page_list = PageListView.as_view()
page_detail = PageDetailView.as_view()
page_update = PageUpdateView.as_view()
page_delete = PageDeleteView.as_view()
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Food, FoodType
from .forms import FoodForm, FoodTypeForm

# Asosiy sahifa
@login_required
def home(request):
    return render(request, 'index.html')

# Barcha taomlar ro'yxatini ko'rsatish (faqat tizimga kirgan foydalanuvchilar uchun)
@login_required
def food_list(request):
    foods = Food.objects.all()
    return render(request, 'food_list.html', {'foods': foods})

# Taomning batafsil sahifasi (hamma foydalanuvchilar ko'rishi mumkin)
@login_required
def food_detail(request, pk):
    food = get_object_or_404(Food, pk=pk)
    food.increment_view_count()
    return render(request, 'food_detail.html', {'food': food})

# Yangi taom qo'shish funksiyasi (faqat ruxsat berilgan foydalanuvchilar uchun)
@login_required
@permission_required('app.add_food', raise_exception=True)
def add_food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food_list')
    else:
        form = FoodForm()
    return render(request, 'add_food.html', {'form': form})

# Yangi FoodType qo'shish funksiyasi (faqat ruxsat berilgan foydalanuvchilar uchun)
@login_required
@permission_required('app.add_foodtype', raise_exception=True)
def add_food_type(request):
    if request.method == 'POST':
        form = FoodTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food_list')
    else:
        form = FoodTypeForm()
    return render(request, 'add_food_type.html', {'form': form})

# Taomni tahrirlash funksiyasi (faqat ruxsat berilgan foydalanuvchilar uchun)
@login_required
@permission_required('app.change_food', raise_exception=True)
def edit_food(request, pk):
    food = get_object_or_404(Food, pk=pk)
    if request.method == 'POST':
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return redirect('food_list')
    else:
        form = FoodForm(instance=food)
    return render(request, 'edit_food.html', {'form': form})

# Taomni o'chirish funksiyasi (faqat ruxsat berilgan foydalanuvchilar uchun)
@login_required
@permission_required('app.delete_food', raise_exception=True)
def delete_food(request, pk):
    food = get_object_or_404(Food, pk=pk)
    food.delete()
    return redirect('food_list')

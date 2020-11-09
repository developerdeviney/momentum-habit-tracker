from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from django.contrib.auth.decorators import login_required
from .models import Habit, Daily_Record
from .forms import HabitForm, RecordForm, SearchForm

# Create your views here.

# list objects
def habit_list(request):
    habits = Habit.objects.all()
    return render(request, "habit_list.html", {"habits": habits})


# show one model
def habit_detail(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    return render(request, "habit_detail.html", {"habit": habit})


# create a model
@login_required
def create_habit(request):
    if request.method == "GET":
        form = HabitForm()
    else:
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect(to="habit_detail", pk=habit.pk)

    return render(request, create_habit.html, {"form": form})


# update a model
@login_required
def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == "GET":
        form = HabitForm(instance=habit)
    else:
        form = HabitForm(instance=habit, data=request.POST)
        if form.is_valid():
            habit = form.save()
            return redirect(to="habit_detail", pk=habit.pk)
    return render(request, "habit_detail.html", {"habit": habit, "form": form})


# delete a model
@login_required
def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    habit.delete()
    return redirect(to="habit_list")

    return render(request, "delete_habit.html", {"habit": habit})


def create_record(request, pk):
    if request.method == "GET":
        form = RecordForm()
    else:
        form = RecordForm(data=request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user
            record.save()
            return redirect(to="habit_detail", pk=Daily_Record.pk)

    return render(request, "create_record.html", {"form": form})


@login_required
def delete_daily_record(request, pk):
    daily_record = get_object_or_404(
        Daily_Record.objects.filter(user_habit=request.user, pk=pk)
    )
    if request.method == POST:
        record.delete()
        return redirect("habit_list")

    return render(request, "delete_record.html", {"daily_record": daily_record})


def habit_search(request):
    if request.method == "GET":
        form = SearchForm()

    elif request.method == "POST":
        form = SearchForm(data=request.POST)

    if form.is_valid():
        name = form.cleaned_data["name"]
        name = Habit.objects.filter(name__contains=name)

        return render(request, "search_results.html", {"name": name})

    return render(request, "habit_search.html", {"form": form})
from django.shortcuts import render, redirect, get_object_or_404
from .models import stud_list
from .forms import StudentForm

def group_list(request):
    groups = stud_list.objects.values_list('group', flat=True).distinct()
    return render(request, 'students/index.html', {'groups': groups})

def group_detail(request, group_name):
    students = stud_list.objects.filter(group=group_name)
    return render(request, 'students/group_detail.html', {
        'group': group_name,
        'students': students
    })

# Додавання студента
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/students/')
    else:
        form = StudentForm()
    return render(request, 'students/add.html', {'form': form, 'edit': False})

# Видалення студента
def delete_student(request, student_id):
    student = get_object_or_404(stud_list, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('/students/')
    return render(request, 'students/del.html', {'student': student})

# Редагування оцінки студента
def revise_student(request, student_id):
    student = get_object_or_404(stud_list, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/students/')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/add.html', {'form': form, 'edit': True})

# Фінансовий звіт
def finance_report(request):
    groups = {}
    for student in stud_list.objects.all():
        groups.setdefault(student.group, []).append(student)

    report = []
    total = 0
    for group, students in groups.items():
        group_total = sum(s.scholarship for s in students)
        total += group_total
        report.append((group, students, group_total))

    return render(request, 'students/finance.html', {'report': report, 'total': total})
from django.shortcuts import render, redirect

from .forms import UniversityForm, StudentForm
from .models import UniversityModel, StudentModel


def menu(request):
    return render(request, "menu.html")


def university_home(request):
    universities = UniversityModel.objects.all()
    return render(request, 'myapp/university_home.html', {'universities': universities})


# def create_university(request):
#     form = UniversityForm()
#     return render(request, 'myapp/create_university.html', {'form': form})
def create_university(request):
    if request.method == 'POST':
        form = UniversityForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            short_name = form.cleaned_data['abbreviated']
            date_creation = form.cleaned_data['date_creation']

            try:
                university = UniversityModel(full_name=name, abbreviated=short_name, data_creation=date_creation)
                university.save()
            except Exception as e:
                print(e)
                # return render(request, 'model_not_created.html')

            # return render(request, 'model_created.html')
    # else:
    form = UniversityForm()

    return render(request, 'myapp/create_university.html', {'form': form})


def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            date_of_birth = form.cleaned_data['date_of_birth']
            university = form.cleaned_data['university']
            year_admission = form.cleaned_data['year_admission']

            try:
                student = StudentModel(full_name=full_name, date_of_birth=date_of_birth, university=university,
                                       year_admission=year_admission)
                student.save()
            except Exception as e:
                print(e)
                # return render(request, 'model_not_created.html')

            # return render(request, 'model_created.html')
    # else:
    form = StudentForm()

    return render(request, 'myapp/create_student.html', {'form': form})


def universities(request):
    universities = UniversityModel.objects.all()
    return render(request, 'universities.html', {'universities': universities})


def remove_university(request, university_id):
    university = UniversityModel.objects.get(id=university_id)
    university.delete()
    return redirect('universities')


def update_university(request, university_id):
    university = UniversityModel.objects.get(id=university_id)

    if request.method == 'POST':
        university.name = request.POST['name']
        university.abbreviated = request.POST['abbreviated']
        university.data_creation = request.POST['date_creation']
        university.save()
        return redirect('universities')

    university_form = UniversityForm(
        initial={
            'name': university.name,
            'abbreviated': university.abbreviated,
            'date_creation': university.data_creation,
        })

    return render(request, 'update_university.html', {'university': university_form, 'id': university.id})


def students(request):
    students = StudentModel.objects.all()
    return render(request, 'students.html', {'students': students})


def remove_student(request, student_id):
    student = StudentModel.objects.get(id=student_id)
    student.delete()
    return redirect('students')


def update_student(request, student_id):
    student = StudentModel.objects.get(id=student_id)

    if request.method == 'POST':
        student.full_name = request.POST['full_name']
        student.date_of_birth = request.POST['date_of_birth']
        print(request.POST['university'])
        student.university = UniversityModel.objects.get(abbreviated=request.POST['university'])
        student.year_admission = request.POST['year_admission']
        student.save()
        return redirect('students')

    student_form = StudentForm(
        initial={
            'full_name': student.full_name,
            'date_of_birth': student.date_of_birth,
            'university': student.university,
            'year_admission': student.year_admission,
        })

    return render(request, 'update_student.html', {'student': student_form, 'id': student.id})

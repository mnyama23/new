from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_view(request):

    if request.method == "POST":

        studentName = request.POST.get("studentName")
        studentId = request.POST.get("studentId")
        dob = request.POST.get("dob")


      
        print(studentName)
        print(studentId)
        print(dob)


        return redirect('next')
    return render(request, "login.html")

@csrf_exempt
def next(request):

    if request.method == "POST":
        personalCode = request.POST.get("personalCode")

        print(personalCode)

        return redirect("https://google.com")
    return render(request, "next.html")

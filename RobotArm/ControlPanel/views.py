from django.shortcuts import render, redirect
from .models import Pose
from .forms import PoseForm
from .models import Run

def run_values_view(request):
    latest_run = Run.objects.last()
    context = {
        'run': latest_run
    }
    return render(request, 'ControlPanel/Run.html', context)

def control_panel(request):
    poses = Pose.objects.all()

    action = request.POST.get("action")
    
    if request.method == 'POST':
        if action == "save":
            form = PoseForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("control_panel")

        elif action == "run":
            form = PoseForm(request.POST)
            if form.is_valid():
                Run.objects.create(
                motor1=form.cleaned_data['motor1'],
                motor2=form.cleaned_data['motor2'],
                motor3=form.cleaned_data['motor3'],
                motor4=form.cleaned_data['motor4'],
                motor5=form.cleaned_data['motor5'],
                motor6=form.cleaned_data['motor6'],
                status=1
)
                return redirect("run_display")

        elif action == "reset":
            form = PoseForm(initial={f'servo{i}': 90 for i in range(1, 7)})

        elif action == "load":
            pose_id = request.POST.get("load_id")
            pose = Pose.objects.get(id=pose_id)
            form = PoseForm(initial={
            'motor1': pose.motor1,
            'motor2': pose.motor2,
            'motor3': pose.motor3,
            'motor4': pose.motor4,
            'motor5': pose.motor5,
            'motor6': pose.motor6,
})

        elif action == "remove":
            pose_id = request.POST.get("remove_id")
            Pose.objects.filter(id=pose_id).delete()
            return redirect("control_panel")

    else:
        # الطلب GET عادي، أول ما تفتح الصفحة
        form = PoseForm(initial={f'servo{i}': 90 for i in range(1, 7)})

    return render(request, "ControlPanel/ControlPage.html", {"form": form, "poses": poses})
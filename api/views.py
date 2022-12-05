from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from .models import User
from .models import Job

# API config.


@require_http_methods(["GET"])
def get_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return JsonResponse({"id": user.id, "name": user.name, "email": user.email})


@require_http_methods(["PUT"])
def update_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    data = json.loads(request.body)
    user.name = data["name"]
    user.email = data["email"]
    user.save()
    return JsonResponse({"id": user.id, "name": user.name, "email": user.email})

    @require_http_methods(["GET"])
    def get_job(request, job_id):
        job = get_object_or_404(Job, pk=job_id)
    return JsonResponse({"id": job.id, "title": job.title, "company": job.company})

    @require_http_methods(["POST"])
    def create_job(request):
        data = json.loads(request.body)
    job = Job.objects.create(
        title=data["title"],
        company=data["company"]
    )
    return JsonResponse({"id": job.id, "title": job.title, "company": job.company})

    @require_http_methods(["PUT"])
    def update_job(request, job_id):
        job = get_object_or_404(Job, pk=job_id)
    data = json.loads(request.body)
    job.title = data["title"]
    job.company = data["company"]
    job.save()
    return JsonResponse({"id": job.id, "title": job.title, "company": job.company})

    @require_http_methods(["DELETE"])
    def delete_job(request, job_id):
        job = get_object_or_404(Job, pk=job_id)
    job.delete()
    return JsonResponse({"message": "Job deleted."})

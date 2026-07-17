from django.urls import path


from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("students/", views.student, name="students"),
    path("students/details/<int:id>", views.details, name="details"),
    path("upload/", views.upload),
    path(
        "api_students/",
        views.StudentModelViewset.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "api_students/<int:pk>/",
        views.StudentModelViewset.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
]

from django.urls import path
from .views import all_notes, create_notes, delete_notes, update_notes

urlpatterns = [
    path("", all_notes, name="notes_list"),
    path("create/", create_notes, name="create_note"),
    path("update/<int:pk>/", update_notes, name="update_notes"),
    path("delete/<int:pk>/", delete_notes, name='delete_notes'),
]

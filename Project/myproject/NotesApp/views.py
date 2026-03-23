from django.shortcuts import render, redirect, get_object_or_404
from .models import Notes
from .forms import NotesForm

# All Notes_____!

def all_notes(request):
    query = request.GET.get('q')
    if query:
        notes = Notes.objects.filter(title__icontains=query)
    else:
        notes = Notes.objects.all()
    return render(request, "NotesApp/notes_list.html", {"notes":notes, "query":query})

# create Notes______!

def create_notes(request):
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes_list')
        return render(request, "NotesApp/note_create.html", {"form":form})
    else:
        form = NotesForm()
        return render(request, "NotesApp/note_create.html" ,{"form":form})


# Update Notes_____!

def update_notes(request, pk):
     notes = get_object_or_404(Notes,pk=pk)
     if request.method == "POST":
          notes = NotesForm(request.POST)
          if notes.is_valid():
               notes.save()
               return redirect("notes_list")
          return render(request, "NotesApp/note_create.html", {"notes":notes})
     else:
          note = NotesForm()
          return render(request, "NoteApp/note_create.html", {"note":note})
     


# Delete Note______!
def delete_notes(request, pk):
    notes = get_object_or_404(Notes, pk=pk)
    if request.method == "POST":
         notes.delete()
         return redirect('notes_list')
    return render(request, "NotesApp/note_delete.html")
from gc import get_objects
from django.shortcuts import render, get_object_or_404, redirect
from .forms import EntryForm
# TODO: SOAL No.6 Anda harus mengimport fungsi decorator login_required
from django.contrib.auth.decorators import login_required

from .models import Blog, Author, Entry

def index(request):
    blogs = Blog.objects.all()
    data = {
        'blogs': blogs,
    }
    return render(request, 'blogs/index.html', data)


def blog_entries(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogs/blog_entries.html', {'blog': blog})
    """
    Function-based view untuk menampilkan daftar entry suatu blog.
    View ini menggunakan template 'blogs/blog_entries.html'
    """
    # TODO: SOAL No.3 Implementasikan fungsi ini dan gunakan template 'blogs/blog_entries.html'
    pass


def entry_detail(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    return render(request, 'blogs/entry_detail.html', {'entry': entry})
    """
    Function-based view untuk menampilkan detail suatu entry.
    View ini menggunakan template 'blogs/entry_detail.html'
    """
    # TODO: SOAL No.4 Implementasikan fungsi ini dan gunakan template 'blogs/author_entries.html'
    pass


def author_entries(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'blogs/author_entries.html', {'author': author})
    """
    Function-based view untuk menampilkan semua entries (tulisan) dari author.
    View ini menggunakan template 'blogs/author_entries.html'
    """
    # TODO: SOAL No.5 Implementasikan fungsi ini dan gunakan template 'blogs/author_entries.html'
    pass

# TODO: SOAL No.6 Pastikan user harus login terlebih dahulu sebelum bisa menambahkan entry.
# Bisa dilakukan dengan menambahkan decorator login_required
# atau dengan mengecek isi request.user
@login_required('', login_url='/login')
def add_entry(request, blog_id):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.blog = get_object_or_404(Blog, pk=blog_id)
            entry.save()
            form.save_m2m()
            return redirect('blogs:blog_entries', blog_id=blog_id)
    else:
        form = EntryForm()
        blog = get_object_or_404(Blog, pk=blog_id)
        data = {
            'form': form,
            'blog': blog,
        }
        return render(request, 'blogs/add_entry.html', data)

    return render(request, 'blogs/add_entry.html', data)

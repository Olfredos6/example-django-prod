from django.shortcuts import render
from website.models import Book


def index(request):
    books = Book.objects.all().order_by("-date_published")[:9]
    return render(
        request,
        "website/index.html",
        {
            "books_data": [
                ["Dernières parutions", books[:4]],
                ["Meilleures ventes", books[5:9]],
            ]
        },
    )


def catalog(request):
    books = Book.objects.all()[:15]
    # books = Book.objects.all().order_by("rating", "-date_published")[:20]
    return render(request, "website/catalog.html", {"books": books})


def search(request):
    book_matches = []
    # keyword = request.GET.get("keyword", None)
    # book_matches = Book.objects.filter(title__icontains=keyword)
    return render(request, "website/catalog.html", {"books": book_matches})

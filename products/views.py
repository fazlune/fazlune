from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, CreateView

from products.models import Product, ProductReview, Category
from .forms import ReviewForm


# Create your views here.
# Create your views here.
def home_page(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    selected_category_id = request.GET.get('category')
    search_query = request.GET.get('qidiruv', '')
    if search_query:
        products = products.filter(name__icontains=search_query)
    elif selected_category_id:
        products = Product.objects.filter(category_id=selected_category_id)
    else:
        products = Product.objects.all()
    context = {'products': products, 'categories': categories}

    return render(request, 'index.html', context)


def detail_page(request, slug):
    if request.method == "POST":
        product = get_object_or_404(Product, slug=slug)
        review = request.POST.get('review')
        user = request.user
        ProductReview.objects.create(user=user, product=product, review=review)

    product = get_object_or_404(Product, slug=slug)
    product_reviews = ProductReview.objects.all().order_by('-created_at').filter(product=product)
    context = {'product': product, 'product_reviews': product_reviews}
    return render(request, 'detail_page.html', context)


def delete_reviews(request, slug, id):
    review = ProductReview.objects.get(id=id)
    review.delete()
    return redirect('products:detail', slug=slug)


def edit_reviews(request, id, slug):
    if request.method == "POST":
        review = ProductReview.objects.get(id=id)
        edit_form = ReviewForm(instance=review, data=request.POST, files=request.FILES)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('products:detail', slug=slug)

    else:
        review = ProductReview.objects.get(id=id)
        edit_form = ReviewForm(instance=review)
    return render(request, 'edit_review.html', {'review': review, 'edit_form': edit_form})


class CreateProduct(CreateView):
    model = Product
    template_name = 'create.html'
    fields = ('name', 'description', 'price', 'product_image', 'category')


def author_page(request):
    return render(request, 'Author.html')

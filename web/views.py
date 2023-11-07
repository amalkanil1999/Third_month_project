from django.shortcuts import render , reverse
from django.http.response import HttpResponseRedirect


from web.forms import ProductForm , ImagesForm
from web.models import Product, Images , Tags


def index(request):
    products = Product.objects.filter(is_deleted=False)
    tags = Tags.objects.filter(title__isnull=False, title__gt='').distinct()[:10]

    q = request.GET.get('q')
    if q:
        products = products.filter(title__icontains=q)
       
    categories_set = []
    for product in products:
        if product.category not in categories_set:
            categories_set.append(product.category)

    search_category = request.GET.getlist("category")
    if search_category:
        products = products.filter(category__in=search_category)


    search_tags = request.GET.getlist("clothes")
    if search_tags:
        products=products.filter(tags__in=search_tags).distinct()

    sort = request.GET.get("sort")
    if sort:
        if sort == "date-asc":
            products = products.order_by("published_date")
        elif sort == "date-desc":
            products = products.order_by("-published_date")

    context={ 
        "title": "CLOTHING" ,
        "products": products,
        "categories_set": categories_set,
        "tags": tags,
    }
    return render(request, 'index.html',context=context)


def detailed(request,uuid):
    product = Product.objects.get(id=uuid)
    context={
        "title": "CLOTHING | detailed",
        "product": product,
    }
    return render(request,'detailed.html',context=context)


def create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        files = request.FILES.getlist("images")
        if form.is_valid():
            section = form.cleaned_data['section']
            instance = form.save(commit=False)
            instance.save()
            section_list = section.split(",")
            for section in section_list:
                category, created = Tags.objects.get_or_create(title=section.strip())
                instance.tags.add(category)
            for i in files:
                Images.objects.create(product=instance, images=i)
            return HttpResponseRedirect(reverse("web:index"))
    else:
        form = ProductForm()
        imagesform = ImagesForm()
    context={
        "title": "CREATE |",
        "form": form,
        "imagesform": imagesform, 
    }
    return render(request,'create.html',context=context)
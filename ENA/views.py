from django.shortcuts import render

def show_ena(request):
    context={
        'title': 'ENA',
        'name': 'ena',
        'img_src': 'https://i.ytimg.com/vi/L2R9pmu0llk/maxresdefault.jpg',
    }
    return render(request, "ENA/등장인물.html", context=context)
    #return render(request, "ENA/ena.html")

def show_moony(request):
    context = {
        'title': 'ENA',
        'name': 'moony',
        'img_src': 'https://www.fangamer.com/cdn/shop/files/product_ena_moony_plush_main.png?crop=center&height=1200&v=1692229021&width=1800',
    }
    return render(request, "ENA/등장인물.html", context=context)
    #return render(request, "ENA/moony.html")

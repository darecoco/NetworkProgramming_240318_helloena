from django.shortcuts import render

group = {
    'Characters': [
        {
            'title': 'ENA',
            'name': 'ena',
            'img_src':'ENA/images/May I help you sir.gif',
            # 'img_src': 'https://i.ytimg.com/vi/L2R9pmu0llk/maxresdefault.jpg',
        },
        {
            'title': 'ENA',
            'name': 'moony',
            'img_src':'ENA/images/moony.webp',
            # 'img_src': 'https://www.fangamer.com/cdn/shop/files/product_ena_moony_plush_main.png?crop=center&height=1200&v=1692229021&width=1800',
        },
        {
            'title': 'ENA',
            'name': 'merci',
            'img_src':'ENA/images/merci.png',
            # 'img_src': 'https://i.namu.wiki/i/TFEojh7xN347UTnIdHqCcVrjBkguvlvO0FeIU7lu3F1xchewM8DrZT584UDCKjp5maWs67ZYe0Awf9CQFe8_JA.webp',
        }
    ]
}


def show_ena(request):
    context = list(filter(lambda character: 'ena' in character['name'], group['Characters']))[0]
    # context = group['Characters'][0]
    return render(request, "ENA/등장인물.html", context=context)
    # return render(request, "ENA/ena.html")


def show_moony(request):
    context = list(filter(lambda character: 'moony' in character['name'], group['Characters']))[0]
    # context = group['Characters'][1]
    return render(request, "ENA/등장인물.html", context=context)
    # return render(request, "ENA/moony.html")


def show_character(request, 등장인물):
    context = list(filter(lambda character: 등장인물 in character['name'], group['Characters']))[0]
    return render(request, "ENA/등장인물.html", context=context)

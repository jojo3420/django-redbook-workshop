from django.shortcuts import render


def index(request):
    return render(request, 'template_app/index.html')

def base(request):
    return render(request, 'template_app/base.html')


def main(request):
    context = {
        "hobbies": ["music", "walking", 'games', 'dance']
    }
    return render(request, 'template_app/main.html', context)

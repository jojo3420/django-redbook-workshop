from django.shortcuts import render


def base(request):
    return render(request, 'template_app/base.html')


def main(request):
    context = {
        "hobbies": ["music", "walking", 'games', 'dance']
    }
    return render(request, 'template_app/main.html', context)

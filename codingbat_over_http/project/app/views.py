from django.http import JsonResponse
from django.views.decorators.http import require_GET


@require_GET
def near_hundred(request, n):
    result = abs(n - 100) <= 10 or abs(n - 200) <= 10
    return JsonResponse({"result": result})


@require_GET
def string_splosion(request, s):
    result = "".join(s[: i + 1] for i in range(len(s)))
    return JsonResponse({"result": result})


@require_GET
def cat_dog(request, s):
    cat_count = s.count("cat")
    dog_count = s.count("dog")
    result = cat_count == dog_count
    return JsonResponse({"result": result})


@require_GET
def lone_sum(request, a, b, c):
    result = a + b + c if a != b and b != c and a != c else 0
    return JsonResponse({"result": result})

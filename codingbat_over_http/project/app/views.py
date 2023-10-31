from django.http import HttpRequest, HttpResponse
from django.views.decorators.http import require_GET
import json


@require_GET
def near_hundred(request: HttpRequest, n: int) -> HttpResponse:
    result = abs(n - 100) <= 10 or abs(n - 200) <= 10
    return HttpResponse(json.dumps({"result": result}), content_type="application/json")


@require_GET
def string_splosion(request: HttpRequest, s: str) -> HttpResponse:
    result = "".join(s[: i + 1] for i in range(len(s)))
    return HttpResponse(json.dumps({"result": result}), content_type="application/json")


@require_GET
def cat_dog(request: HttpRequest, s: str) -> HttpResponse:
    cat_count = s.count("cat")
    dog_count = s.count("dog")
    result = cat_count == dog_count
    return HttpResponse(json.dumps({"result": result}), content_type="application/json")


@require_GET
def lone_sum(request: HttpRequest, a: int, b: int, c: int) -> HttpResponse:
    if a != b and b != c and a != c:
        result = a + b + c
    else:
        result = 0 if a == b == c else a if b == c else b if a == c else c
    return HttpResponse(json.dumps({"result": result}), content_type="application/json")

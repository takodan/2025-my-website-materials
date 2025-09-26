from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

# # Views functions
# def january(request):
#     return HttpResponse("H")

monthly_challenge = {
    "january": "Happy once",
    "february": "Happy twice",
    "march": "Happy three time",
    "april": None,
    "may": None,
    "june": None,
    "july": None,
    "august": None,
    "september": None,
    "october": None,
    "november": None,
    "december": None,
}

def challenges_index(request):
    response = "Challenges"
    months = list(monthly_challenge.keys())

    return render(request, "challenges\index.html", {
        "months": months
    })



def challenge_of_the_month(request, month):
    try:
        challenge = monthly_challenge[month]
        # Response template string
        # response = render_to_string("challenges/challenge.html")
        # return HttpResponse(challenge)

        # Response template string with render
        return render(request, "challenges\challenge.html", {
            "month_text": month.capitalize(),
            "challenge_text": challenge,
        })
    except:
        return HttpResponseNotFound("<h1>error: a year only have six months</h1>")


# Path Converters template
# Redirects
def challenge_of_the_int(request, month):
    months = list(monthly_challenge.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>error: a year only have six months</h1>")

    redirect_month = months[month - 1]

    # Named URLs
    redirect_path = reverse("challenge_of_the_month_url", args=[redirect_month])

    # return HttpResponseRedirect("/challenges/" + redirect_month)
    return HttpResponseRedirect(redirect_path)

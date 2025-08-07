from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

# # Views functions
# def january(request):
#     return HttpResponse("H")

monthly_challenge = {
    "january": "Happy once",
    "february": "Happy twice",
    "march": "Happy three time",
}

def challenges_index(request):
    response = "Challenges"
    months = list(monthly_challenge.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse(challenge_of_the_month, args=[month])
        response += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    return HttpResponse("<h1>" + response + "</h1>")


# Dynamic Path Segments
def challenge_of_the_month(request, month):
    try:
        challenge = monthly_challenge[month]
        return HttpResponse(challenge)
    except:
        return HttpResponseNotFound("<h1>error: a year only have three months</h1>")


# Path Converters template
# Redirects
def challenge_of_the_int(request, month):
    months = list(monthly_challenge.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>error: a year only have three months</h1>")

    redirect_month = months[month - 1]

    # Named URLs
    redirect_path = reverse(challenge_of_the_month, args=[redirect_month])

    # return HttpResponseRedirect("/challenges/" + redirect_month)
    return HttpResponseRedirect(redirect_path)

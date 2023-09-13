from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    'january':'Dzialczy!',
    'february':'''
                        1. Balloon Bonanza (Month 1)\n\n

    Objective: Master 30 new balloon animal shapes.
    Challenge: By the end of the month, perform a show where the audience shouts out animals and you create them on the spot.
                        ''',
    'march': None,
}

# def index(request):
#     return HttpResponse('Dzialczy!')

# def february(request):
#     return HttpResponse('''
#                         1. Balloon Bonanza (Month 1)\n\n

#     Objective: Master 30 new balloon animal shapes.
#     Challenge: By the end of the month, perform a show where the audience shouts out animals and you create them on the spot.
#                         ''')

def monthly_challenge_by_number(request, month: int):
    # months = monthly_challenges.keys()
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound('Invalid month')

    redirect_month = months[month - 1]
    # return HttpResponseRedirect('/challenges/' + redirect_month)
    redirect_path = reverse('month-challenge', args=[redirect_month])
    
    return HttpResponseRedirect(redirect_path)

# def monthly_challenge(request, month):
#     try:
#         challenge_text = monthly_challenges[month]

#         response_data = f'<h1>{challenge_text}</h1>'

#         return HttpResponse(response_data)
#     except:
#         return HttpResponseNotFound('Wykrzaczylo sie')

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        # response_data = render_to_string('challenges/challenge.html')
        # return HttpResponse(response_data)
        return render(request, 'challenges/challenge.html', {
            'text': challenge_text,
            'month': month,
        })
    except:
        return HttpResponseNotFound


# def index(request):
#     months = list(monthly_challenges.keys())
    
#     response_html = ''

#     for month in months:
#         redirect_path = reverse('month-challenge', args=[month])
#         link = f'<a href={redirect_path}>{month}</a><br>\n'
#         response_html += link

#     return HttpResponse(response_html)

def index(request):
    months = list(monthly_challenges.keys())
    return render(request, 'challenges/index.html', {
        'months': months
    })
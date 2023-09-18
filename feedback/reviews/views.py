from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View


class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, 'reviews/review.html', {
            'form': form,
        })
    def post(self, request):
        form = ReviewForm(request.POST) 
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thank-you')
        return render(request, 'reviews/review.html', {
            'form': form,
        })
def review(request):

    # if request.method == 'POST':
    #     entered_username = request.POST['username']
    #     if entered_username == '':
    #         return render(request, 'reviews/review.html', {
    #             'has_error': True,
    #         })
    #     return HttpResponseRedirect('/thank-you')
    if request.method == 'POST':
        # form = ReviewForm(request.POST)
        existing_data = Review.objects.get(pk=1)
        form = ReviewForm(request.POST) 
        if form.is_valid():
            # username = form.cleaned_data['user_name']
            # review_text = form.cleaned_data['review_text'] 
            # rating = form.cleaned_data['rating']
            # review = Review(user_name = username,
            #                review_text = review_text,
            #                rating=rating)
            # review.save()
            form.save()
            return HttpResponseRedirect('/thank-you')


    else:
        form = ReviewForm()
    
    return render(request, 'reviews/review.html', {
        'form': form,
    })

def thank_you(request):
    return render(request, 'reviews/thank-you.html')
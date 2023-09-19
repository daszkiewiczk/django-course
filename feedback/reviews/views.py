from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from .models import Review
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView



# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()
#         return render(request, 'reviews/review.html', {
#             'form': form,
#         })
#     def post(self, request):
#         form = ReviewForm(request.POST) 
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/thank-you')
#         return render(request, 'reviews/review.html', {
#             'form': form,
#         })

# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = 'reviews/review.html'
#     success_url = '/thank-you'
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = '/thank-you'

# class ThankYouView(View):
#     def get(self, request):
#         return render(request, 'reviews/thank-you.html')
class ThankYouView(TemplateView):
    template_name = 'reviews/thank-you.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['message'] = 'This works!'
        return context

# class ReviewsListView(TemplateView):
#     template_name = 'reviews/review_list.html'

#     def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
#         context =  super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context['reviews'] = reviews
#         return context

class ReviewsListView(ListView):
    template_name = 'reviews/review_list.html'
    model = Review
    context_object_name = 'reviews'
    def get_queryset(self) -> QuerySet[Any]:
        basequery = super().get_queryset() 
        data = basequery.filter(rating__gt=4)
        return data


def review(request):

    # if request.method == 'POST':
    #     entered_username = request.POST['username']
    #     if entered_username == '':
    #         return render(request, 'reviews/review.html', {
    #             'has_error': True,2
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

# def thank_you(request):
#     return render(request, 'reviews/thank-you.html')


# class SingleReviewView(TemplateView):
#     template_name = 'reviews/single_review.html'
#     def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
#         context = super().get_context_data(**kwargs)
#         # reviews = Review.objects.all()
#         review_id = kwargs['id']
#         selected_review = Review.objects.get(pk=review_id)
#         context['review'] = selected_review 
#         return context

class SingleReviewView(DetailView):
    model = Review
    template_name = 'reviews/single_review.html'

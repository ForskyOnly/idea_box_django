from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, IdeaForm
from .models import Idea, Vote
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import F


def home_page(request):
    sort_by = request.GET.get("sort_by", "date")

    if sort_by == "best":
        ideas = Idea.objects.all().annotate(vote_sum=F('good') - F('bad')).order_by('-vote_sum', '-date')
    else:
        ideas = Idea.objects.all().order_by('-date')

    if request.method == "POST":
        form = IdeaForm(request.POST)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.user = request.user
            idea.save()
            return redirect("home")
        vote_type = request.POST.get("vote_type")
        idea_id = request.POST.get("idea_id")
        if vote_type and idea_id:
            idea = get_object_or_404(Idea, pk=idea_id)
            user_vote = Vote.objects.filter(user=request.user, idea=idea).first()
            if user_vote:
                if user_vote.vote != vote_type:
                    if vote_type == "UP":
                        idea.good += 1
                    elif vote_type == "DOWN":
                        idea.good -= 1
                    user_vote.vote = vote_type
                    user_vote.save()
            else:
                if vote_type == "UP":
                    idea.good += 1
                elif vote_type == "DOWN":
                    idea.good -= 1
                idea.save()
                vote = Vote(user=request.user, idea=idea, vote=vote_type)
                vote.save()
    else:
        form = IdeaForm()

    return render(request, "main/home.html", {"form": form, "ideas": ideas, "sort_by": sort_by})



class SignupPage(CreateView):
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

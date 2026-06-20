from django.shortcuts import render, redirect
from .models import Question, Result, Profile
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


@login_required(login_url='login')
def test_view(request, category):
    # Har doim savollarni olamiz
    questions = Question.objects.filter(subject=category)
    
    if request.method == 'POST':
        score = 0
        total = questions.count()
        
        # Javoblarni hisoblash
        for q in questions:
            selected_option = request.POST.get(f"question_{q.id}")
            if selected_option == q.correct_answer:
                score += 1
        
        # Natijani saqlash
        Result.objects.create(
            user_name=request.user.username,
            category=category,
            score=score,
            total_questions=total
        )
        
        # Profilni yangilash
        profile, created = Profile.objects.get_or_create(user=request.user)
        profile.total_score += score
        
        # Darajani aniqlash
        if profile.total_score >= 100:
            profile.level = "Senior"
        elif profile.total_score >= 50:
            profile.level = "Middle"
        else:
            profile.level = "Junior"
        profile.save()
        
        # Natija sahifasiga o'tish
        return render(request, 'quiz/result.html', {
            'score': score, 
            'total': total,
            'level': profile.level
        })
    
    # GET so'rovi uchun (testni ko'rsatish)
    return render(request, 'quiz/test.html', {
        'questions': questions, 
        'category': category
    })


def leaderboard_view(request):
    # Ball bo'yicha yuqoridan pastga saralash
    profiles = Profile.objects.all().order_by('-total_score')
    return render(request, 'quiz/leaderboard.html', {'profiles': profiles})




def index_view(request):
    # Bu yerda o'z kodingiz bo'lishi kerak
    return render(request, 'quiz/index.html') # Misol uchun



def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Profil yaratish
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'quiz/signup.html', {'form': form})




def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'quiz/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')




@login_required
def profile_view(request):
    results = Result.objects.filter(user_name=request.user.username)
    return render(request, 'quiz/profile.html', {'results': results})



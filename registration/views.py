from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from portfolio import urls
from django.contrib import messages

# Create your views here.
def Register(request):

	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			messages.success(request, f"Konto utworzono pomyślnie.")
			login(request, user)
			return redirect("/")
		else:
			for msg in form.error_messages:
				messages.error(request, f"Wystąpił problem podczas tworzenia konta.")


	form = UserCreationForm
	args = {
		'form': form
	}
	return render(request, 'registration/register.html', args)
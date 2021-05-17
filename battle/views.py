from django.shortcuts import render
from django.views import View
from video.models import Video

# Create your views here.
class MainView(View):
    def get(self, request):
        stuff = Video.objects.filter(battle_id="battle_id").all()
        return render(request, "main/main.html", {"vids": stuff})
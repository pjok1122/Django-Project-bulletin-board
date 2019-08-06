from django.shortcuts import render,redirect
from django.http import Http404
from django.core.paginator import Paginator
from .models import Board
from users.models import Users
from .forms import BoardForm
from tag.models import Tag
def board_list(request):
    boards_all = Board.objects.all().order_by('-id')
    page = int(request.GET.get('p', 1)) #없으면 1로 지정
    paginator = Paginator(boards_all, 5) #한 페이지 당 몇개 씩 보여줄 지 지정 
    boards = paginator.get_page(page)
    return render(request, "board/board_list.html", {"boards":boards})
def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('페이지를 찾을 수 없습니다.')

    return render(request, "board/board_detail.html", {'board':board})
def board_write(request):
    if not request.session.get('user'):
        redirect('/users/login/')
    if request.method =="POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            user = Users.objects.get(pk=user_id)
            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = user
            board.save()

            tags = form.cleaned_data['tags'].split(',')
            for tag in tags:
                tag = tag.strip()
                _tag, _ = Tag.objects.get_or_create(name=tag)
                
                board.tags.add(_tag)

            return redirect('/board/list/')
    else:
        form = BoardForm()
    
    return render(request, "board/board_write.html", {'form':form})
    
# Create your views here.

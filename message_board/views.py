from django.shortcuts import render
from django.views import generic

from .models import MessageBoard

class IndexView(generic.ListView):
    template_name = 'message_board/index.html'
    context_object_name = 'latest_message_board_list'

    def get_queryset(self):
        return MessageBoard.objects.order_by('-pub_date')[:30]

class DetailView(generic.DetailView):
    model = MessageBoard
    template_name = 'message_board/detail.html'

from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView, CreateView
from influencePower.models import Influencer, NormalUser, Comment
import datetime 
from django.shortcuts import redirect, get_object_or_404, render

class InfluencerList(ListView):
    template_name = 'influencePower/influencer_list.html'
    context_object_name = 'influencer_list'
    def get_queryset(self):
        return Influencer.objects.order_by()
    
class NormalUserList(ListView):
    template_name = 'influencePower/normalUser_list.html'
    context_object_name = 'normaluser_list'
    def get_queryset(self):
        return NormalUser.objects.order_by()
    
class InfluencerDetail(DetailView):
    model = Influencer
    template_name_suffix = '_detail'
    
class NormalUserDetail(DetailView):
    model = NormalUser
    template_name_suffix = '_detail'
    
class CommentCreate(CreateView):
    model = Comment
    fields = ('name', 'text')
    template_name = 'influencePower/comment_form.html'
    def form_valid(self, form):
        influencer_pk = self.kwargs['pk']
        influencer = get_object_or_404(Influencer, pk=influencer_pk)
        comment = form.save(commit=False)
        comment.target = influencer
        comment.save()
        return redirect('influencer_detail', pk=influencer_pk)
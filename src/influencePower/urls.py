from django.urls import path
from influencePower import views

app = 'influencePower'
urlpatterns = [
    path('influencers/',views.InfluencerList.as_view(), name='influencer_list'),
    path('influencers/<int:pk>/',views.InfluencerDetail.as_view(), name='influencer_detail'),
    path('normalusers/',views.NormalUserList.as_view(), name='normaluser_list'),
    path('normalusers/<int:pk>/',views.NormalUserDetail.as_view(), name='normaluser_detail'),
    path('comment/<int:pk>/',views.CommentCreate.as_view(), name='comment_create')
    ]
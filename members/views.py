"""
ThunderSite - ThundeRatz

Members Pages Views
Daniel Nery Silva de Oliveira

02/2018
"""

from django.views.generic import ListView
from .models import Member

class MemberListView(ListView):
    model = Member
    context_object_name = 'members_list'
    template_name = 'members/members_list.html'

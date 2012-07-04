from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.decorators import login_required
from django.http import Http404
from firstclass.middleware.online.settings import FIRSTCLASS_VIEWONLINE_AUTH
from .models import Message

def view_message_online(request, key, template='firstclass/message.html'):
    message = get_object_or_404(Message, key=key)

    if FIRSTCLASS_VIEWONLINE_AUTH:
        if request.user.email not in message.data['to']:
            raise Http404

    return render_to_response(template, {
        'message': message,
    })

if FIRSTCLASS_VIEWONLINE_AUTH:
    view_message_online = login_required(view_message_online)

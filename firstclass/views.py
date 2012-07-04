from django.shortcuts import get_object_or_404, render_to_response
from .models import Message

def view_message_online(request, key, template='firstclass/message.html'):
    message = get_object_or_404(Message, key=key)

    return render_to_response(template, {
        'message': message,
    })

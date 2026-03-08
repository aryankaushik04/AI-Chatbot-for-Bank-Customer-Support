import json
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse
from django.conf import settings

from chatterbot import ChatBot


class ChatSupportAppView(TemplateView):
    template_name = 'app.html'


class ChatSupportApiView(View):
    """
    Provide an API endpoint to interact with Chat Support.
    """

    chat_bot = ChatBot(**settings.CHATTERBOT)

    def post(self, request, *args, **kwargs):
        """
        Return a response to the statement in the posted data.

        * The JSON data should contain a 'text' attribute.
        """
        input_data = json.loads(request.body.decode('utf-8'))

        if 'text' not in input_data:
            return JsonResponse({
                'text': [
                    'The attribute "text" is required.'
                ]
            }, status=400)

        response = self.chat_bot.get_response(**input_data)

        response_data = response.serialize()

        return JsonResponse(response_data, status=200)

    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        return JsonResponse({
            'name': self.chat_bot.name
        })

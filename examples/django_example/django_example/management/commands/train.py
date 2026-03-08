"""
This is an example of a custom Django management command that
trains a ChatterBot instance with specified data.

For more information on how to create custom management commands,
see the Django documentation:
https://docs.djangoproject.com/en/4.2/howto/custom-management-commands/

For details on the available training options for ChatterBot see:
http://docs.chatterbot.us/training/ 
"""

from django.core.management.base import BaseCommand
from django.conf import settings

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os


class Command(BaseCommand):
    help = 'Train a BankSupportBot instance with banking data.'

    def handle(self, *args, **options):
        chatbot = ChatBot(**settings.CHATTERBOT)

        trainer = ChatterBotCorpusTrainer(chatbot)

        # Path to the banking.yml file relative to the project root
        corpus_path = os.path.join(settings.BASE_DIR, '..', '..', 'data', 'banking.yml')
        
        if os.path.exists(corpus_path):
            trainer.train(corpus_path)
            self.stdout.write(self.style.SUCCESS(f'Successfully trained with {corpus_path}'))
        else:
            self.stdout.write(self.style.ERROR(f'Corpus file not found at {corpus_path}'))

        self.stdout.write(
            self.style.SUCCESS('Training completed successfully')
        )

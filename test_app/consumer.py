from channels.consumer import SyncConsumer, StopConsumer
from asgiref.sync import async_to_sync
from .models import Message, Group
class MySyncConsumer(SyncConsumer):

    def websocket_connect(self, event):
        print("channel layer -->", self.channel_layer)
        print("channel name -->", self.channel_name)
        self.name = self.scope['url_route']['kwargs']['name']
        async_to_sync(self.channel_layer.group_add)(self.name, self.channel_name)
        self.send({
            "type": "websocket.accept"
        })


    def websocket_disconnect(self, event):
        print("channel layer -->", self.channel_layer)
        print("channel name -->", self.channel_name)
        async_to_sync(self.channel_layer.group_discard)(self.name, self.channel_name)
        raise StopConsumer()


    def websocket_receive(self, event):
        async_to_sync(self.channel_layer.group_send)(self.name, {
            'type': 'chat.message',
            'message': event['text']
        })

    def chat_message(self, event):
        self.send({
            'type': 'websocket.send',
            'text': event['message']
        })
        
        group = Group.objects.get(name=self.name)
        chat = Message(content=event['message'], group=group)
        chat.save()
    

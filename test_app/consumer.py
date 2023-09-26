from channels.consumer import SyncConsumer, StopConsumer

class MySyncConsumer(SyncConsumer):
    
    def websocket_connect(self, event):
        print("Connect")
        self.send({
            "type":"websocket.accept"
        })
        
    def websocket_disconnect(self, event):
        print("Disconnect")
        raise StopConsumer()
        
    def websocket_receive(self, event):
        print("recieve ->", event['text'])
        self.send({
            'type':'websocket.send',
            'text':"hello world"
        })
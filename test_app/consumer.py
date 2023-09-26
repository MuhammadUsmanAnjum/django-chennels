from channels.consumer import SyncConsumer

class MySyncConsumer(SyncConsumer):
    
    def websocket_connect(self, event):
        print("Connect")
        self.send({
            "type":"websocket.accept"
        })
        
    def websocket_disconnect(self, event):
        print("Disconnect")
        
    def websocket_receive(self, event):
        print("recieve")
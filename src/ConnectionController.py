from ConnectionModel import ConnectionModel
from ConnectionView import ConnectionView

class ConnectionController:
    def __init__(self):
        self.model = ConnectionModel()
        self.view = ConnectionView()
        
        self.update_connections()
        
    def update_connections(self):
        for item in self.view.tree.get_children():
            self.view.tree.delete(item)
            
        conns = self.model.get_connections_info()
        
        for conn in conns:
            ps_conn = conn[-1]
            self.view.tree.insert("", "end",
                    text=conn[2],
                    values=(ps_conn.pid, conn[0], conn[1], ps_conn.laddr.ip, ps_conn.laddr.port,
                            ps_conn.raddr.ip, ps_conn.raddr.port)
                    )
            
        self.view.after(500, self.update_connections)
        
    def run(self):
        self.view.mainloop()

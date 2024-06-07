import psutil
import socket

class ConnectionModel:
    def get_connections_info(self):
        conns = psutil.net_connections(kind="all")
        established_conns = [conn for conn in conns if conn.status == psutil.CONN_ESTABLISHED]

        connection_info = []
        for conn in established_conns:
            protocol = self.get_protocol_type(conn.type)
            direction = 'Outbound' if conn.laddr < conn.raddr else 'Inbound'
            process = psutil.Process(conn.pid)
            
            connection_info.append((protocol, direction, process.name(), conn))

        return connection_info

    def get_protocol_type(self, conn_type):
        if conn_type == socket.SOCK_STREAM:
            return 'TCP'
        elif conn_type == socket.SOCK_DGRAM:
            return 'UDP'
        elif conn_type == socket.SOCK_RAW:
            return 'RAW'
        else:
            return 'OTHER'
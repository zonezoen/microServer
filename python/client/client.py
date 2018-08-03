from python.test import ttypes
from python.test import UserService

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


__HOST = 'localhost'
__PORT = 3001

tsocket = TSocket.TSocket(__HOST, __PORT)
transport = TTransport.TBufferedTransport(tsocket)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = UserService.Client(protocol)

stu = UserService.Student("zone","18")

transport.open()
client.addStu(stu)
print(client.getStu("zone"))
transport.close()


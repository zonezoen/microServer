import socket
import sys

# sys.path.append('./gen-py')
from python.test import ttypes
from python.test import UserService
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

stus = {}


class TestHandler:
    def addStu(self, stu):
        print("python server add student.")
        stus[stu.name] = stu
        # print("add new student : " + stu.name)

    def getStu(self, name):
        print("python server get student.")
        print("get student : " + name)
        return stus[name]


# 创建服务端
handler = TestHandler()
processor = UserService.Processor(handler)
# 监听端口
transport = TSocket.TServerSocket("localhost", 3001)
# 选择传输层
tfactory = TTransport.TBufferedTransportFactory()
# 选择传输协议
pfactory = TBinaryProtocol.TBinaryProtocolFactory()
# 创建服务端
server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
print("Starting thrift server in python...")
server.serve()


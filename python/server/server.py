import socket
import sys
from python.test import ttypes
from python.test import UserService
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
stus = {}
class TestHandler:
    def addStu(self, stu):
        print("我是 python 服务器，我的 addStu() 方法被调用了.")
        stus[stu.name] = stu
        # print("add new student : " + stu.name)

    def getStu(self, name):
        print("我是 python 服务器，我的 getStu() 方法被调用了.")
        print("get student : " + name)
        return stus[name]

# 创建服务端
handler = TestHandler()
processor = UserService.Processor(handler)
# 监听端口
transport = TSocket.TServerSocket("127.0.0.1", 3000)
# 选择传输层
tfactory = TTransport.TBufferedTransportFactory()
# 选择传输协议
pfactory = TBinaryProtocol.TBinaryProtocolFactory()
# 创建服务端
server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
print("Starting thrift server in python...")
server.serve()







from python.test import ttypes
from python.test import UserService
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

__HOST = '127.0.0.1'
__PORT = 3000
tsocket = TSocket.TSocket(__HOST, __PORT)
transport = TTransport.TBufferedTransport(tsocket)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
# 穿件客户端
client = UserService.Client(protocol)
# thrift 生成的的 Student 结构
stu = UserService.Student("zone", "18")
transport.open()
# 调用服务端 addStu() 方法
print("我是 python 客户端，我调用了 addStu() 方法.")
client.addStu(stu)
# 调用服务端 getStu() 方法
print("我是 python 客户端，我调用了 getStu() 方法.")
print("返回的结果为：")
print(client.getStu("zone"))
transport.close()

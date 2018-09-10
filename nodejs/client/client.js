var thrift = require('thrift');
var UserService = require('../UserService.js');
var ttypes = require('../test_types');

var connection = thrift.createConnection('127.0.0.1', 3000);
var client = thrift.createClient(UserService, connection);
connection.on("error", function (e) {
    console.log(e);
});
var stu = new ttypes.Student({name: "zone-nodejs", age: "23"});
// 调用服务端 addStu() 方法
client.addStu(stu, function (err, res) {
    if (err) {
        console.log(err);
        return
    }
    console.log("我是 nodejs 客户端，我调用了 addStu() 方法.")
})
// 调用服务端 getStu() 方法
client.getStu("zone-nodejs", function (err, res) {
    if (err) {
        console.log(err);
        return
    }
    console.log("我是 nodejs 客户端，我调用了 getStu() 方法.")
    console.log("返回的结果为：" + JSON.stringify(res))
})




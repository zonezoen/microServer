var thrift = require("thrift");
var UserService = require('../UserService.js');
var ttypes = require('../test_types');

var stus = {}
var server = thrift.createServer(UserService,
    {
        addStu: function (stu, callback) {
            console.log("我是 nodejs 服务器，我的 addStu() 方法被调用了.");
            stus[stu.name] = stu
            console.log(stu);
            callback();
        },
        getStu: function (name, callback) {
            console.log("我是 nodejs 服务器，我的 getStu() 方法被调用了.");
            callback(null, stus[name])
        }
    }
);
// 启动服务
server.listen(3000);
console.log("nodejs server start");
server.on("error", function (e) {
    console.log(e);
});














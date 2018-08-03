var thrift = require("thrift");
var UserService = require('../UserService.js');
var ttypes = require('../test_types');

var stus = {}
var server = thrift.createServer(UserService,
    {
        addStu: function (stu, callback) {
            console.log(stu);

            console.log("add student");
            stus[stu.name] = stu
            console.log(stu);
            callback();

        },
        getStu: function (name, callback) {
            console.log("get stu " + name);
            callback(null, stus[name])
        }
    }
);

server.listen(3001);
console.log("server start");

server.on("error", function (e) {
    console.log(e);
});
var thrift = require('thrift');
var UserService = require('../UserService.js');
var ttypes = require('../test_types');

var connection = thrift.createConnection('localhost', 3001);
var client = thrift.createClient(UserService, connection);

connection.on("error", function (e) {
    console.log(e);
});

var stu = new ttypes.Student({name: "zone-nodejs", age: "23"});
client.addStu(stu, function (err, res) {
    if (err) {
        console.log(err);
        return
    }
    console.log("add stu on nodejs client")
    console.log(res)
})

client.getStu("zone-nodejs", function (err, res) {
    if (err) {
        console.log(err);
        return
    }
    console.log("get stu on nodejs client");

    console.log(res)
})




var amqp = require('amqp');

var connection = amqp.createConnection({url: "amqp://zone:123456@118.25.222.89:5672"});

// add this for better debuging
connection.on('error', function(e) {
  console.log("Error from amqp: ", e);
});

// Wait for connection to become established.
connection.on('ready', function () {
  // Use the default 'amq.topic' exchange
  connection.queue('hello', function (q) {
      // Catch all messages
      q.bind('#');

      // Receive messages
      q.subscribe(function (message) {
        // Print messages to stdout
        console.log(message);
      });
  });
});

var http = require('http');

http.createServer(function (req, res) {
  res.write('Its working!');
  res.write('\nnode');
  res.end();
}).listen(80);

console.log('Server running at 80');

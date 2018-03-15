var a = 1
var b = 0
var c = 0
var d = 1
var len = ''
var element= ''

var readline = require('readline');

var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.on('line', (line) => {
  len = line;
  rl.pause()
});

console.log(len);

// function fibonacci(element) {
// for (var i = 0; i < element; i++) {
//   var rl2 = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout
//   });
//   rl2.on('line', (line) => {
//     for (var i = 0; i < line; i++) {
//       a, b = b, a+b;
//       c, d = d, c+d;
//     }
//     a = toString(a)
//     c = toString(c)
//     console.log(a+' '+c)
//   });
// }
//
// }

var fs = require('fs'),
    input = fs.readFileSync('/dev/stdin').toString(),
    lines = input.split("\n");

lines.shift();

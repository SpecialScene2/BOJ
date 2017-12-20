var fs = require('fs'), a = '', b = '';

var text = fs.readFileSync('input.text', 'utf8');
text = text.split(' ');
a = Number(text[0])
b = Number(text[1])
console.log(a/b)

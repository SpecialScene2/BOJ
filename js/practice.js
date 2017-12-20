var fs = require('fs');

var text = ''
var result1 = ''
var result2 = ''
// 동기적 읽기
var text = fs.readFileSync('input.text', 'utf8');
text = text.split('\n');
console.log(text)

function fibonacci_zero(num){
  var a = 1, b = 0, temp;

  while (num >= 2){
    temp = b;
    b = a + b;
    a = temp;
    num--;
  }

return b;
}

function fibonacci_one(num){
  var a = 0, b = 1, temp;

  while (num >= 2){
    temp = b;
    b = a + b;
    a = temp;
    num--;
  }

return b;
}

function fibonacci() {
 for (var i = 0; i < Number(text[0]); i++) {
   console.log('Count')
   if (Number(text[i+1])>1) {
     result1 = String(fibonacci_zero(text[i+1]));
     result2 = String(fibonacci_one(text[i+1]));
     console.log(result1+' '+result2);
   }
   else if (Number(text[i+1]) === 0) {
     var a = 1, b = 1;
     result1 = String(a);
     result2 = String(b);
     console.log(result1+' '+result2);
   }
   else if (Number(text[i+1]) === 1) {
     var a = 0, b = 1;
     result1 = String(a);
     result2 = String(b);
     console.log(result1+' '+result2);
   }
 }

}

fibonacci();

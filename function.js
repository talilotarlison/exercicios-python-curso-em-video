
function b(num=2){
var soma = num + 10
console.log(soma);
console.log("minha soma!");
return soma + 10
}

var res = b();

console.log(res);

console.clear;
//função anonima

var f = function (soma=10){
  return soma + 10
}


console.log(f(2));

var numero = prompt("Digite o numero fatorial: ")
fatorial = numero
for (var i = 1; i < numero; i++){
  fatorial = fatorial * i  
  
} 
console.log(`seu numero é ${fatorial}`)


var numero = 10
fatorial = numero
for (var i = 1; i < numero; i++){
  fatorial = fatorial * i  
  
} 
console.log('seu numero é' + fatorial)

// uso de switch no javascrip
const expr = prompt()
switch (expr) {
  case 'Oranges':
    console.log('Oranges are $0.59 a pound.');
    break;
  case 'Mangoes':
  case 'Papayas':
    console.log('Mangoes and papayas are $2.79 a pound.');
    // expected output: "Mangoes and papayas are $2.79 a pound."
    break;
  default:
    console.log(`Sorry, we are out of ${expr}.`);
}

// https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/switch

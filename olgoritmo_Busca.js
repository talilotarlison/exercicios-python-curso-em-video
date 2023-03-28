//https://pt.khanacademy.org/computing/computer-science

function buscar(valor){
    
var primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];

var numero;
numero = valor;

for ( i=0; i <= primes.length; i++){
    if( primes[i] == numero){
        console.log("Tem na lista!");
    }else{
        console.log("Nao tem na Lista!");
    }
  }
}
buscar(20)


// Outra  maneira de fazer busca linear:

function buscar(valor){
    
var primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];
//console.log(primes[1] )
var numero;
numero = valor;

for ( i=0; i <= primes.length; i++){
    if( primes[i] == numero){
        console.log(" Tem o numero " + primes[i] + "na Lista!");
  }
 }
}
buscar(23)

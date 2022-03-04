//Librerias para manejar los diferentes tipos de variable.
#include <iostream>
#include <string>
// Se utiliza ese comando para abreviar la librería estandar en el código.
using namespace std;
//Función principal, donde va todo el programa.
int main(){ 
//std::cout<<"Este es mi primer programa"<<std::endl; //similar a np.cos() (Opción)
cout<<"Este es mi primer programa"<<endl; //similar a np.cos()
//Declarar variables:
int a=4;
float b=6.0;
double c=1e-6;
float k;
k=1.;
cout<<k<<endl;
cout<<"b = "<<b<<endl;
//Ingresar una variable
int s;
cout<<"Ingrese el valor entero: ";cin>>s;
//Char es para caracteres y guarda como un array
const char carac[] = "Char es para caracteres";
cout<<carac<<endl;
//String mantiene la palabra u oración completa.
string g="String es todo completo";
//string a = "Prueba de poner otro valor en la misma variable (Bota error si se declara el tipo de variable)";
k=2.;
cout<<k<<endl;
//Números binarios (0b) y hexadecimales (0x)
int v=0b11;
// a retorna el número ascii
int h=0xa;
cout<<"Número Binario: "<<v<<endl;
cout<<"Número Hexadecimal: "<<h<<endl;
return 0;
}
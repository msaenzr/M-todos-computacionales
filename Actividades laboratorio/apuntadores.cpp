#include <iostream>
using namespace std;
void suma(double x,double y, double &z){
    z=x+y;
}

int main (){
    double a=2;
    double *p;
    p=&a; //Posición de memoria de la variable.
    cout<<p<<endl;
    cout<<*p<<endl; // * Retorna el valor guardado en la posición de memoria indicada.
    double b[2][3]={{1,2,3},{4,5,6}};
    cout<<b<<endl;
    cout<<b[0][0]<<endl;
    double *q;
    q=&b[0][0];
    cout<<"Posiciones de memoria de b"<<endl;
    for (int i=0;i<6;i++){
        //for(int j=0;j<3;j++){}
        cout<<q<<endl;
        cout<<*q<<endl;
        q++; //Asignar una posición siguiente en la matrz b
    }
    cout<<"Tamano de 0x1f815ffab8: "<<sizeof(0x1f815ffab8)<<endl; //Tamaño de una variable 
    //Ejemplo de la función suma
    double x=1,y=3,z;
    suma(x,y,z);
    cout<<"z = "<<z<<endl;
    return 0;
}
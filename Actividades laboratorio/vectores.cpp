#include <iostream>
using namespace std;

//Suma de vectores
 void suma(int n, double A[],double B[],double C[]){
    for (int i=0;i<n;i++){
        C[i]=A[i]+B[i];
    }
}

//Resta de vectores
 void resta(int n, double A[],double B[],double C[]){
    for (int i=0;i<n;i++){
        C[i]=A[i]-B[i];
    }
}
 //Producto de un vector con un escalar
 void producto_por_escalar (int n, double k, double A[],double C[]){
    for (int i=0;i<n;i++){
        C[i]=k*A[i];
    }
}
//Producto interno 
 double producto_interno(int n, double B[], double A[]){
    double d=0;
    for (int i=0;i<n;i++){
        d+= A[i]*B[i];
    }
    return d;
}
//Función para imprimir un vector
void imprimir(int n, double C[]){
    cout<<"(";
    for (int i=0;i<n;i++){
        cout<<C[i]<<",";
    }
    cout<<")"<<endl;

}

//Verificar ortogonalidad de dos vectores
void ortogonalidad(int n, double A[],double B[]){
    double d= producto_interno(n,B,A);
    if(d!=0)
        cout<<"Los vectores no son ortogonales"<<endl;
    else
        cout<<"Los vectores son ortogonales"<<endl;
    }

int main(){

    //Variable de presición para las funciones
    int n=3;
    double k=2.5;
    //Creacion de vectores
    double A[n]={1,2,3};
    double B[n]={3,4,5};
    double C[n]={0,0,0};
    //Llamar funciones
    suma(n,A,B,C);
    imprimir(n,C);
    resta(n,A,B,C);
    imprimir(n,C);
    producto_por_escalar(n,k,A,C);
    imprimir(n,C);
    cout<<"Producto A*B"<<endl<<producto_interno(n,B,A)<<endl;
    ortogonalidad(n,A,B);
    return 0;
}
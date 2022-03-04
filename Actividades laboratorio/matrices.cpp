#include <iostream>
using namespace std;

//Suma de matrices

void suma_matrices(int n,int m, double A[][3],double B[][3],double D[][3]){
    //n=Número de filas
    //m=Número de columnas
    for (int i=0;i<n;i++){
        for (int j=0;j<m;j++){
            D[i][j]+=(A[i][j]+B[i][j]);
        }
    } 
}

void resta_matrices(int n,int m, double A[][3],double B[][3],double R[][3]){
    //n=Número de filas
    //m=Número de columnas
    for (int i=0;i<n;i++){
        for (int j=0;j<m;j++){
            R[i][j]+=(A[i][j]-B[i][j]);
        }
    } 
}

void producto_escalar(int n, int m, double A[][3], double R[][3], int k){
    //n=Número de filas
    //m=Número de columnas
    for (int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            R[i][j]+=(A[i][j]*k);
        }
    }
}

void producto_matrices(int n, int m,double A[][3],double C[][2], double M[][2]){

    for (int i=0;i<n;i++){
        for (int j=0;j<n;j++){
            int v=0;
            for(int p=0;p<m;p++){
                v+=A[i][p]*C[p][j];
            }
            M[i][j]=v;
        }
    }
}

void imprimir_matriz(int n, int m, double D[][3]){
    for (int i=0;i<n;i++){
        for (int j=0;j<m;j++){
            cout<<D[i][j]<<" ";
        }
        cout<<endl;

    }
}

void imprimir_matriz2(int n, double D[][2]){
    for (int i=0;i<n;i++){
        for (int j=0;j<n;j++){
            cout<<D[i][j]<<" ";
        }
        cout<<endl;

    }
}

int main(){
    //Declaración de valores de presición
    int n=2;
    int m=3;
    double k=4;
    //Creación de matrices nxm y mxn
    double A[][3]={{1,2,3},{4,5,6}};
    double B[][3]={{6,5,4},{2,5,4}};
    double C[][2]={{1,2},{3,4},{5,6}};
    //Matriz de salida
    double D[n][3];
    double R[n][3];
    double N[n][3];
    double M[n][2];
    //Llamar funciones
    suma_matrices(n,m,A,B,D);
    cout<<"Suma de matrices A y B:"<<endl;
    imprimir_matriz(n,m,D);
    cout<<"Resta de matrices A y B:"<<endl;
    resta_matrices(n,m,A,B,R);
    imprimir_matriz(n,m,R);
    cout<<"Producto por escalar A*k: "<<endl;
    producto_escalar(n,m,A,N,k);
    imprimir_matriz(n,m,N);
    cout<<"Producto de matrices A*C: "<<endl;
    producto_matrices(n,m,A,C,M);
    imprimir_matriz2(n,M);
    return 0;
}
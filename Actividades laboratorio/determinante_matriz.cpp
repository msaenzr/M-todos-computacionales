#include <iostream>
using namespace std;

int main(){
    
    //Inicialización de variables dadas por el usuario.
    //Número de filas
    int m;
    //Número de columnas
    int n;
    cout<<"Ingrese el numero de filas: "<<endl;
    cin>>m;
    cout<<"Ingrese el numero de columnas: "<<endl;
    cin>>n;
    //Número de columnas de la matriz aumentada
    if (m!=n){
        cout<<"Hay un error, los valores de la fila y de las columnas deben ser iguales."<<endl;
    }
    double A[m][n];
    double B[m][n];

    for (int i=0; i<m; i++){
        cout<<"Ingrese la fila #"<<i<<": "<<endl;
        for (int j=0; j<n; j++){
            cin>>A[i][j];

        }
    }
    //Impresión de matriz que entra por parámetro
    cout<<"La matriz ingresada es: "<<endl;
    for (int i=0; i<n;i++){
        for (int j=0;j<m;j++){
            cout<<A[i][j]<<" ";
        }
        cout<<endl;
    }

    //Algoritmo de reducción matriz triangular superior
    float det =1;
    double l[n];
    for (int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            l[j] = A[i][j];
            //cout<<"fila: "<<l[j]<<endl;
        }
        int k =i;
        while (k<m){
            float c =-A[k][i]/l[i];                 
            if(k!=i & c!=0){
                for (int f=0;f<n;f++){
                    A[k][f] = A[k][f] + (c*l[f]);
                }
            }
            k++;
        }
        det *= l[i];
    }

    //Impresión de matriz que entra por parámetro
    cout<<"La matriz triangular superior es: "<<endl;
    for (int i=0; i<n;i++){
        for (int j=0;j<m;j++){
            cout<<A[i][j]<<" ";
        }
        cout<<endl;
    }
    //Impresión del valor del determinante
    cout<<"El determinante de la matriz es :"<<det<<endl;
    return 0;
}
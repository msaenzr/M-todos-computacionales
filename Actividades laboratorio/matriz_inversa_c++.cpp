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
    int nb = 2*n;
    if (m!=n){
        cout<<"Hay un error, los valores de la fila y de las columnas deben ser iguales."<<endl;
    }
    double A[m][n];
    double B[m][nb];

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
  
    //Estructuración de matriz aumentada 
    for (int i=0;i<m;i++){
      for (int j=0;j<n;j++){
        B[i][j] = A[i][j];
      }
      for (int j=n;j<nb;j++){
        if(i==j-n)
          B[i][j]=1;
        else
          B[i][j]=0;
      }
    }
    //Impresión de matriz aumentada inicial
    cout<<"La matriz aumentada es: "<<endl;
    for (int i=0; i<m;i++){
        for (int j=0;j<nb;j++){
            cout<<B[i][j]<<" ";
        }
        cout<<endl;
    }
    
    //Comprobación de que el primer elemento no sea cero, y si lo es, correr la fila
      if (B[0][0]==0){
      for (int h=0;h<1;h++){
        for (int d=0;d<nb;d++){
          float ac =B[h][d];
          float ac2 =B[h+1][d];
          B[h][d]=ac2;
          B[h+1][d]=ac;
        }
      }
    }
    //Algoritmo de reducción 
    double l[nb];
    for (int i=0;i<m;i++){
      float piv =B[i][i];
      for(int j=0; j<nb;j++){
        B[i][j] = B[i][j]/piv;
        l[j] = B[i][j];
        }
      for (int k=0;k<m;k++){
        float c=B[k][i];
        if(k!=i){
          for(int f=0;f<nb;f++){
            B[k][f] = B[k][f] + (l[f]*-c);
          }
        }
      }
          }

    //Impresión de matriz invertida 
    cout<<"La matriz invertida es: "<<endl;
    for (int i=0; i<m;i++){
        for (int j=n;j<nb;j++){
            cout<<B[i][j]<<" ";
        }
        cout<<endl;
    }
    return 0;
}

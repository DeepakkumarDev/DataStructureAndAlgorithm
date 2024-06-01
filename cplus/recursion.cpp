#include <iostream>

using namespace std;

void fun(int n){
    if(n>0){
        printf("%d ",n);
        // cout<<n<<" ";
        // cout<<n<<endl;
        fun(n-1);
    }
}

void fun2(int n){
    if(n>0){
        fun2(n-1);
        cout<<n<<" ";
    }
}

//Recursive Function using Static and Global Variable

int fun3(int n){
    if(n>0){
        return fun3(n-1)+n;
    }
    return 0;
}
int fun4(int n){
    static int x=0;
    if(n>0){
        x++;
        return fun4(n-1)+x;
    }
    return 0;
}
int a=0;
int fun5(int n){
    if(n>0){
        a++;
        return fun5(n-1)+a;
    }
    return 0;
}

int main(){
   int x=5;
   cout<<"Static "<<endl;
   cout<<fun4(x)<<",";
   cout<<endl;
   cout<<"Not Static"<<endl;
   cout<<fun3(x)<<" ";
   cout<<endl;
   cout<<"Gloabal"<<endl;
   cout<<fun5(x)<<"";
   cout<<endl;
//    fun2(x);
//    fun(x);

    

    return 0;
}

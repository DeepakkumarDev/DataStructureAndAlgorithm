#include <iostream>
#include <vector>
using namespace std;

int main(){
    // vector<int> arr;
    // vector<int> arr={1,2,10,12,15};

    vector<int> arr(10,7);
    vector<int> visited(100,0);
    
    arr.pop_back();

    arr.push_back(16);

    for(int i=0;i<arr.size();i++){

        cout<<arr[i]<<endl;
    }

    cout<<arr.size()<<endl;

    cout<<arr.capacity()<<endl;


    return 0;
    
}
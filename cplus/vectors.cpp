#include <iostream>
#include <vector>
#include<string>
#include<unordered_set>
using namespace std;

/*
Given an array containing N integers ,and an numbers S denoting a target sum.
Find two distinct integers that can pair up to form target sum.Let us assume there will be 
only one such pair 
*/


vector<int> pairSum(vector<int> arr,int Sum){
    //logic
    unordered_set<int> s;
    vector<int> result;
    for(int i=0;i<arr.size();i++){
        int x=Sum-arr[i];
        if(s.find(x)!=s.end()){
            result.push_back(x);
            result.push_back(arr[i]);
            return result;
        }
        s.insert(arr[i]);
    }

    return {};
}

int main(){
    vector<int> arr{10,5,2,3,-6,9,11};
    int Sum=4;
    auto p=pairSum(arr,Sum);
    if(p.size()==0){
        cout<<"No Such Pair";
    }
    else{
        cout<<p[0]<<","<<p[1]<<endl;
    }

    return 0; 
}








vector<string> fizzbuzz(int n){
    vector<string> result;
    for(int i=1;i<=n;i++){
        if((i%15)==0){
            result.push_back("FizzBuzz");
        }
        else if(i%5==0){
            result.push_back("Buzz");
        }
        else if(i%3==0){
            result.push_back("Fizz");
        }
        else{
            result.push_back(to_string(i));
        }
    }
    return result;
}




// int main(){
    // vector<int> arr;
    // vector<int> arr={1,2,10,12,15};
    //Fill Constructor 
    // vector<int> arr(10,7);
    // vector<int> visited(100,0);
    
    // arr.pop_back();

    // arr.push_back(16);

    // for(int i=0;i<arr.size();i++){

    //     cout<<arr[i]<<endl;
    // }

    // cout<<arr.size()<<endl;

    // cout<<arr.capacity()<<endl;

    // vector<vector<int>> arr={
    //     {1,2,3},
    //     {4,5,6},
    //     {7,8,9,10},
    //     {11,12}};
    //     arr[0][0]+=10;
    // for(int i=0;i<arr.size();i++){
    //     for(int number=0;number<arr[i].size();number++){
    //         cout<<arr[i][number]<<",";
    //         // for(int number:arr[i]){
    //         // cout<<number;
            
    //     }
    //     cout<<endl;
    // }

// vector<string> output=fizzbuzz(30);
// for(string x: output){
//     cout<<x<<",";
// }
    
// }


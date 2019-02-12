//
// Created by Anurag Sarkar on 2019-02-12.
//

//Vasya has recently learned to type and log on to the Internet. He immediately entered a chat room
// and decided to say hello to everybody. Vasya typed the word s. It is considered that Vasya managed
// to say hello if several letters can be deleted from the typed word so that it resulted in the word
// "hello". For example, if Vasya types the word "ahhellllloou", it will be considered that he said hello,
// and if he types "hlelo", it will be considered that Vasya got misunderstood and he didn't manage to
// say hello. Determine whether Vasya managed to say hello by the given word s.


#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    string s;
    cin>>s;
    string x = "";
    string f = "hello";
    for(int i =0;i<5;i++) {
        int p = s.find(f[i]);
        if(p != string::npos) {
            x += s[p];
            s.erase(0,p+1);
        }
    }
//    cout << s;
    if(x == f) cout << "YES";
    else cout << "NO";

}
//
// Created by Anurag Sarkar on 2019-01-29.
//

//peasant multiplication. A variant of this method was copied into the Rhind papyrus by
//the Egyptian scribe Ahmes around 1650 BC, from a document he claimed was (then) about
//350 years old. This was the most common method of calculation by Europeans before Fibonacci’s
//introduction of Arabic numerals; it was still taught in elementary schools in Eastern Europe
//in the late 20th century. This algorithm was also commonly used by early digital computers
//that did not implement integer multiplication directly in hardware.



//The peasant multiplication algorithm breaks the difficult task of general multiplication
//into four simpler operations:
//(1) determining parity (even or odd),
//(2) addition,
//(3) duplation (doubling a number),
//and (4) mediation (halving a number, rounding down).
//Of course a full specification of this algorithm requires describing how to perform
//those four ‘primitive’ operations. Peasant multiplication requires (a constant factor!)
//more paperwork to execute by hand, but the necessary operations are easier (for humans)
//to remember than the 10 × 10 multiplication table required by the American grade school
//algorithm


#include <iostream>

using namespace std;

int peasentMultiply(int n, int m) {
    int prod = 0; // start int product with setting it to 0
    while(n > 0) { // start counter
        prod += m; // add any variable n or m (flow will change accordingly)
        n = n/2; // n -> n/2
        m *= 2; // m -> m*2
    }
    return prod; // return product
}

int main() {
    int n,m;
    cin>>n>>m;
    cout << peasentMultiply(n,m);
    return 0;
}


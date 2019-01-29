//
// Created by Anurag Sarkar on 2019-01-29.
//

#include <algorithm>
#include <vector>
#include <math.h>
using namespace std;

#ifndef HAILEY_CONGRESSIONALAPPOINTMENT_H
#define HAILEY_CONGRESSIONALAPPOINTMENT_H

//Representatives and direct Taxes shall be apportioned among the several States which
//may be included within this Union, according to their respective Numbers. . . . The
//Number of Representatives shall not exceed one for every thirty Thousand, but each State
//shall have at Least one Representative. . . .

//Since there are a limited number of seats available in the House of Representatives, exact
//proportional representation is impossible without either shared or fractional representatives,
//neither of which are egal. As a result, several different apportionment algorithms have been
//proposed and used to round the fractional solution fairly. The algorithm actually used today,
//called the Huntington-Hill method or the method of equal proportions, was first suggested by
//Census Bureau statistician Joseph Hill in 1911, refined by Harvard mathematician Edward Huntington
//in 1920, adopted into Federal law (2 U.S.C. §§2a and 2b) in 1941, and survived a Supreme
//Court challenge in 1992.7 The input array Pop[1 .. n] stores the populations of the n states,
//and R is the total number of representatives. Currently, n = 50 and R = 435.The outputarray Rep[1 .. n]
//stores the number of representatives assignedto each state.

class CongressionalAppointment {
public:
    vector<double> congressionalAppointment(vector<int>population, int representative) {
        vector<double >rep;
        for(int i=0;i<population.size();i++) {
            rep.push_back(1 + (1/(sqrt((i+2)*(i+1)))));
        }
        return rep;
    }
};


#endif //HAILEY_CONGRESSIONALAPPOINTMENT_H

//
// Created by Anurag Sarkar on 2019-02-02.
//

#ifndef HAILEY_TOWEROFHANOI_H
#define HAILEY_TOWEROFHANOI_H

#endif //HAILEY_TOWEROFHANOI_H


//The Tower of Hanoi puzzle was first published by the mathematician François Éduoard
//Anatole Lucas in 1883, under the pseudonym ‘N. Claus (de Siam)’ (an anagram of ‘Lucas d’Amiens’).
//The following year, Henri de Parville described the puzzle with the following remarkable story:

//In the great temple at Benares beneath the dome which marks the centre of the world, rests a
//brass plate in which are fixed three diamond needles, each a cubit high and as thick as the body
//of a bee. On one of these needles, at the creation, God placed sixty-four discs of pure gold, the
//largest disc resting on the brass plate, and the others getting smaller and smaller up to the top
//one. This is the Tower of Bramah. Day and night unceasingly the priests transfer the discs from
//one diamond needle to another according to the fixed and immutable laws of Bramah, which require
//that the priest on duty must not move more than one disc at a time and that he must place this
//disc on a needle so that there is no smaller disc below it. When the sixty-four discs shall have
//been thus transferred from the needle on which at the creation God placed them to one of the
//other needles, tower, temple, and Brahmins alike will crumble into dust, and with a thunderclap
//the world will vanish.

class TowerOfHanoi {
public:

    void towerOfHanoi(int numberOfDisk, char fromTower, char toTower, char auxTower) {
        int totalMoves = 0;
        if(numberOfDisk > 1) {
            towerOfHanoi(numberOfDisk-1,fromTower,auxTower,toTower);
            totalMoves++;
            towerOfHanoi(numberOfDisk-1,auxTower,toTower,fromTower);
        }
    }



};
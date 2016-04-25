# BUG LIST

Please dont remove fixed problems, but move them to the **fixed**-section!

## Current problems

#### 160422_01
player cant jump into an exactly 2 blocks high passage from 1 block below, because she will jump past the fitting position -> jumpspeed

#### 160422_02
player will be ported on top of a block, if she hits it from the side while falling downwards.

## Fixed Problems

#### 160424_01
collision boxes of the animals aren't calculated correctly on the left and the right
- fixed 160424, reason: plotting of world blocks was relative to a fixed one-block-wide player model, not dynamically



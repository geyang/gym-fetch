here is the summary for the three domains:

1. uniformly sample distractor object, but feed a constant target for it.
2. initialize the distractor object at a fixed location, and the target to be the same location. The target remains the same throughout the episode and the entire training session. There will not be tracking.
3. pick w of the tasks from 1), uniformly sample between them using an environment wrapper, and learn a single multi-task policy.

 Let me know if there is anything you would like to add! (edited) 

------

I think we are on the same page, but just to be sure:
First of all, there is no tracking throughout an episode for all those envs.

1. uniformly initialize the locations of both the object of interest and the distractor object.
2. uniformly initialize the locations of the object of interest, but fix the initialization location of the distractor object.
3. pick a few of tasks from 1 (for instance, block-PickAndPlace with lid-PickAndPlace), learn one policy that is able to accomplish both. No distractor anymore.

(edited)
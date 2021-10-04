# CROSMO
CROSMO (CRop Space MOdule) is a deployable module capable of providing fresh food to the crew, optimizing as many resources and time as possible. In addition, CROSMO will have the ability to indicate the astronauts' dietary regimen, considering the food nutrients and resources.

In this section we study the problem of managing a crop production system to provide the necessary nutrients for a long-duration exploration mission. The crop system must support the nutritional requirements of the crew, including key nutrients and vitamins (such as Vitamins B1, C, and K).

To achieve this efficiently, we propose the use of mathematical optimization to define the approximate number and type of seeds to plant, while minimizing the amount of total weight of the crops. We use mathematical optimization to select the best alternative (Chong & Zak, 2001). 

We solve this problem through linear programming, taking into consideration past work in diet problems (Stigler, 1945; Gass S.I., Harris C.M., 2001). In this case, the crops considered where red romaine lettuce, chinese cabbage, mizuna mustard, and the set of types of nutrients is I={Vitamin B,..., Vitamin C}. Let j ∈ J denote the crop j, and let i ∈ I denote the nutrient i. 

In the model, parameters weight_j denote the weight of crop j when it is harvested, nutrients_ij represent the amount of nutrients of type i of the kind of crop j, b_j is the minimum requirement of nutrient j. Variables x_j represent the number of grams of crop j every member of the crew should eat, and variables z_j represent a penalty if the nutritional requirement is not satisfied.

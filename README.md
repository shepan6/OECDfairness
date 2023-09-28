# ethicAI - Ethical Data and AI framework for evaluating fairness

ethicAI aims to serve data professional with key tools to understand fairness in three main aspects of the modelling pipeline:

Raw/Preprocessed Data -> Model Building -> Decision Augmentation

Looks to augment fairkit-learn (https://github.com/INSPIRED-GMU/fairkit-learn) (Johnson & Brun, 2002) and AI Fairness 360 (Bellamy et al., 2018), which predominantly focus on helping to optimise models on both performance metrics and certain metrics.

## Installation
Run the following to install:
   `pip install ethically`

## Raw/Preprocessed Data 

NOTE: could make this compatible with Tensorflow Datasets object. Can also create a datasets object, which is compatible with Tensorflow Datasets object.

The goal of this section of the framework to evaluate data fairness. 
Taking inspiration from Sureesh & Gutag 2019, there are various forms of bias to consider in both raw and processed datasets, namely:
- Historical bias
    - Evaluating rate of priveledged groups with favourable outcomes vs unpriveledged groups with unfavourable outcomes.
- Sample Selection \ Representation bias
    - Representativeness
        - Training and test sets are "similar" to one another.
            - Principal components in same order (from explaining most of the underlying data to least.)
- Measurement bias

## Model Building 

- Group-Independent Predictions: ensuring that model predictions are unaffected by demographic group membership.
- Equal Metrics across groups: ensuring that model performance metrics across groups are similar to each other.


## Decision Augmentation

### Model discrimination

This section looks to understand which (combination of) input feaures have the highest discriminatory power on the output. 
For this, could base this tool with Linear Discriminant Analysis (?) 

### Model robustness

Evaluating model performance as a function of test set variability. As test set variability (variation fo features) is bigger than that of the training set, we can evaluate model fit as a function of difference between training and test set.


## References 

Bellamy, R. K., Dey, K., Hind, M., Hoffman, S. C., Houde, S., Kannan, K., ... & Zhang, Y. (2018). AI Fairness 360: An extensible toolkit for detecting, understanding, and mitigating unwanted algorithmic bias. arXiv preprint arXiv:1810.01943.

Johnson, B., & Brun, Y. (2022, May). Fairkit-learn: a fairness evaluation and comparison toolkit. In Proceedings of the ACM/IEEE 44th International Conference on Software Engineering: Companion Proceedings (pp. 70-74).

Suresh, H., & Guttag, J. V. (2019). A framework for understanding unintended consequences of machine learning. arXiv preprint arXiv:1901.10002, 2(8).
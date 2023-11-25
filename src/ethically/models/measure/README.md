# Measuring ethical aspects of data and modelling pipelines


## Representativeness

The idea of representativeness is to ensure that:
- The data is an accurate depiction of the true distribution within the data
- To ensure data equality (equal representation of certain features)
- To ensure data variation (variety of labels, variation within features) (highlighted in Barbedo, 2022)
- To ensure optimal similarity between training, validation and test sets (Schat et al. 2020)
    - Schat et al.'s Data representativeness criterion (DRC) is motivated by KL Divergence (essentially looking at disctance between two probability distributions.). The main principle behind their idea is view data representativeness as an optimisation problem over model performance: identifying an optimal split of the data such that the model has high generalisation, given the data.

The relevance to the modelling step is to assign trust to generalisation performance metric. If the data is too similar to each other, than generalisation performance will be not be deemed trustworthy. If data is too diverse, then generalisation performance of a model will typically suffer.


### Proposed metrics

From OECD.AI Catalogue of Tools & Metrics for Trustworthy AI: https://oecd.ai/en/catalogue/metrics?terms=&page=1
- Conditional Demographic Disparity (CDD): the difference in probabilities of disadvantage sub-group with respect to "positive" and "negative" predictor.
-  

- Dataset divergence:
    - To measure average KL divergence between k train/test splits. 
    We expect that higher average KL divergence between train/test splits would mean greater distances between train/test splits on average (which could lead to poor generalisation performance, BUT higher data variation [which could signal representativeness]).
    Those with smaller average KL divergence will have datasets which are similar to each other (which would make it harder to evaluate generalisation performance, as the datasets are so similar.)
- Single-cluster variation
    - Based on the assumption that all of the data points belong to one single cluster (assuming that the data was representing the same thing)
    Use hierarchical clustering to cluster all entries to a super-single cluster. Evaluate max distance metric to cluster all examples into one cluster and normalise by max possible distance. The higher the value, the greater the variation in data.



## References
Barbedo, J. G. (2022). Deep learning applied to plant pathology: the problem of data representativeness. Tropical Plant Pathology, 47(1), 85-94.
Schat, E., van de Schoot, R., Kouw, W. M., Veen, D., & Mendrik, A. M. (2020). The data representativeness criterion: Predicting the performance of supervised classification based on data set similarity. Plos one, 15(8), e0237009.
https://pair.withgoogle.com/explorables/measuring-diversity/
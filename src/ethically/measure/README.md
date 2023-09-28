# Measuring ethical aspects of data and modelling pipelines


## Representativeness

The idea of representativeness is to ensure that:
- The data is an accurate depiction of the true distribution within the data
- To ensure data equality (equal representation of certain features)
- To ensure data variation (variety of labels, variation within features) (highlighted in Barbedo, 2022)
- To ensure optimal similarity between training, validation and test sets (Schat et al. 2020)
    - Schat et al.'s Data representativeness criterion (DRC) is motivated by KL Divergence (essentially looking at disctance between two probability distributions.). The main principle behind their idea is view data representativeness as an optimisation problem over model performance: identifying an optimal split of the data such that the model has high generalisation, given the data.


## References
Barbedo, J. G. (2022). Deep learning applied to plant pathology: the problem of data representativeness. Tropical Plant Pathology, 47(1), 85-94.
Schat, E., van de Schoot, R., Kouw, W. M., Veen, D., & Mendrik, A. M. (2020). The data representativeness criterion: Predicting the performance of supervised classification based on data set similarity. Plos one, 15(8), e0237009.
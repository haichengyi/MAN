Codes and data for the paper entitled "Learning representations to predict intermolecular interactions on large-scale heterogeneous molecular association network"
### Molecular Association Network：
contains 8 kinds of molecules, 18 types of associations, 14,315 nodes, 114,150 molecular associations.  
![Molecular Association Network](MAN.png)  
The associations among miRNA, mRNA, circRNA, lncRNA, protein, drug, disease, and microbe, including miRNA-disease associations, circRNA-disease associations, circRNA-miRNA associations, disease-mRNA associations, disease-microbe associations, drug-disease interactions, drug-mRNA associations, drug-microbe associations, drug-protein interactions, lncRNA-disease associations, lncRNA-mRNA associations, lncRNA-miRNA associations, lncRNA-protein interactions, miRNA-drug associations, miRNA-mRNA associations, miRNA-protein interactions, mRNA-protein associations, protein-protein interactions. 

### Requirements
```python
openne
numpy==1.14
networkx==2.0
scipy==0.19.1
tensorflow>=1.15.2
gensim==3.0.1
scikit-learn==0.19.0
```
### Citation:
```
Yi et al. Learning Representations to Predict Intermolecular Interactions on Large-Scale Heterogeneous Molecular Association Network. iScience 2020;23(7):101261.
```
Contact: haichengyi#gmail.com

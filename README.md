# Retrosynthesis-Reaction-Pathway

The web application generates complete breakdown pathways for the given product molecule.

The code for data preparation and training the model will be provided in future commits. For inference purpose a checkpoint created after 44000 steps is provided [here](https://drive.google.com/file/d/1qGnw2MLGhgtYaNb_Gn_xUKW_VKPhJt7K/view?usp=sharing).

Also I found [this](https://github.com/kheyer/Retrosynthesis-Prediction) repo a good reference for training the model.

# Installations

1) rdkit
2) OpenNMT

# Running the web app

1) Download the model in the ```Retrosynthesis-Reaction-Pathway``` directory. If you are using a different model then change the model path [here](https://github.com/QuickLearner171998/Retrosynthesis-Reaction-Pathway/blob/ea3ce4627a65a4ecac6f39a9f04606f56bae484a/utils.py#L24).
2) Run ```python app.py``` and vsit the link displayed on the terminal/Command prompt.
3) Enter the correct SMILES in the text box and click on upload.
4) The molecule visualisation and the complete pathway will be shown.

# TODO

- [ ] Improve the frontend.
- [ ] Add option to enter IUPAC name instead of SMILES as input.

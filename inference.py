from utils import *
from urllib.request import urlopen


def predict(mol):

    def iupacToSmiles(name):
        try:
            url = 'http://cactus.nci.nih.gov/chemical/structure/' + name + '/smiles'
            ans = urlopen(url).read().decode('utf8')
            return ans
        except:
            return 'Did not work'

    def smiles_to_IUPAC(smi):
        try:
            url = "https://cactus.nci.nih.gov/chemical/structure/" + smi + "/iupac_name"
            ans = urlopen(url).read().decode('utf8')
            if(len(ans) > 1000):
                return "Name not Available"
            return ans
        except:
            return 'Name Not Available'

    # mol = "N#CC[C@H](O)c1ccccc1"
    molecule = mol[0]
    for c in mol[1:]:
        molecule = molecule + ' ' + c
    # molecule

    # viz moldecule and get its name
    smi = molecule.replace(' ', '')
    m = Chem.MolFromSmiles(smi)

    name = smiles_to_IUPAC(smi)

    # fig = Draw.MolToMPL(m)
    img = Draw.MolToImage(m)
    # imshow(fig)
    # img.save(r"static\molecule.png")
    retro = RetroSynthesis(molecule)

    # run synthesis runs the iterative prediction process
    retro.run_retrosynthesis()

    # display_synthesis displays all predicted reactions
    return name, img, retro.display_synthesis()


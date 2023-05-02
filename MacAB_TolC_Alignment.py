#Assignment 10
#Kali Cook

#Original Structure: PDB ID 5BUN Chain A
#Original Sequence: ENLMQVYQQARLSNPELRKSAADRDAAFEKINEARSPLLPQLGLGADYTYSNGYRDANGINSNETSASLQLTQTLFDMSKWRGLTLQEKAAGIQDVTYQTDQQTLILNTANAYFKVLNAIDVLSYTQAQKEAIYRQLDQTTQRFNVGLVAITDVQNARAQYDTVLANEVTARNNLDNAVEELRQVTGNYYPELASLNVEHFKTDKPKAVNALLKEAENRNLSLLQARLSQDLAREQIRQAQDGHLPTLNLTASTGISDTSYSGSKTNSTQYDDSNMGQNKIGLNFSLPLYQGGMVNSQVKQAQYNFVGASEQLESAHRSVVQTVRSSFNNINASISSINAYKQAVVSAQSSLDAMEAGYSVGTRTIVDVLDATTTLYDAKQQLANARYTYLINQLNIKYALGTLNEQDLLALNSTLGKPIPTSPESVAPETPDQDAAADGYNAHSAAPAVQPTAARANSNNGNPFRH

#Molecular Modeling and Proteomics
#Group 3 
#Kali C., Serena T., and Brian Y.

#This Script:
# Fetches solved structure of the solved MacAB-TolC efflux pump in E. coli
# Aligns the 3 MacAB-TolC efflux pump proteins to the solved structure
# for the A. baumannii (Purple) and S. enteritidis (Blue) Swiss-Model predicted structures

####USER INPUT
####You will have to change manually change the file path of the predicted structures
####to match your local folder

# import chimera commands
from chimerax.core.commands import run

# fetch original PDB structure
run(session, "open 5NIK")

# Make cartoon, not surface depiction 
run(session, "hide atoms")
run(session, "show cartoon")

# adjust View
run(session, "turn y 90")
run(session, "view /B-K")

# open predicted structures - hardcoded
###User manually enters file path
###Be sure to keep order the same
#A. baumannii MacA
run(session, "open C:/Users/Kali/Documents/GitHub/Efflux Pumps/Swiss_MacA_AB/MACA_AB_SWISS/models/01/templates/5ws4.1.A.pdb")
#A. baumannii MacB
run(session, "open C:/Users/Kali/Documents/GitHub/Efflux Pumps/Swiss_MacB_AB/MACB_AB_SWISS/models/01/templates/5ws4.1.A.pdb")
#A. baumanniiTolC
run(session, "open C:/Users/Kali/Documents/GitHub/Efflux Pumps/Swiss_TolC_AB/TOLC_AB_SWISS/models/01/templates/5bun.1.A.pdb")
#S. enteritidis MacA
run(session, "open C:/Users/Kali/Documents/GitHub/Efflux Pumps/Swiss_MacA_SE/MACA_SE_SWISS/models/02/templates/2v4d.1.A.pdb")
#S. enteritidis MacB
run(session, "open C:/Users/Kali/Documents/GitHub/Efflux Pumps/Swiss_MacB_SE/MACB_SE_SWISS/models/01/templates/5ws4.1.A.pdb")
#S. enteritidis TolC
run(session, "open C:/Users/Kali/Documents/GitHub/Efflux Pumps/Swiss_TolC_SE/TOLC_SE_SWISS/models/01/templates/5bun.1.A.pdb")

# make proteins different colors
run(session, "color #2-4 purple") #A. baumannii
run(session, "color #5-7 blue") #S. enteritidis

# matchmaker alignments
run(session, "match #2-7 to #1")
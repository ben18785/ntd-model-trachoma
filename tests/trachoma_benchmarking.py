from trachoma.trachoma_simulations import Trachoma_Simulation

BetFilePath = 'files/InputBet_single_sim.csv'  
MDAFilePath = 'files/InputMDA_scen1.csv' 
PrevFilePath = 'files/OutputPrev_scena1.csv'
InfectFilePath = 'files/Infect.csv'

Trachoma_Simulation(BetFilePath=BetFilePath,
                MDAFilePath=MDAFilePath,
                PrevFilePath=PrevFilePath,
                SaveOutput=False,
                OutSimFilePath=None,
                InSimFilePath=None,
                InfectFilePath=InfectFilePath)

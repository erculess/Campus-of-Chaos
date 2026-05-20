from personagens import Onze, Hopper, Eddie, Max
from inimigos import Vecna, Demobat

if __name__ == "__main__":
    print("\n" + "="*40)
    print(" INÍCIO DA FASE: INVASÃO AO MUNDO INVERTIDO ")
    print("="*40 + "\n")

    onze = Onze()
    hopper = Hopper()
    eddie = Eddie()
    max_m = Max()

    vecna = Vecna()
    demobat1 = Demobat()
    demobat2 = Demobat()

    vecna.atacar(max_m)
    demobat1.atacar(hopper)
    
    print("\n--- TURNO DOS HERÓIS ---")
    
    max_m.curar_aliado(max_m)
    eddie.solo_guitarra()     
    hopper.atacar_soco(demobat1) 
    onze.ataque_mental(vecna)    
    
    print("\n" + "="*40)


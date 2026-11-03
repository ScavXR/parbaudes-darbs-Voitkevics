# ----------------------------------------------------------------------
# C1. Python — rīks, kas atlasa un saglabā
# ----------------------------------------------------------------------

# Uzraksti skriptu, kuram līmeni padod kā argumentu komandrindā. Skripts izvada, cik tāda līmeņa rindu žurnālā ir, un saglabā visas šīs rindas failā, kura nosaukums sākas ar līmeņa nosaukumu. Ja arguments nav padots, skripts izvada pamācību un neavarē.
#
# Šis fails ir tukšs. Visu kodu raksti pats zem šīs rindas.
# ----------------------------------------------------------------------                                                                                                


import sys

if len(sys.argv) < 2:
    print("Uzraksti līmeni!")
    print("Raksti python "sava faila nosaukumu" ERROR")
else:
    limenis = sys.argv[1]
    atlasitas_rindas = []
    rindu_skaits = 0
    
    with open("sistema.log", "r", encoding="utf-8") as fails:
        for rinda in fails:
            if limenis in rinda:
                atlasitas_rindas.append(rinda)
                rindu_skaits = rindu_skaits + 1
    
    print("Atrastas", rindu_skaits, "rindas ar līmeni", limenis)
    jaunais_fails = limenis + "_sistema.log"    
    if rindu_skaits > 0:
        with open(jaunais_fails, "w", encoding="utf-8") as izvade:
            for rinda in atlasitas_rindas:
                izvade.write(rinda)
        print("Viss saglabāts failā:", jaunais_fails)

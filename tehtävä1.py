import json
import os

TIEDOSTO = "dictionary.json"

OLETUSSANASTO = {
  "hello": "terve",
  "clock": "kello",
  "dog": "koira",
  "monday": "maanantai",
  "human": "ihminen"
}

class Sanakirja:
    def __init__(self, tiedosto, oletus):
        self.tiedosto = tiedosto
        self.oletus = oletus
        self.sanasto = self.lataa()

    def lataa(self):
        if not os.path.isfile(self.tiedosto):
            print("Sanastotiedostoa ei löytynyt. Käytetään oletussanastoa.")
            return self.oletus.copy()
        try:
            with open(self.tiedosto, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"Virhe sanaston latauksessa: {e}. Käytetään oletussanastoa.")
            return self.oletus.copy()

    def tallenna(self):
        try:
            with open(self.tiedosto, "w", encoding="utf-8") as f:
                json.dump(self.sanasto, f, ensure_ascii=False, indent=2)
            print("Sanasto tallennettu onnistuneesti.")
        except Exception as e:
            print(f"Sanaston tallennus epäonnistui: {e}")

    def hae_kaannos(self, sana):
        return self.sanasto.get(sana)

    def lisaa_sana(self, sana, maaritelma):
        self.sanasto[sana] = maaritelma

def paavalikko():
    sanakirja = Sanakirja(TIEDOSTO, OLETUSSANASTO)
    print("Yksinkertainen sanakirjasovellus. Tyhjä syöte lopettaa.")

    while True:
        sana = input("\nAnna käännettävä sana: ").strip().lower()
        if not sana:
            break
        kaannos = sanakirja.hae_kaannos(sana)
        if kaannos:
            print(f"Käännös: {kaannos}")
        else:
            print("Sanaa ei löytynyt.")
            maaritelma = input("Anna määritelmä (tai jätä tyhjäksi ohittaaksesi): ").strip()
            if maaritelma:
                sanakirja.lisaa_sana(sana, maaritelma)
                print(f"Lisättiin '{sana}': '{maaritelma}' sanastoon.")
            else:
                print("Ei määritelmää annettu. Sanaa ei lisätty.")

    sanakirja.tallenna()
    print("NÄKEMIIN")

if __name__ == "__main__":
    paavalikko()
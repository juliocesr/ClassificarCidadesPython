import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
if __name__ == '__main__':
    def clasificarZonaPorCidade(cidade):
        geolocator = Nominatim(user_agent="Zonas")
        try:
            location = geolocator.geocode(cidade + ", São Paulo, Brasil")
            if location:
                lat, lon = location.latitude, location.longitude

                if lat < -23.52 and lon > -46.50:
                    return "Zona Sul"
                elif lat < -23.50 and lon < -46.40:
                    return "Zona Leste"
                elif lat > -23.40 and lon > -46.50:
                    return "Zona Norte"
                elif lat > -23.40 and lon < -46.65:
                    return "Zona Oeste"
                elif -23.52 <= lat <= -23.50 and -46.65 <= lon <= -46.50:
                    return "Centro"
                else:
                    return "Não encontrado"
            else:
                return "Não encontrado"
        except GeocoderTimedOut:
            return "Timeout"

    df = pd.read_excel("Lista_cidades_SP.xlsx", engine="openpyxl")
    df["Zona"] = df["Cidade"].apply(clasificarZonaPorCidade)
    df.to_excel("cidades_classificadas.xlsx", index=False, engine="openpyxl")
    for zona in df["Zona"].unique():
        if zona != "Não encontrado" and zona != "Timeout":
            df_zona = df[df["Zona"] == zona]
            df_zona.to_excel(f"cidades_{zona.lower().replace(' ', '_')}.xlsx", index=False, engine="openpyxl")
    print("Processamento concluído. Arquivos gerados!")

# Este código realiza o seguinte:
* Geocodificação: Recebe o nome da cidade e usa a API Nominatim da biblioteca Geopy para converter o nome da cidade em coordenadas geográficas (latitude e longitude).
* Classificação: Com base nas coordenadas obtidas, o código classifica a cidade em uma das zonas de São Paulo.
* Geração de Relatórios: Depois de classificar as cidades, o código gera automaticamente arquivos Excel, dividindo as cidades por zona.
# Resultados:
Geração de um arquivo cidades_classificadas.xlsx com a classificação de cada cidade.
Criação de arquivos separados por zona, como cidades_zona_sul.xlsx, cidades_zona_leste.xlsx, e assim por diante.
# Tecnologias utilizadas:
* Python
* Pandas
* Geopy (Geocodificação)
* Excel (para salvar os resultados)

"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    #print(len(df))
    df.dropna(inplace=True)
    #sexo
    df["sexo"] = df["sexo"].apply(lambda x: str(x).lower())
    # print(df["sexo"].unique())

    #tipo_de_emprendimiento
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].apply(lambda x: str(x).lower())
    #print(df["tipo_de_emprendimiento"].unique())
    #idea_negocio
    df["idea_negocio"] = df["idea_negocio"].apply(lambda x: str(x).lower().replace("-"," ").replace("_"," ").strip())
    #print(len(df["idea_negocio"].unique()))
    #115
    #99
    #75
    #barrio
    df["barrio"] = df["barrio"].apply(lambda x: str(x).lower().replace("_"," ").replace("¿","ñ").replace("-"," ").strip().replace("20","veinte"))
    print(len(df["barrio"].unique()))
    #415
    #281
    #255
    #221 xxx 234

    #estrato
    #df["estrato"] = df["estrato"]
    print(len(df["estrato"].unique()))

    #comuna_ciudadano
    df["comuna_ciudadano"] = df["comuna_ciudadano"].apply(lambda x: int(x))
    print(len(df["comuna_ciudadano"].unique()))

    #fecha_de_beneficio
    df["fecha_de_beneficio"] = df["fecha_de_beneficio"]
    print((df["fecha_de_beneficio"].unique()))


    df.drop_duplicates(inplace=True)
    #
    # Inserte su código aquí
    #print(len(df))


    #print(df["sexo"].unique())

    return df
(clean_data())
#11145
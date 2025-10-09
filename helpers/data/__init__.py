import json
from models.InstituicaoEnsino import InstituicaoEnsino


def getInstituicoesEnsino():

    instituicoesEnsino = []

    # IE no formato JSON lido do arquivo.
    with open('data/instituicoesensino.json', 'r') as f:
        instituicoesEnsinoJson = json.load(f)

    # Conversão para o objeto de InstituicaoEnsino.
    for instituicaoEnsinoJson in instituicoesEnsinoJson:
        ie = InstituicaoEnsino(instituicaoEnsinoJson["codigo"],
                               instituicaoEnsinoJson["nome"],
                               instituicaoEnsinoJson["co_uf"],
                               instituicaoEnsinoJson["co_municipio"],
                               instituicaoEnsinoJson["qt_mat_bas"],
                               instituicaoEnsinoJson["qt_mat_prof"],
                               0,
                               instituicaoEnsinoJson["qt_mat_esp"])
        instituicoesEnsino.append(ie)

    return instituicoesEnsino


getInstituicoesEnsino()

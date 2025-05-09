from dataclasses import dataclass
from enum import Enum
from typing import Dict, List


@dataclass
class TermoBase:
    coreano: str
    portugues: str
    descricao: str = ""

    def __str__(self) -> str:
        return f"{self.coreano} ({self.portugues})"


class TermoEnumMixin:
    """Mixin para adicionar funcionalidade comum a todas as enumerações de termos."""

    @classmethod
    def listar_todos(cls) -> List[Dict[str, str]]:
        """Retorna uma lista de dicionários com todos os termos."""
        return [
            {
                "coreano": termo.value.coreano,
                "portugues": termo.value.portugues,
                "descricao": termo.value.descricao,
            }
            for termo in cls
        ]


class Bases(TermoEnumMixin, Enum):
    APGUBI = TermoBase(
        "Apgubi",
        "Base frontal",
        "Pernas afastadas, com a frente dobrada e peso à frente",
    )
    DWITGUBI = TermoBase(
        "Dwitgubi",
        "Base para trás",
        "Peso do corpo principalmente na perna de trás, postura recuada",
    )
    JUCHUM_SEOGI = TermoBase(
        "Juchum Seogi",
        "Posição de cavaleiro",
        "Posição com as pernas abertas e joelhos flexionados",
    )
    NARANI_SEOGI = TermoBase(
        "Narani Seogi",
        "Base paralela",
        "Pés alinhados paralelamente à largura dos ombros",
    )
    MOA_SEOGI = TermoBase(
        "Moa Seogi",
        "Base fechada",
        "Pés juntos, tocando um no outro",
    )
    BEOM_SEOGI = TermoBase(
        "Beom Seogi",
        "Base de tigre",
        "Peso do corpo quase todo na perna de trás, frente levemente apoiada",
    )
    KKOA_SEOGI = TermoBase(
        "Kkoa Seogi",
        "Base cruzada",
        "Uma perna cruza sobre a outra, pés próximos",
    )
    DWIT_KKOA_SEOGI = TermoBase(
        "Dwit Kkoa Seogi",
        "Base cruzada para trás",
        "Uma perna cruza sobre a outra, pés próximos, com a perna de trás apoiada no chão",
    )
    AP_KKOA_SEOGI = TermoBase(
        "Ap Kkoa Seogi",
        "Base cruzada para frente",
        "Uma perna cruza sobre a outra, pés próximos, com a perna de frente apoiada no chão",
    )
    HAKDARI_SEOGI = TermoBase(
        "Hakdari Seogi",
        "Base da garça",
        "Equilíbrio sobre uma perna, outra perna flexionada com a ponta do pé encostando no joelho",
    )
    YEOP_SEOGI = TermoBase(
        "Yeop Seogi",
        "Posição lateral",
        "Postura onde o praticante posiciona o corpo de lado em relação ao adversário, usada para maximizar o alcance e a força em chutes laterais como o Yeop Chagi.",
    )


class Acoes(TermoEnumMixin, Enum):
    CHAGI = TermoBase(
        "Chagi",
        "Chute",
        "Movimento de ataque usando a perna ou o pé",
    )
    MAKGI = TermoBase(
        "Makgi",
        "Bloqueio",
        "Ação defensiva para interceptar um ataque",
    )
    CHIGI = TermoBase(
        "Chigi",
        "Bater",
        "Movimento de ataque usando mãos, braços ou cotovelos de forma lateral ou circular",
    )
    JIREUGI = TermoBase(
        "Jireugi",
        "Soco",
        "Ataque direto e reto com o punho fechado",
    )
    JJIREUGI = TermoBase(
        "Jjireugi",
        "Perfuração",
        "Ataque de perfuração, geralmente com ponta dos dedos ou mão em lança",
    )
    DANGGYEO = TermoBase(
        "Danggyeo",
        "Puxar",
        "Ação de puxar o adversário, usada em técnicas de controle ou defesa",
    )
    JITJJIKI = TermoBase(
        "Jitjjiki",
        "Esmagar",
        "Ação de ataque que pressiona ou esmaga, geralmente com o pé ou mão",
    )


class Direcoes(TermoEnumMixin, Enum):
    OLLYEO = TermoBase("Ollyeo", "Para cima", "Direção para cima")
    NAERYEO = TermoBase("Naeryeo", "Para baixo", "Direção para baixo")
    AP = TermoBase("Ap", "Frente", "Direção para frente")
    DWIT = TermoBase("Dwit", "Trás", "Direção para trás")
    YEOP = TermoBase("Yeop", "Lado", "Direção para o lado")


class PartesCorpo(TermoEnumMixin, Enum):
    PALMOK = TermoBase(
        "Palmok",
        "Antebraço",
        "Parte do antebraço usada para bloqueios e defesas",
    )
    JUMEOK = TermoBase(
        "Jumeok",
        "Punho",
        "Mão fechada usada para socos",
    )
    DUJUMEOK = TermoBase(
        "Dujumeok",
        "Punho duplo",
        "Punho com as duas mãos fechadas, usado para socos duplos",
    )
    SONNAL = TermoBase(
        "Sonnal",
        "Faca da mão",
        "Borda externa da mão aberta usada para ataques e defesas",
    )
    SONKUT = TermoBase(
        "Sonkut",
        "Ponta dos dedos",
        "Ponta dos dedos usada para ataques de perfuração",
    )
    PALGUP = TermoBase(
        "Palgup",
        "Cotovelo",
        "Usado para ataques de curta distância",
    )
    MUREUP = TermoBase(
        "Mureup",
        "Joelho",
        "Usado para ataques em curta distância com a perna",
    )
    MOMTONG = TermoBase(
        "Momtong",
        "Tronco",
        "Região do torso usada como área-alvo ou para suportar técnicas",
    )
    EOLGUL = TermoBase(
        "Eolgul",
        "Rosto",
        "Região do rosto, alvo de ataques e área a ser protegida em bloqueios altos.",
    )


class TiposMovimento(TermoEnumMixin, Enum):
    DOLLYEO = TermoBase(
        "Dollyeo",
        "Girar",
        "Movimento circular ou rotatório",
    )
    HURRYEO = TermoBase(
        "Huryeo",
        "Chicoteado",
        "Movimento rápido e curvado como um chicote",
    )
    BITEUREO = TermoBase(
        "Biteureo",
        "Torcido",
        "Movimento de ataque com torção",
    )
    NULLEO = TermoBase(
        "Nulleo",
        "Empurrado para baixo",
        "Movimento descendente puxando ou empurrando",
    )
    JEOCHEO = TermoBase(
        "Jeocheo",
        "Empurrado para cima",
        "Movimento ascendente de empurrar para cima",
    )
    HECHEO = TermoBase(
        "Hecheo",
        "Separar",
        "Movimento de abrir ou separar",
    )
    GEODEUP = TermoBase(
        "Geodeup",
        "Repetido",
        "Movimento duplo ou repetido",
    )
    SANTEUL = TermoBase(
        "Santeul",
        "Montanha",
        "Movimento em arco elevado como uma montanha",
    )
    GEODEUREO = TermoBase(
        "Geodeureo",
        "Assistido",
        "Usado para indicar que uma técnica é assistida ou reforçada por outra mão, como em Geodeureo Makgi (bloqueio assistido).",
    )
    MODUM = TermoBase(
        "Modum",
        "Unido",
        "Usado em posturas ou movimentos onde as pernas ou mãos estão unidas, como em Modum Seogi (posição com pés juntos).",
    )
    GEUMGANG = TermoBase(
        "Geumgang",
        "Diamante / Forte como diamante",
        "Nome de um Poomsae avançado (2º Dan) e conceito que representa força inquebrável, estabilidade e grandeza.",
    )
    JASUMBAL = TermoBase(
        "Jasumbal",
        "Perna da frente",
        "Indica que a técnica é executada com a perna da frente, sem troca de base.",
    )
    BALBUCHEO = TermoBase(
        "Balbucheo",
        "Chute com avanço",
        "Movimento em que o praticante avança com a perna de trás enquanto executa o chute com a perna da frente, ganhando impulso e cobrindo distância.",
    )
    MOMDORA = TermoBase(
        "Momdora",
        "Rotação do corpo",
        "Indica que a técnica envolve uma rotação do tronco ou do corpo para gerar mais força ou mudar de direção.",
    )
    DWIDORA = TermoBase(
        "Dwidora",
        "Giro reverso",
        "Rotação completa para trás usada para gerar força em técnicas como chutes giratórios ou ataques surpresa.",
    )
    JEPIPUM = TermoBase(
        "Jepipum",
        "Técnica da andorinha",
        "Movimento estilizado, frequentemente usado em formas (poomsae) ou demonstrações",
    )
    TTWIEO = TermoBase(
        "Ttwieo",
        "Saltar",
        "Modificador que indica a execução de um movimento com salto, como em Ttwieo Chagi",
    )
    SEWO = TermoBase(
        "Sewo",
        "Vertical",
        "Indica que a técnica é realizada em direção vertical, geralmente de cima para baixo.",
    )
    EOPEO = TermoBase(
        "Eopeo",
        "Horizontal",
        "Indica que a técnica é realizada na direção horizontal, geralmente paralela ao chão.",
    )
    BAL_BAKUDA = TermoBase(
        "Bal Bakuda",
        "Trocar o pé",
        "Ação de alternar a perna da frente com a de trás, trocando a base",
    )
    DOLGAE = TermoBase(
        "Dolgae",
        "Redemoinho",
        "Movimento giratório contínuo, usado em treinos acrobáticos ou para descrever giros intensos",
    )
    GAWI = TermoBase(
        "Gawi",
        "Tesoura",
        "Movimento com membros em oposição, semelhante ao fechamento de uma tesoura",
    )


class ModificadoresDirecao(TermoEnumMixin, Enum):
    BAKKAT = TermoBase(
        "Bakkat",
        "Externo",
        "Indica movimento de fora para dentro",
    )
    AN = TermoBase(
        "An",
        "Interno",
        "Indica movimento de dentro para fora",
    )
    OESANTEUL = TermoBase(
        "Oesanteul",
        "Arco externo",
        "Movimento em forma de arco para fora",
    )
    MOM_DORA = TermoBase(
        "Mom Dora",
        "Vire o corpo",
        "Comando usado para girar o corpo, geralmente 180°, em treinos e poomsae",
    )
    DWIT_DORA = TermoBase(
        "Dwit Dora",
        "Vire-se para trás",
        "Comando para girar o corpo 180° para trás no lugar",
    )


class PartesMao(TermoEnumMixin, Enum):
    BATANSON = TermoBase(
        "Batanson",
        "Palma da mão",
        "Centro da mão usado para bloqueios e ataques",
    )
    PYEONSON = TermoBase(
        "Pyeonson",
        "Mão estendida",
        "Mão com dedos abertos e estendidos",
    )
    SONNAL = TermoBase(
        "Sonnal",
        "Faca da mão",
        "Borda externa da mão (lado do dedo mínimo) usada para golpes cortantes",
    )
    SONKKEUT = TermoBase(
        "Sonkkeut",
        "Pontas dos dedos",
        "Pontas dos dedos usadas para ataques de perfuração (tipo 'spearfinger')",
    )
    DEUNGJUMEOK = TermoBase(
        "Deungjumeok",
        "Costas do punho",
        "Parte superior do punho usada em bloqueios e ataques (ex: Deungjumeok Ap Chigi)",
    )
    MEJUMEOK = TermoBase(
        "Mejumeok",
        "Base do punho",
        "Parte inferior do punho, usada como martelo em golpes para baixo (Mejumeok Naeryo Chigi)",
    )
    SONBADAK = TermoBase(
        "Sonbadak",
        "Sola da mão",
        "A parte interna da mão, como a palma usada para empurrar (semelhante a Batanson mas mais geral)",
    )
    AGEUMSON = TermoBase(
        "Ageumson",
        "Mão em arco (Arc Hand)",
        "Forma técnica onde a mão está aberta, com o polegar e o dedo indicador afastados e os demais dedos levemente curvados para dentro, formando um arco ou meia-lua. Utilizado em ataques perfurantes e técnicas específicas de bloqueio.",
    )
    DEUNG = TermoBase(
        "Deung",
        "Costas",
        "Geralmente se refere à parte traseira da mão ou punho, como em Deungjumeok (costas do punho).",
    )
    DEUNGPALMOK = TermoBase(
        "Deungpalmok",
        "Costas do pulso",
        "Parte superior do pulso utilizada em certas técnicas de bloqueio ou ataque. Corresponde à superfície traseira do punho quando um soco é desferido.",
    )
    PYEONJUMEOK = TermoBase(
        "Pyeonjumeok",
        "Punho semi-serrado",
        "Área da segunda falange (articulação média) dos dedos, usada quando os nós dos dedos são estendidos ou achatados em relação à forma de um punho fechado. Também chamado de 'Half-clenched Fist'.",
    )
    PYEONSONKKEUT = TermoBase(
        "Pyeonsonkkeut",
        "Pontas dos dedos achatadas",
        "Técnica em que a ponta do dedo médio é levemente curvada para alinhar-se com os dedos indicador e anelar, com todos os dedos pressionados juntos. Também conhecida como 'Flat Fingertips'.",
    )


class PartesPe(TermoEnumMixin, Enum):
    BALDEUNG = TermoBase(
        "Baldeung",
        "Empeine do pé",
        "Parte superior do pé usada para chutar (por exemplo, Dollyeo Chagi)",
    )
    BALBADAK = TermoBase(
        "Balbadak",
        "Sola do pé",
        "Parte inferior do pé usada para empurrões ou chutes frontais (Push Kick)",
    )
    BALNAL = TermoBase(
        "Balnal",
        "Faca do pé",
        "Borda externa do pé usada em chutes laterais (Yop Chagi)",
    )
    BALNALDEUNG = TermoBase(
        "Balnaldeung",
        "Faca interna do pé",
        "Borda interna do pé usada em técnicas específicas de corte",
    )
    APCHUK = TermoBase(
        "Apchuk",
        "Bola do pé",
        "Parte frontal do pé (parte logo abaixo dos dedos) usada em chutes frontais (Ap Chagi)",
    )
    DWICHUK = TermoBase(
        "Dwichuk",
        "Calcanhar",
        "Parte traseira do pé, usada em chutes para trás (Dwi Chagi)",
    )


class TiposChute(TermoEnumMixin, Enum):
    APBAL = TermoBase(
        "Apbal",
        "Pé da frente",
        "Uso do pé da frente para executar um chute, geralmente mais rápido e para ataques rápidos de curta distância.",
    )
    DWITBAL = TermoBase(
        "Dwitbal",
        "Pé de trás",
        "Uso do pé de trás para executar o chute, normalmente mais potente e com maior alcance.",
    )
    BALBUCHEO = TermoBase(
        "Balbucheo",
        "Impulsionar o pé",
        "Movimento de impulso rápido com o pé, usado para aumentar a velocidade e força do chute, aproveitando o balanço do corpo.",
    )
    MIREO = TermoBase(
        "Mireo",
        "Empurrar",
        "Movimento de empurrar com a perna, utilizado para chutes como o Mireo Chagi, focando em afastar o adversário com a sola do pé.",
    )
    DUBALDANGSANG = TermoBase(
        "Dubaldangsang",
        "Dois pés simultâneos",
        "Uso simultâneo dos dois pés em saltos ou chutes, como em técnicas de chute duplo (por exemplo, Dubaldangsang Twio Chagi).",
    )
    GORO = TermoBase(
        "Goro",
        "Arrastar/Rastejar",
        "Movimento de arrastar o pé no chão durante a execução do chute, usado para criar impulso ou disfarçar a preparação do golpe.",
    )
    DUBAL = TermoBase(
        "Dubal",
        "Dois pés",
        "Indica o uso de ambos os pés simultaneamente em uma técnica, como em Dubal Ddangseong Chagi (chute com os dois pés).",
    )


class TecnicasDeBloqueio(TermoEnumMixin, Enum):
    EOTGEOREO = TermoBase(
        "Eotgeoreo",
        "Cruzado",
        "Movimento onde os braços se cruzam para bloquear ataques, aumentando a força e a cobertura da defesa.",
    )

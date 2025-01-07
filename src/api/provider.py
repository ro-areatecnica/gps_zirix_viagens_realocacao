import logging
from enum import Enum
from api.client import APIClient
from config import (
    URL, API_KEY, ENDPOINT_REALOCACAO, TIMEOUT_IN_SECONDS, RETRIES
)

logger = logging.getLogger(__name__)


class ProviderEnum(Enum):
    """Classe de enumeração para encapsular parâmetro de provedores de serviço de GPS
    """

    ZIRIX = "zirix"


class Provider(APIClient):
    """Classe que encapsula os métodos de requisição de dados da API,
    agnóstico em relação ao provedor.
    """

    def __init__(self, provider):
        """Construtor da classe Provider

        Args:
            - provider (ProviderEnum): Enum do provedor de serviços.
        """
        self.provider_name = provider
        self.url = URL
        self.api_key = API_KEY
        self.realocacao = ENDPOINT_REALOCACAO
        super().__init__(base_url=self.url, api_key=self.api_key,
                         timeout=TIMEOUT_IN_SECONDS, retries=RETRIES)

    def get_realocacao(self, data_hora_inicio, data_hora_fim):
        """Método que recupera as realocações de linhas

        Args:
            data_hora_inicio (str): Timestamp de início da captura dos dados. (formato YYYY-MM-DD HH:mm:SS)
            data_hora_fim (str): Timestamp de fim da captura dos dados. (formato YYYY-MM-DD HH:mm:SS)

        Returns:
            list: Lista dos registros de realocações no período especificado
        """

        params = {
            "guidIdentificacao": self.api_key,
            "dataInicial": data_hora_inicio,
            "dataFinal": data_hora_fim
        }

        response = self.get(endpoint=self.realocacao, params=params)

        print(f"Total de registros retornados da API do enpoint REALOCACAO: {len(response)}")

        return response
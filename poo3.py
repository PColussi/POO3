class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel) -> None:
        self._tipo_combustivel = tipo_combustivel
        self._valor_litro = valor_litro
        self._quantidade_combustivel = quantidade_combustivel

    @property
    def tipo_combustivel(self):
        return self._tipo_combustivel
    
    @tipo_combustivel.setter
    def tipo_combustivel(self, novo_tipo_combustivel):
        self._tipo_combustivel = novo_tipo_combustivel
        return f"Tipo de combustível alterado para {novo_tipo_combustivel}"
    

    @property
    def valor_litro(self):
        return self._valor_litro
    
    @valor_litro.setter
    def valor_litro(self, novo_valor_litro):
        self._valor_litro = novo_valor_litro
        return f"Valor do litro alterado para R${novo_valor_litro:.2f}"

    @property
    def quantidade_combustivel(self):
        return self._quantidade_combustivel
    
    @quantidade_combustivel.setter
    def quantidade_combustivel(self, nova_quantidade_combustivel):
        self._quantidade_combustivel = nova_quantidade_combustivel
        return f"Quantidade de combustível na bomba alterada para {nova_quantidade_combustivel:.2f}"
        
    
    def abastecer_por_valor(self,valor_abastecer):
        litro_abastecido = valor_abastecer / self._valor_litro
        if litro_abastecido <= self._quantidade_combustivel:
            self._quantidade_combustivel -= litro_abastecido
            return f"Valor abastecido: {valor_abastecer:.2f}. Litros abastecidos: {litro_abastecido}"
        else:
            return "Não há combustível suficiente."

    def abastecer_por_litro(self, litros_abastecidos):
        valor_pagar = litros_abastecidos * self._valor_litro
        if litros_abastecidos <= self._quantidade_combustivel:
            self._quantidade_combustivel -= litros_abastecidos
            return f"Abastecidos: {litros_abastecidos}. Valor a pagar: R${valor_pagar}"
        else:
            return "Não há combustível suficiente."
    
    def alterar_valor(self, novo_valor):
        self._valor_litro = novo_valor
        return f"Valor do litro alterado para R${novo_valor:.2f}"

    def alterar_combustivel(self, novo_combustivel):
        self._tipo_combustivel = novo_combustivel
        return f"Tipo de combustível alterado para {novo_combustivel}"

    def alterar_quantidade_combustivel(self, nova_quantidade):
        self._quantidade_combustivel = nova_quantidade
        return f"Quantidade de combustível na bomba alterada para {nova_quantidade:.2f}"



class Bomba_alcool(BombaCombustivel):
    def __init__(self, quantidade_combustivel) -> None:
        super().__init__("Álcool", 4.00, quantidade_combustivel)


class Bomba_gasolina(BombaCombustivel):
    def __init__(self, quantidade_combustivel) -> None:
        super().__init__("Gasolina", 5.30, quantidade_combustivel)



bomba_alcool = Bomba_alcool(1000)
bomba_gasolina = Bomba_gasolina(2000)
print(bomba_alcool.quantidade_combustivel)
bomba_alcool.abastecer_por_litro(10)
print(bomba_alcool.quantidade_combustivel)





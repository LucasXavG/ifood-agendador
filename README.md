Este projeto é um script em Python que automatiza o processo de agendamento de horários no painel do entregador do iFood.  
Com uso de Selenium e técnicas de carregamento rápido, o tempo de execução foi reduzido de **cerca de 20 segundos para apenas 1 a 3 segundos**!

---

##  Funcionalidades

- Login automático no sistema do iFood
- Clicagem automática no botão **"Solicitar Agenda"**
- Busca ultra rápida por horários da unidade **DOM PEDRO**
- Seleção dos horários disponíveis
- Marcação do termo de compromisso
- Envio do agendamento

---

##  Requisitos

- Python 3.7+
- [Selenium](https://pypi.org/project/selenium/)
- [webdriver-manager](https://pypi.org/project/webdriver-manager/)

---

##  Instalação

```bash
pip install selenium webdriver-manager
```

---

##  Como usar

1. Altere o script com suas credenciais do iFood:
   ```python
   driver.find_element(By.ID, "Email").send_keys("SEU_EMAIL")
   driver.find_element(By.ID, "Senha").send_keys("SUA_SENHA")
   ```

2. Execute o script:
   ```bash
   python automate_ifood_scheduling.py
   ```

3. O script irá:
   - Fazer login automaticamente
   - Procurar a praça DOM PEDRO (ou outra que você definir)
   - Selecionar todos os horários disponíveis
   - Confirmar o agendamento rapidamente

---

## Alterar a praça desejada

O script procura pela praça DOM PEDRO, que é identificada pelo ID `1312-selectZona`.  
Se quiser usar outra praça, basta **trocar esse valor** por outro ID no trecho:

```python
dom_pedro_button = WebDriverWait(driver, 0.1).until(
    EC.element_to_be_clickable((By.ID, "1312-selectZona"))
)
```

> Para descobrir o ID da sua praça, você pode inspecionar o botão correspondente no navegador.

---

## Observações

- O tempo de execução foi otimizado:  
  O que antes demorava **20 segundos ou mais**, agora é feito em **1 a 3 segundos**, graças ao carregamento instantâneo e lógica de tentativa direta.
- O script pode ser adaptado para outras regiões ou fluxos de agendamento.
- Tenha responsabilidade ao usar automações: o uso excessivo pode violar os termos de uso da plataforma.

---

## Licença

Uso pessoal e educacional. Sem garantias. Modifique com responsabilidade.

---

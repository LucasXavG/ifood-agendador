from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    driver.get("https://agenda.dn.app.br/Entregador")
    print("Página carregada.")

    # Login 
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "Email")))
    driver.find_element(By.ID, "Email").send_keys("MEU E-MAIL")
    driver.find_element(By.ID, "Senha").send_keys("MINHA SENHA")
    driver.find_element(By.XPATH, "//button[text()='Entrar']").click()
    print("Login enviado.")

    # Clicar em Solicitar Agenda
    planning_menu = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/Entregador/Agendamentos/Criar') and contains(., 'Solicitar Agenda')]"))
    )
    # Scroll 
    driver.execute_script("arguments[0].scrollIntoView(true);", planning_menu)
    driver.execute_script("arguments[0].click();", planning_menu)
    print("Botão 'Solicitar Agenda' clicado!")

    # LOOP
    dom_pedro_encontrada = False
    tentativas = 0
    
    while not dom_pedro_encontrada:
        tentativas += 1
        try:
            # Tentar encontrar DOM PEDRO (INSTANTÂNEO - 0.1 segundo)
            dom_pedro_button = WebDriverWait(driver, 0.1).until(
                EC.element_to_be_clickable((By.ID, "1312-selectZona"))
            )
            dom_pedro_button.click()
            print(f"🎯 DOM PEDRO ENCONTRADA na tentativa {tentativas}!")
            dom_pedro_encontrada = True
            
        except:
            print(f"🤖 Tentativa {tentativas}: DOM PEDRO não FOI, recarregando INSTANTÂNEO...")
            driver.refresh()
            
            # Aguardar página carregar INSTANTÂNEO e clicar novamente em Solicitar Agenda
            try:
                planning_menu = WebDriverWait(driver, 0.1).until(
                    EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/Entregador/Agendamentos/Criar') and contains(., 'Solicitar Agenda')]"))
                )
                driver.execute_script("arguments[0].click();", planning_menu)
            except:
                # Se não conseguir em 0.1s, tenta sem scroll para ser mais rápido
                try:
                    planning_menu = driver.find_element(By.XPATH, "//a[contains(@href, '/Entregador/Agendamentos/Criar') and contains(., 'Solicitar Agenda')]")
                    driver.execute_script("arguments[0].click();", planning_menu)
                except:
                    continue
    
    # AGUARDAR O MINIMO
    WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((By.ID, "divPeriodos"))
    )
    print("HORARIOS DOM PEDRO !")
    
    # SELECIONE TUDO
    horarios_clicados = 0
    for i in range(20):
        try:
            # VERIFICAR SE EXISTE
            driver.find_element(By.ID, f"Periodos[{i}]_Selecionado")
            
            # CLICAR LABEL
            label_horario = driver.find_element(By.CSS_SELECTOR, f"label[for='Periodos[{i}]_Selecionado']")
            driver.execute_script("arguments[0].click();", label_horario)
            horarios_clicados += 1
            
        except:
            break
    
    print(f"{horarios_clicados} horários DOM PEDRO selecionados rapidamente!")
    
    # CLIQUE CHECKBOX FINAL
    try:
        checkbox_termo = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, "ckbTermo"))
        )
        driver.execute_script("arguments[0].click();", checkbox_termo)
        print("Checkbox final marcado!")
    except:
        # BACKUP
        checkbox_termo = driver.find_element(By.CSS_SELECTOR, "input.form-check-input[type='checkbox']")
        driver.execute_script("arguments[0].click();", checkbox_termo)
        print("Checkbox final marcado (método alternativo)!")
    
    # CLIQUE BOTÃO FINAL
    try:
        botao_solicitar = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "send"))
        )
        driver.execute_script("arguments[0].click();", botao_solicitar)
        print("ENVIADO DEU CERTO")
    except:
        # SE NÃO DER CERTO
        try:
            botao_solicitar = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary")
            driver.execute_script("arguments[0].click();", botao_solicitar)
            print("ENVIADO DEU CERTO (OUTRO METODO) 🎉")
        except Exception as botao_error:
            print(f"Erro ao clicar no botão final: {botao_error}")

except Exception as e:
    print(f"Erro: {e}")
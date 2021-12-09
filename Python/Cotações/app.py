# Importações necessárias:
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Abrir o Navegador Google Chrome:
navegador = webdriver.Chrome()

# Acessar o Google.com e pesquisar:
navegador.get('https://www.google.com.br/')

# Pegar a cotação do Dolar:
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação dólar')
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
# Xpath do Dólar
navegador.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')
# Pegar o valor do dólar
dolar = navegador.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print('\nO valor do dolar agora é de R$ {:.2f}.'.format(float(dolar)))

# Acessar o Google.com e pesquisar:
navegador.get('https://www.google.com.br/')

# Pegar a cotação do Bitcoin:
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação bitcoin')
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
# Xpath do Dólar
navegador.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')
# Pegar o valor do dólar
bitcoin = navegador.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print('\nO valor do bitcoin agora é de R$ {:.2f}.'.format(float(bitcoin)))

# Acessar o Google.com e pesquisar:
navegador.get('https://www.google.com.br/')

# Pegar a cotação do Ethereum:
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação ethereum')
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
# Xpath do Dólar
navegador.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')
# Pegar o valor do dólar
ethereum = navegador.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print('\nO valor do ethereum agora é de R$ {:.2f}.\n'.format(float(ethereum)))



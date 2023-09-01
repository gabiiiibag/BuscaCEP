import requests

def main():  
    print("╔══════════════════════╗")
    print("║   Busca de CEP       ║")
    print("╚══════════════════════╝")

    cep = (input("Favor insira um CEP: "))

    if len(cep) !=  8:
        print("número inválido")
        exit()

    request = requests.get("https://viacep.com.br/ws/{}/json/".format(cep))

    addressdata = request.json()

    if 'erro' not in addressdata:
            print ("CEP ENCONTRADO\n")
            print ('CEP: {}'.format (addressdata['cep']))
            print ('Logradouro: {}'.format (addressdata ['logradouro']))
            print ( 'Complemento: {}'.format (addressdata ['complemento']))
            print ('Bairro: {}'.format (addressdata ['bairro']))
            print ('Cidade: {}'.format (addressdata ['localidade']))
            print ('Estado: {}'.format (addressdata['uf']))
            
    else:
            print('{}: CEP inválido.'.format (cep))

    novo_cep = int(input("gostaria de fazer uma nova consulta?\n\n 1 - Sim\n 2 - Não\n"))
    if novo_cep == 1:
        main()
    else:
        exit()

if __name__ == '__main__':
    main()
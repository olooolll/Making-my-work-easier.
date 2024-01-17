from datetime import datetime
from weasyprint import HTML
from data_base_os import *
from pypdf import *
from endereco import *

def criar_ordem_de_servico_html():

    numero_os = input('Digite o número da OS: ')

    dados_os = dados_os_lista(numero_os)

    dados_licenciado = valor_licenca_lista(dados_os)

    numeor_tecnico = input('Digite o número do técnico: ')

    dados_tecnico = valor_tecnico_lista(numeor_tecnico)

    dados_cooler =  dados_cooler_lista(dados_os)


    
    data_atual = datetime.now().strftime("%d/%m/%Y")
    # HTML do documento
    html_content = f"""
<html>
    <head>
        <title>Ordem de Serviço</title>
        <style>
            /* Estilos CSS aqui */
            body, p {{ 
                margin:0 ;
            }}

            h1, h2 {{
                text-align: center;
                margin-top: 0;
            }}

            table, tbody {{

                margin: 0 auto;
                border-collapse: collapse;
                border: 2px solid black;
            }}
            tr, td {{
                margin: 0;
                border: 1px solid gray;
            }}

            th {{
                color: white;
                background-color: black;
                text-align: start;
                
            }}

            h6, p{{
                text-transform: capitalize;
                margin-top: 5px;
                margin-bottom: 5px;
            }}

            td p {{
                text-indent: 10px;
            }}

        </style>
    </head>
    <body>
        
        <h1>Ordem de Serviço N° {dados_os[0]}</h1>
        <h2>Manutenção correntiva de {dados_os[20]}</h2>

        <table>
            <tbody>
                <tr>
                    <th colspan="2">Responsalvel</th>
                </tr>
                <tr>
                    <td>
                        <h6>Nome:</h6>
                        <p>{dados_licenciado[1]}</p>
                    </td>
                    
                    <td>
                        <h6>Telefone:</h6>
                        <p>{dados_licenciado[2]}</p>
                    </td>
                    <tr>
                        <th colspan="2">Equipamento</th>
                    </tr>    
                </tr>
                
                <tr>
                    <td>
                        <h6>Modelo: {dados_os[21]}</h6>
                    </td>
                    <td>
                        <h6>Serial: {dados_os[16]}</h6>
                    </td>
                </tr>

                <tr>
                    <th colspan="2">Enderecço</th>
                    <tr>
                        <td>
                            <h6>Condominío:</h6>
                            <p>{dados_os[17]}</p>
                        </td>
                        <td>
                            <h6>Bairro:</h6>
                            <p>{dados_cooler[13]}</p>
                        </td>
                        <tr>
                            <td>
                                <h6>Logadolro:</h6>
                                <p>{dados_cooler[10]}</p>
                            </td>
                            <td>
                                <h6>Cidade:</h6>
                                <p>{dados_cooler[15]}</p>
                            </td>
                        </tr>
                    </tr>
                </tr>
                <tr>
                    <th colspan="2">Diagnóstico</th>
                </tr>
                <tr>
                    <td colspan="2">
                        <h6>Responsalvel: {dados_os[18]}</h6>
                        <p>{dados_os[21]}</p>
                    </td>
                </tr>

                <tr>
                    <th colspan="2">Solução</th>
                </tr>
                <tr>
                    <td colspan="2">
                        <p>{dados_os[21]}2</p>
                    </td>
                </tr>

                <tr>
                    <th colspan="2">Equipamentos a ser levado</th>
                </tr>
                <tr>
                    <td colspan="2">
                        <p>                        Para manutenções realizadas na Automação TAKE tenha em mãos as seguintes ferramentas:
                            <br>
                            <br>
                            > Alicate Universal e de Corte;
                            <br>
                            > Chaves de Fenda e Philips;
                            <br>
                            > Chaves canhão ou Bit de 1/4 pol. E de 7mm;
                            <br>
                            > Multímetro;
                            <br>
                            > Ferro de Solda.
                            <br>
                            <br>
                            > Entre em contato com o Departamento de Suporte técnico para seguir as instruções
                            <br>
                            > Obtenha com o licenciado de a liberação de entrada ao local da geladeira instalada</p>
                    </td>
                </tr>

                <tr>
                    <th colspan="2">Técnico</th>
                </tr>
                <tr>
                    <td>
                        <h6>Nome:</h6>
                        <p>{dados_tecnico[2]}</p>
                    </td>
                    <td>
                        <h6>Numero:</h6>
                        <p>{dados_tecnico[0]}</p>
                    </td>
                    <tr>
                        <td>
                            <h6>Razão social:</h6>
                            <p>{dados_tecnico[4]}</p>
                        </td>
                        <td>
                            <h6>CNPJ:</h6>
                            <p>{dados_tecnico[3]}</p>
                        </td>
                    </tr>
                </tr>

                <tr>
                    <th colspan="2">observações</th>
                </tr>
                <tr>
                    <td colspan="2">
                        <p>A ordem de serviço foi gerada {data_atual} e tem a vigência de ser completada em até 2 dias, caso não realize a visita entraremos em contato para o cancelamento da mesma</p>
                    </td>
                </tr>

            </tbody>
        </table>

    </body>
</html>
    """

    # Gera o PDF a partir do HTML
    HTML(string=html_content).write_pdf(f'OS {dados_os[0]} - {dados_os[16]} - {dados_os[12]}.pdf')

if __name__ == "__main__":
    # Nome do arquivo PDF que você deseja criar
    nome_do_arquivo = "ordem_de_servico_html.pdf"

    # Informações do cliente
    cliente = "Nome do Cliente"

    # Descrição do serviço
    descricao_servico = """
    Este é um exemplo de ordem de serviço.
    Inclua aqui todos os detalhes relevantes sobre o serviço a ser realizado.
    """

    # Chama a função para criar a ordem de serviço em PDF a partir de HTML
    criar_ordem_de_servico_html()

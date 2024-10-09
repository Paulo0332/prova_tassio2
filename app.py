from flask import Flask, render_template
from reportagens import Reportagem

app = Flask(__name__)

lista_reportagem = [
Reportagem(1, "Demitida por Lewandowski, advogada assume posto no Palácio do Planalto", "Pedro Teixeira","Política", "A advogada Estela Aranha foi nomeada assessora especial do presidente Luiz Inácio Lula da Silva (PT). O ato foi oficializado em publicação no Diário Oficial da União (DOU). Estela é ex-secretária de Direitos Digitais do Ministério da Justiça, tendo atuado durante a gestão de Flávio Dino, hoje ministro do Supremo Tribunal Federal (STF). Estela foi demitida por Ricardo Lewandowski quando ele substituiu Dino no comando do Ministério da Justiça, no começo do ano.", "demitida_lewandowski.png","pedro_teixeira.jpg"),
Reportagem(2, "X diz que vai pagar novas multas e Moraes reitera decisão para desbloquear conta bancária", "Lucas Mendes","Política", "A rede social X informou, nesta terça-feira (1º), que vai pagar as novas multas determinadas pelo ministro Alexandre de Moraes, do Supremo Tribunal Federal (STF).","twitter_xandao.jpg","lucas_mendes.jpg"),
Reportagem(3, "Como a escalada do conflito no Oriente Médio pode impactar a economia do Brasil?","João Nakamura","Economia","A seis dias de a guerra entre Israel e o Hamas completar um ano, o Irã voltou a bombardear o território israelense. E apesar de estar a meio mundo de distância, o que acontece no Oriente Médio reflete no Brasil e no mercado internacional. Olhando para o petróleo, a reação do mercado foi instantânea: a cotação do barril chegou a saltar 5% nesta terça-feira (1º).“O petróleo é uma commodity global. Se tem uma guerra justamente na região de onde vem a maior parte da produção do mundo, ela fica menos disponível e o preço sobe”, explica Virginia Parente, economista e professora do Instituto de Energia e Ambiente da Universidade de São Paulo (USP).","conflito_oriente.jfif","joao_nakamura.jfif"),
Reportagem(4, "Dia das Crianças: 8 em cada 10 brasileiros pretendem gastar até R$ 250 com presentes","Patrick Fuentes","Economia", "Olhando para o petróleo, a reação do mercado foi instantânea: a cotação do barril chegou a saltar 5% nesta terça-feira (1º). “O petróleo é uma commodity global. Se tem uma guerra justamente na região de onde vem a maior parte da produção do mundo, ela fica menos disponível e o preço sobe”, explica Virginia Parente, economista e professora do Instituto de Energia e Ambiente da Universidade de São Paulo (USP).","dia_crianca.jpg","patrick_fuentes.jfif"),
Reportagem(5, "Museu da Língua Portuguesa terá programação gratuita no Dia das Crianças","Giovana Christ","Cultura", "O Museu da Língua Portuguesa, em São Paulo, fará uma programação especial para o Dia das crianças, em 12 de outubro. O Festival Dia das Crianças 2024 contará com 16 atividades gratuitas envolvendo música, teatro e brincadeiras.","museu.webp","giovana.jpg"),
Reportagem(6,"J. Borges: exposição no Rio celebra obra do pernambucano, morto nesta sexta (26)","Fernanda Pinoti","Cultura", "O artista pernambucano J. Borges, que morreu na manhã desta sexta-feira (26) aos 88 anos, está em exposição no Museu do Pontal, no Rio de Janeiro.","j_borges.webp","fernanda_pinotti.jfif"),
Reportagem(7,"Arsenal controla PSG em casa e vence primeira na Champions League", "Luccas Oliveira","Esporte", "O Arsenal deu mais uma prova de força na temporada ao vencer, com certa tranquilidade, o PSG por 2 a 0, nesta terça-feira (1), pela segunda rodada da Champions League.Os dois gols da partida saíram na primeira etapa. Havertz abriu o placar de cabeça, aproveitando cruzamento de Trossard. E Saka ampliou “quase sem querer”: a falta que jogou na área passou por todo mundo e enganou o goleiro Donnarumma.","arsenal.jfif","luccas_oliveira.jfif"),
Reportagem(8,"Copa do Brasil: Federação Paulista apoia Corinthians e critica CBF por mudanças","Raul Moura","Esporte","A mudança de datas das semifinais da Copa do Brasil por parte da CBF segue gerando polêmicas. Na tarde desta terça-feira (1), a Federação Paulista de Futebol saiu em defesa do Corinthians e fez duras críticas a entidade que comanda o o futebol brasileiro. Em nota oficial, a FPF repudiou a troca de forma pública e disse que “tal medida afronta o Regulamento Geral de Competições da CBF”. O Corinthians entrou com ação no STJD (Superior Tribunal de Justiça Desportiva), contra a decisão da CBF para mudar a data da partida de volta da semifinal contra o Flamengo na Copa do Brasil.","copa_brasil.webp","raul_moura.jfif"),


]


@app.route('/')
def home():
    return render_template("index.html", lista_reportagem=lista_reportagem,)

@app.route('/teste')
def teste():
    return render_template('teste.html', lista_reportagem=lista_reportagem)


@app.route('/reportagens')
def reportagens():
    return render_template('detalhes.html', Reportagem=Reportagem, lista_reportagem=lista_reportagem)


@app.route("/detalhe/<int:id>")
def detalhe(id):
    for reportagem in lista_reportagem:
        if reportagem.get_id() == id:
            return render_template("detalhes.html", reportagem=reportagem)
        
    return "<h1>Ops! Nenhum reportagem encontrado!</h1>"
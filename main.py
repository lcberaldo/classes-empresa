class Empregado:
    numero_empregados = 0

    def __init__(self, nome_completo, email, matricula_funcional, salario):
        self.nome_completo = nome_completo
        self.email = email
        self.matricula_funcional = matricula_funcional
        self.salario = int(salario)
        self.profissao = ''
        Empregado.numero_empregados += 1

    def iniciar_jornada(self):
        print(f'O {self.profissao} {self.nome_completo} iniciou sua jornada de trabalho!')

    def finalizar_jornada(self):
        print(f'O {self.profissao} {self.nome_completo} finalizou sua jornada de trabalho!')

    def receber_aumento(self):
        raise NotImplementedError

    @classmethod
    def mostrar_numero_total_empregados(cls):
        print(f'O número total de empregados na empresa é: {cls.numero_empregados}')


class Desenvolvedor(Empregado):
    porcentagem_aumento_dev = 0.05

    def __init__(self, nome_completo, email, matricula_funcional, salario,
                 linguagens_programacao=None, litros_cafe=0.0, burnout=False):
        super(Desenvolvedor, self).__init__(nome_completo, email, matricula_funcional, salario)

        if linguagens_programacao is None:
            linguagens_programacao = ['']

        self.profissao = 'Dev'
        self.linguagens_programacao = linguagens_programacao
        self.litros_cafe = litros_cafe
        self.burnout = burnout
        print(f'O/A desenvolvedor {nome_completo} foi contratado!')

    def adicionar_linguagem(self, nova_linguagem):
        self.linguagens_programacao.append(nova_linguagem)

        string_linguagens = self.linguagens_programacao
        print(f'{self.nome_completo} acaba de aprender a programar em {nova_linguagem} '
              f'então agora sabe: {string_linguagens}')

    def beber_cafe(self):
        if self.litros_cafe >= 1:
            self.burnout = True
            print('O desenvolvedor entrou em burnout!!!!!! ')
        else:
            self.litros_cafe += 0.250
            print(f'{self.nome_completo} acaba de beber 250ml de café!')

    def receber_aumento(self):
        aumento = self.salario * Desenvolvedor.porcentagem_aumento_dev
        self.salario += aumento
        print(f'o dev {self.nome_completo} recebeu R${aumento:.2f} e agora recebe {self.salario:.2f}')


class GerenteProjeto(Empregado):
    porcentagem_aumento_gerente = 0.12

    def __init__(self, nome_completo, email, matricula_funcional, salario, time=None, projetos_evolvidos=None):
        super(GerenteProjeto, self).__init__(nome_completo, email, matricula_funcional, salario,)

        if projetos_evolvidos is None:
            projetos_evolvidos = []
        if time is None:
            time = []

        self.time = time
        self.projetos_envolvidos = projetos_evolvidos
        print(f'{nome_completo} foi designado como Gerente de projetos!')

    def adicionar_desenvolvedor(self, desenvolvedor):
        self.time.append(desenvolvedor)
        print(f'O dev {desenvolvedor.nome_completo} foi adicionado ao time!')
        string_time = ''

        for desenvolvedor in self.time:
            string_time += desenvolvedor.nome_completo + ', '

        print(f'O time: {string_time}')

    def remover_desenvolvedor(self, desenvolvedor):
        self.time.remove(desenvolvedor)
        print(f'O dev {desenvolvedor.nome_completo} foi removido do time!')
        print(f'O time agora é {self.time}')

    def participar_projeto(self, projeto):
        self.projetos_envolvidos.append(projeto)
        print(f'{self.nome_completo} agora trabalha no projeto {projeto}')
        print(f'sua lista de projetos agora é {self.projetos_envolvidos}')

    def sair_projeto(self, projeto):
        self.projetos_envolvidos.remove(projeto)
        print(f'{self.nome_completo} saiu do projeto {projeto}')
        print(f'sua lista de projetos agora é {self.projetos_envolvidos}')

    def receber_aumento(self):
        aumento = self.salario * GerenteProjeto.porcentagem_aumento_gerente
        self.salario += aumento
        print(f'o gerente {self.nome_completo} recebeu R${aumento:.2f} e agora recebe {self.salario:.2f}')



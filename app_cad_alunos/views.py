from django.shortcuts import render
from .models import Alunocad
def home(request):
    return render(request,'alunos/home.html')

def alunos(request):
    #salvar os dados da tela para o banco de dados.
    novo_aluno = Alunocad()
    novo_aluno.nome = request.POST.get('nome')
    novo_aluno.sobrenome = request.POST.get('sobrenome')
    novo_aluno.telefone = request.POST.get('telefone')
    novo_aluno.cpf = request.POST.get('cpf')
    novo_aluno.cep = request.POST.get('cep')
    novo_aluno.endereco = request.POST.get('endereco')
    novo_aluno.bairro = request.POST.get('bairro')
    novo_aluno.cidade = request.POST.get('cidade')
    novo_aluno.estado = request.POST.get('estado')
    novo_aluno.email = request.POST.get('email')
    novo_aluno.modalidade = request.POST.get('modalidade')
    novo_aluno.horario = request.POST.get('horario')
    novo_aluno.save()
    
    #exibir todos os alunos já cadastrados em nova página
    alunos = {
    'alunos': Alunocad.objects.all()
    }
    
    #retornar os dados para a pagina de lista de alunos
    return render(request,'alunos/alunos.html',alunos)
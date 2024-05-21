from django.db import models
from django.core.exceptions import ValidationError

class Alunocad(models.Model):
    id_aluno = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    sobrenome = models.TextField()
    telefone = models.IntegerField()
    cpf = models.IntegerField()
    cep = models.IntegerField()
    endereco = models.TextField()
    bairro = models.TextField()
    cidade = models.TextField()
    estado = models.TextField()
    email = models.TextField()
    modalidade = models.TextField()
    horario = models.TextField()
    
   
    def save(self, *args, **kwargs):
        if Alunocad.objects.filter(nome=self.nome, cpf=self.cpf).exists():
            pass
        else:
            super(Alunocad, self).save(*args, **kwargs)
            
            
            
            
            
            
            
            
            
            
            
            
# def save(self, *args, **kwargs):
#     if Alunocad.objects.filter(nome=self.nome, cpf=self.cpf).exists():
#         raise ValidationError("Este aluno já está cadastrado.")
#     else:
#         super(Alunocad, self).save(*args, **kwargs)
        
        
#     def excluir_aluno_por_id(cls, aluno_id):
#         try:
#             aluno = cls.objects.get(id_aluno=aluno_id)
#             confirmacao = input(f"Deseja excluir o aluno {aluno.nome} {aluno.sobrenome}? (sim/não): ")
#             if confirmacao.lower() == "sim":
#                 aluno.delete()
#                 print("Aluno excluído com sucesso.")
#             else:
#                 print("Exclusão cancelada.")
#         except cls.DoesNotExist:
#             print("Aluno não encontrado.")
#         except Exception as e:
#             print(f"Ocorreu um erro: {str(e)}")

    
# def save(self, *args, **kwargs):
#         aluno_existente = Alunocad.objects.filter(nome=self.nome, cpf=self.cpf).exists()
#         if aluno_existente:
#            raise ValidationError("Este aluno já está cadastrado.")
#         else:
#             super(Alunocad, self).save(*args, **kwargs)

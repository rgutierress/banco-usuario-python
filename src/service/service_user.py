from src.models.store import Store
from src.models.user import User


class ServiceUser:

    def __init__(self):
        self.store = Store()

    def add_user(self, name, job):
        if name is not None and job is not None:
            if isinstance(name, str) and isinstance(job, str):
                for name_obj in self.store.bd:
                    if name_obj.name == name:
                        return f"Usuário '{name}' já existe"
                user = User(name=name, job=job)
                self.store.bd.append(user)
                return f"Usuário '{name}' atualizado com sucesso."
            else:
                return "Nome e Job devem ser strings"
        else:
            return "Nome e Job não pode ser None"

    def remove_user(self, name, job):
        if name is not None and job is not None:
            if isinstance(name, str) and isinstance(job, str):
                for name_obj in self.store.bd:
                    if name_obj.name == name:
                        self.store.bd.remove(name_obj)
                        return f"Usuário '{name_obj.name}' removido com sucesso."
                return f"Usuário com nome '{name}' não encontrado."
            else:
                return "Nome e Job devem ser strings"
        else:
            return "Nome e Job não pode ser None"

    def update_user(self, new_name, job):
        if new_name is not None and job is not None:
            if isinstance(new_name, str) and isinstance(job, str):
                user_found = False

                for index, user in enumerate(self.store.bd):
                    if user.name == new_name:
                        user.job = job
                        self.store.bd[index] = user
                        user_found = True
                        return f"Usuário '{new_name}' atualizado com sucesso."

                if not user_found:
                    return f"Usuário com nome '{new_name}' não encontrado."
            else:
                return "Nome e Job devem ser strings"
        else:
            return "Nome e Job não podem ser None"

    def get_user_by_name(self, name, job):
        if name is not None and job is not None:
            if isinstance(name, str) and isinstance(job, str):
                for user in self.store.bd:
                    if user.name == name and user.job == job:
                        return f"Usuário encontrado: Nome: {user.name}, Job: {user.job}"
                    else:
                        return f"Usuário com Nome '{name}' não encontrado."
            else:
                return "Nome e Job devem ser strings"
        else:
            return "Nome e Job não podem ser None"


    ##
    ## Solução do Professor
    ##

    # def find_user(self, name):
    #     for user in self.store.bd:
    #         if user.name == name:
    #             return user

    # def add_user(self, name, job):
    #     if name is not None and job is not None:
    #         if isinstance(name, str) and isinstance(job, str):
    #             user_bd = self.find_user(name)
    #             if user_bd == None:
    #                 user = User(name=name, job=job)
    #                 self.store.bd.append(user)
    #                 return "Usuário adicionado"
    #             else:
    #                 return "Usuário já existe"
    #         else:
    #             return "Usuário inválido"
    #     else:
    #         return "Nome ou Job não pode ser None"

    # def delete_user(self, name, job):
    #     if name is not None and job is not None:
    #         if isinstance(name, str) and isinstance(job, str):
    #             user_bd = self.find_user(name)
    #             if user_bd != None:
    #                     self.store.bd.remove(user_bd)
    #                     return "Usuário removido"
    #             else:
    #                     return "Usuário não existe"
    #         else:
    #             return "Usuário inválido"
    #     else:
    #         return "Usuário inválido"
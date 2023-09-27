from src.service.service_user import ServiceUser


class TestServiceUser:

    ### Validate for add_user ###

    def test_add_user_with_success(self):
        ##Setup
        service = ServiceUser()
        expect_response = "Usuário 'Stephane' atualizado com sucesso."

        ##Chamada
        response = service.add_user("Stephane", "QA")

        ##Avaliação
        assert expect_response == response

    def test_add_user_existing_name(self):
        ##Setup
        service = ServiceUser()
        name_exist = "Stephane Miranda"
        job = "QA"
        service.add_user(name_exist, job)

        ## Chamada
        response = service.add_user(name_exist, job)

        ##Avaliação
        assert response == "Usuário 'Stephane Miranda' já existe"

    def test_add_user_with_name_none(self):
        ##Setup
        service = ServiceUser()

        ## Chamada
        response = service.add_user(None, "QA")

        ##Avaliação
        assert response == "Nome e Job não pode ser None"

    def test_add_user_with_job_none(self):
        ##Setup
        service = ServiceUser()

        ## Chamada
        response = service.add_user("Stephane", None)

        ##Avaliação
        assert response == "Nome e Job não pode ser None"

    def test_add_user_with_name_and_job_none(self):
        ##Setup
        service = ServiceUser()

        ## Chamada
        response = service.add_user(None, None)

        ##Avaliação
        assert response == "Nome e Job não pode ser None"

    def test_add_user_with_name_non_string(self):
        ##Setup
        service = ServiceUser()
        expect_response = "Nome e Job devem ser strings"

        ##Chamada
        response = service.add_user(123, "QA")

        ##Avaliação
        assert expect_response == response

    def test_add_user_with_job_non_strings(self):
        ##Setup
        service = ServiceUser()
        expect_response = "Nome e Job devem ser strings"

        ##Chamada
        response = service.add_user("Stephane", 456)

        ##Avaliação
        assert expect_response == response

    def test_add_user_with_name_and_job_non_strings(self):
        ##Setup
        service = ServiceUser()
        expect_response = "Nome e Job devem ser strings"

        ##Chamada
        response = service.add_user(123, 456)

        ##Avaliação
        assert expect_response == response

    def test_add_user_name_empty(self):
        ##Setup
        service = ServiceUser()
        expect_response = ("Usuário '' atualizado com sucesso.")

        ##Chamada
        response = service.add_user("", "QA")

        ##Avaliação
        assert expect_response == response

    def test_add_user_job_empty(self):
        ##Setup
        service = ServiceUser()
        expect_response = ("Usuário 'Stephane' atualizado com sucesso.")

        ##Chamada
        response = service.add_user("Stephane", "")

        ##Avaliação
        assert expect_response == response

    def test_add_user_name_and_job_empty(self):
        ##Setup
        service = ServiceUser()
        expect_response = ("Usuário adicionado")

        ##Chamada
        response = service.add_user("", "")

        ##Avaliação
        assert expect_response == response

    ### Validate for remove_user ###
    
    def test_remove_user_with_success(self):
        ##Setup
        service = ServiceUser()
        resposta = service.add_user("Stephane", "QA")
        expect_response = "Usuário 'Stephane' removido com sucesso."

        ##Chamada
        response = service.remove_user("Stephane", "QA")

        ##Avaliação
        assert  expect_response == response

    def test_remove_user_name_non_existent(self):
        pass

    def test_remove_user_with_name_none(self):
        ##Setup
        service = ServiceUser()
        expect_response = "Nome e Job não pode ser None"

        ##Chamada
        response = service.remove_user(None, "QA")

        ##Avaliação
        assert expect_response == response

    def test_remove_user_with_job_none(self):
        ##Setup
        service = ServiceUser()
        expect_response = "Nome e Job não pode ser None"

        ##Chamada
        response = service.remove_user("Stephane", None)

        ##Avaliação
        assert expect_response == response

    def test_remove_user_with_name_and_job_none(self):
        ##Setup
        service = ServiceUser()
        expect_response = "Nome e Job não pode ser None"

        ##Chamada
        response = service.remove_user(None, None)

        ##Avaliação
        assert expect_response == response

    def test_remove_user_with_name_non_string(self):
        ##Setup
        service = ServiceUser()
        expect_response = "Nome e Job devem ser strings"

        ##Chamada
        response = service.remove_user(123, "QA")

        ##Avaliação
        assert expect_response == response

    def test_remove_user_with_job_non_strings(self):
        ##Setup
        service = ServiceUser()
        expect_response = "Nome e Job devem ser strings"

        ##Chamada
        response = service.remove_user("Stephane", 123)

        ##Avaliação
        assert expect_response == response

    def test_remove_user_with_name_and_job_non_strings(self):
        ##Setup
        service = ServiceUser()
        expect_response = "Nome e Job devem ser strings"

        ##Chamada
        response = service.remove_user(123, 456)

        ##Avaliação
        assert expect_response == response

    def test_remove_user_name_empty(self):
        ##Setup
        service = ServiceUser()
        expect_response = "Usuário com nome '' não encontrado."

        ##Chamada
        response = service.remove_user("", "QA")

        ##Avaliação
        assert expect_response == response

    def test_remove_user_job_empty(self):
        ##Setup
        service = ServiceUser()
        expect_response = "Usuário com nome 'Stephane' não encontrado."

        ##Chamada
        response = service.remove_user("Stephane", "")

        ##Avaliação
        assert expect_response == response

    def test_remove_user_name_and_job_empty(self):
        ##Setup
        service = ServiceUser()
        expect_response = "Usuário com nome '' não encontrado."

        ##Chamada
        response = service.remove_user("", "")

        ##Avaliação
        assert expect_response == response

    ### Validate for update_user ###

    def test_update_user_with_success(self):
        ##Setup
        service = ServiceUser()
        response = service.add_user("Stephane", "QA")
        expect_response = f"Usuário 'Stephane' atualizado com sucesso."

        ##Chamada
        response = service.update_user("Stephane", "QA2")

        ##Avaliação
        assert expect_response == response

    def test_update_user_non_existent(self):
        ##Setup
        service = ServiceUser()
        response = service.add_user("Stephane", "QA")
        expect_response = "Usuário com nome 'StephaneMiranda' não encontrado."

        ##Chamada
        response = service.update_user("StephaneMiranda", "QA2")

        ##Avaliação
        assert expect_response == response

    def test_update_user_with_name_none(self):
        ##Setup
        service = ServiceUser()
        expect_response = "Nome e Job não podem ser None"

        ##Chamada
        response = service.update_user(None, "QA2")

        ##Avaliação
        assert expect_response == response

    def test_update_user_with_job_none(self):
        ##Setup
        service = ServiceUser()
        expect_response = "Nome e Job não podem ser None"

        ##Chamada
        response = service.update_user("Stephane", None)

        ##Avaliação
        assert expect_response == response

    def test_update_user_with_name_and_job_none(self):
        ##Setup
        service = ServiceUser()
        expect_response = "Nome e Job não podem ser None"

        ##Chamada
        response = service.update_user(None, None)

        ##Avaliação
        assert expect_response == response

    def test_update_user_with_name_non_string(self):
        ##Setup
        service = ServiceUser()
        expect_response = ("Nome e Job devem ser strings")

        ##Chamada
        response = service.update_user(123, "QA")

        ##Avaliação
        assert expect_response == response

    def test_update_user_with_job_non_strings(self):
        ##Setup
        service = ServiceUser()
        expect_response = ("Nome e Job devem ser strings")

        ##Chamada
        response = service.update_user("Stephane", 456)

        ##Avaliação
        assert expect_response == response

    def test_update_user_with_name_and_job_non_strings(self):
        ##Setup
        service = ServiceUser()
        expect_response = ("Nome e Job devem ser strings")

        ##Chamada
        response = service.update_user(123, 456)

        ##Avaliação
        assert expect_response == response

    def test_update_user_name_empty(self):
        ##Setup
        service = ServiceUser()
        expect_response = ("Usuário com nome '' não encontrado.")

        ##Chamada
        response = service.update_user("", "QA")

        ##Avaliação
        assert expect_response == response

    def test_update_user_job_empty(self):
        ##Setup
        service = ServiceUser()
        response = service.add_user("Stephane", "QA")

        expect_response = ("Usuário 'Stephane' atualizado com sucesso.")

        ##Chamada
        response = service.update_user("Stephane", "")

        ##Avaliação
        assert expect_response == response

    def test_add_user_name_and_job_empty(self):
        ##Setup
        service = ServiceUser()
        expect_response = ("Usuário com nome '' não encontrado.")

        ##Chamada
        response = service.update_user("", "")

        ##Avaliação
        assert expect_response == response

    ### Validate for get_user_by_name ###

    def test_get_user_success(self):
        ##Setup
        service = ServiceUser()
        response = service.add_user("Stephane", "QA")
        expect_response = ("Usuário encontrado: Nome: Stephane, Job: QA")

        ##Chamada
        response = service.get_user_by_name("Stephane", "QA")

        ##Avaliação
        assert response == "Usuário encontrado: Nome: Stephane, Job: QA"

    def test_get_user_by_name_not_found_user(self):
        ##Setup
        service = ServiceUser()
        response = service.add_user("Stephane", "QA")
        expect_response = ("Usuário encontrado: Nome: Stephane, Job: QA")

        ##Chamada
        response = service.get_user_by_name("Simone", "QA")

        ##Avaliação
        assert response == f"Usuário com Nome 'Simone' não encontrado."

    def test_get_user_by_name_with_name_none(self):
        ##Setup
        service = ServiceUser()
        response = service.add_user("Stephane", "QA")
        expect_response = "Nome e Job não podem ser None"

        ##Chamada
        response = service.get_user_by_name(None, "QA")

        ##Avaliação
        assert response == "Nome e Job não podem ser None"

    def test_get_user_by_name_with_job_none(self):
        ##Setup
        service = ServiceUser()
        response = service.add_user("Stephane", "QA")
        expect_response = "Nome e Job não podem ser None"

        ##Chamada
        response = service.get_user_by_name("Stephane", None)

        ##Avaliação
        assert response == "Nome e Job não podem ser None"

    def test_get_user_by_name_and_job_none(self):
        ##Setup
        service = ServiceUser()
        response = service.add_user("Stephane", "QA")
        expect_response = "Nome e Job não podem ser None"

        ##Chamada
        response = service.get_user_by_name(None, None)

        ##Avaliação
        assert response == "Nome e Job não podem ser None"

    def test_get_user_by_name_no_string(self):
        ##Setup
        service = ServiceUser()
        response = service.add_user("Stephane", "QA")

        ##Chamada
        response = service.get_user_by_name(123, "QA")
        expect_response = "Nome e Job devem ser strings"

        ##Avaliação
        assert response == "Nome e Job devem ser strings"

    def test_get_user_by_name_job_no_string(self):
        ##Setup
        service = ServiceUser()
        response = service.add_user("Stephane", "QA")
        expect_response = "Nome e Job devem ser strings"

        ##Chamada
        response = service.get_user_by_name("Stephane", 123)

        ##Avaliação
        assert response == "Nome e Job devem ser strings"
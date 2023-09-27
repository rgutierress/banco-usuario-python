from src.service.service_user import ServiceUser

service = ServiceUser()
response = service.add_user("Stephane", "QA")
print(response)

response = service.get_user_by_name(None, "QA")
print(response)
# response = service.update_user("Stephane", "")
# print(response)
# response = service.add_user("Stephane", "QA")
# print(response)
#
# response = service.delete_user("Stephane", "QA")
# print(response)

# response1 = service.delete_user("Stephane", "QA")
# print(response1)

##print(service.store.bd[1].name)

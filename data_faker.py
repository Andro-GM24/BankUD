from faker import Faker

f = Faker(["es_CO"])

number_of_mails = 100

list_of_domains = (
    'com',
    'com.br',
    'net',
    'net.br',
    'org',
    'org.br',
    'gov',
    'gov.br'
)
def crear_correo():


   first_name = f.first_name()
   last_name = f.last_name()
   company = f.company().split()[0].strip(',')
   dns_org = f.random_choices(elements=list_of_domains, length=1)[0]
   email = f"{first_name.lower()}.{last_name.lower()}@{company.lower()}.{dns_org}".replace(" ", "")
   return email

numero_de_datos=10
Usuarios=[]
nombre=[]
id=[]
amount=[]
celular=[]
gmail=[]
password=[]


def Crear_usuario ():




      for j in range(1,10):
         nombre.append(f.name())
         id.append(f.unique.random_int(min=1030000000,max=1032000000))
         amount.append(random.uniform(500000, 2000000))
         celular.append(f.phone_number())
         password.append(f.pystr())
         gmail.append(crear_correo())

      return Usuarios
from locust import HttpUser, TaskSet, task, between

class LoginTasks(TaskSet):
    def on_start(self):
        """
        Esta función se ejecuta cada vez que un usuario simulado comienza su tarea.
        Aquí puedes inicializar datos, como credenciales.
        """
        self.username = "usuario_prueba"
        self.password = "contraseña_segura"

    @task
    def login(self):
        """
        Simula el ingreso al sistema mediante una solicitud POST al endpoint de login.
        """
        # Datos de inicio de sesión
        login_data = {
            "username": self.username,
            "password": self.password
        }
        
        # Envía la solicitud POST al endpoint de login
        response = self.client.post("/api/login", json=login_data)
        
        # Verifica si el login fue exitoso
        if response.status_code == 200:
            print("Inicio de sesión exitoso.")
        else:
            print(f"Error en el login: {response.status_code} - {response.text}")

class WebsiteUser(HttpUser):
    """
    Configura el usuario simulado para realizar tareas relacionadas con el login.
    """
    tasks = [LoginTasks]
    wait_time = between(1, 5)  # Espera entre 1 y 5 segundos entre tareas
    host = "http://tu-servidor.com"  # Cambia esto por la URL base de tu sistema

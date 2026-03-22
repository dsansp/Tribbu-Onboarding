# Tribbu Onboarding - Appium Android Automation Framework

Framework de automatización móvil para dispositivos Android físicos usando Appium.

## Estructura del Proyecto

```
Tribbu-Onboarding/
├── config/
│   ├── __init__.py
│   └── capabilities.py    # Configuración de capabilities para Android
├── src/
│   ├── __init__.py
│   ├── driver.py          # Gestión del driver de Appium
│   └── app_launcher.py    # Lanzador de aplicaciones Android
├── tests/
│   ├── __init__.py
│   └── test_example.py    # Tests de ejemplo
├── requirements.txt
└── README.md
```

## Requisitos Previos

1. **Python 3.8+** instalado
2. **Appium Server** instalado y ejecutándose en `http://localhost:4723`
3. **Dispositivo Android físico** conectado vía USB con depuración USB activada
4. **ADB** configurado y accesible desde la terminal

## Instalación

```bash
# Crear entorno virtual (opcional pero recomendado)
python -m venv venv

# Activar entorno virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

## Configuración del Dispositivo

### Habilitar Depuración USB en Android
1. Ir a **Configuración > Información del teléfono**
2. Tocar **Número de compilación** 7 veces para activar opciones de desarrollador
3. Ir a **Opciones de desarrollador**
4. Activar **Depuración USB**

### Verificar conexión del dispositivo
```bash
# Verificar que ADB detecta el dispositivo
adb devices


```

## Uso

### Conectar dispositivo y abrir una app

```python
from src.app_launcher import AppLauncher

# Crear instancia del lanzador
launcher = AppLauncher(appium_url="http://localhost:4723")

# Lanzar app (pasar el package name)
driver = launcher.launch_app(app_id="com.example.app")

# Tu lógica de prueba aquí...

# Cerrar app al terminar
launcher.close_app()
```

### Conectar dispositivo específico por UDID

```python
from src.app_launcher import AppLauncher

launcher = AppLauncher()
driver = launcher.launch_app(
    app_id="com.example.app",
    udid="tu-device-udid-aqui"
)
```

## Capabilities Configurables

El archivo `config/capabilities.py` contiene todas las capabilities configurables:

| Capability | Descripción | Valor por defecto |
|------------|-------------|-------------------|
| `platform_name` | Plataforma móvil | "Android" |
| `automation_name` | Motor de automatización | "UiAutomator2" |
| `device_name` | Nombre del dispositivo | "Android Device" |
| `udid` | ID único del dispositivo | Auto-detectado |
| `app_package` | Package name de la app | Requerido |
| `app_activity` | Activity principal | ".MainActivity" |
| `no_reset` | No reiniciar app | True |
| `full_reset` | Reset completo | False |



## Ejecutar Tests

```bash
# Ejecutar todos los tests
pytest tests/

# Ejecutar un test específico
python -m pytest test_onboarding.py -v --cache-clear

# Ejecutar con verbose
pytest tests/ -v
```

## Reportes Allure

El framework incluye integración con **Allure Reports** para generar reportes detallados de ejecución de tests.

### Instalación de Allure Command Line

```bash
# Windows (con Scoop)
scoop install allure

# Windows (con Chocolatey)
choco install allure

# macOS (con Homebrew)
brew install allure

# Linux
sudo apt-add-repository ppa:qameta/allure
sudo apt-get update
sudo apt-get install allure
```

### Generar Reporte

```bash
# Ejecutar tests y generar resultados de Allure
pytest tests/ --alluredir=allure-results

# Ejecutar test específico con Allure
python -m pytest tests/test_onboarding.py -v --cache-clear --alluredir=allure-results
```

### Visualizar Reporte

```bash
# Generar y abrir reporte en navegador
allure serve allure-results

# O generar reporte estático
allure generate allure-results -o allure-report
allure open allure-report
```

### Estructura del Reporte

Los tests incluyen anotaciones Allure para una mejor organización:

| Anotación | Descripción |
|-----------|-------------|
| `@allure.feature()` | Agrupa tests por funcionalidad principal |
| `@allure.story()` | Describe la historia de usuario dentro de la feature |
| `@allure.severity()` | Prioridad: blocker, critical, normal, minor, trivial |
| `@allure.step()` | Pasos detallados dentro de cada test |
| `@allure.attach()` | Screenshots automáticos en caso de fallo |

### Ejemplo de Reporte

El reporte mostrará:
- Timeline de ejecución
- Pasos detallados de cada test
- Screenshots en fallos
- Estadísticas por feature y severity
- Historial de ejecuciones

## Iniciar Appium Server

```bash
# Usando Appium Desktop (GUI)
# Abrir Appium Desktop y hacer clic en "Start Server"

# Usando línea de comandos
appium

# Con puerto específico
appium -p 4723
```

## Troubleshooting

### Error: "Device not found"
- Verificar que el dispositivo está conectado: `adb devices`
- Verificar que la depuración USB está activada
- Intentar reiniciar el servidor ADB: `adb kill-server && adb start-server`

### Error: "Appium server not reachable"
- Verificar que Appium server está corriendo
- Confirmar el puerto correcto (default: 4723)

### Error: "Permission denied"
- Habilitar permisos de depuración USB en el dispositivo
- Aceptar el diálogo de permiso en el teléfono si aparece


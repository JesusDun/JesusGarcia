import os
from flask import Flask, send_from_directory, jsonify

# Se inicializa la aplicación Flask, indicando que 'assets' es la carpeta para archivos estáticos.
app = Flask(__name__, static_folder='assets')

# --- Rutas para servir archivos estáticos ---
# Esta sección se asegura de que el navegador pueda encontrar tus CSS, JS, imágenes, etc.

@app.route('/assets/<path:path>')
def send_assets(path):
    """Sirve cualquier archivo solicitado desde la carpeta 'assets'."""
    return send_from_directory('assets', path)

# --- Rutas de la aplicación web ---

@app.route('/')
def home():
    """Sirve el archivo principal de tu página web."""
    return send_from_directory('.', 'index.html')

@app.route('/privacy-policy')
def privacy_policy():
    """Sirve la página de la política de privacidad."""
    return send_from_directory('.', 'privacy-policy.html')

@app.route('/terms-and-conditions')
def terms_and_conditions():
    """Sirve la página de términos y condiciones."""
    return send_from_directory('.', 'terms-and-conditions.html')
    
# --- Rutas de la API (Aquí es donde ocurre la magia del Web Service) ---

@app.route('/api/saludo')
def saludo():
    """
    Un ejemplo de un endpoint de API.
    Devuelve un mensaje en formato JSON.
    """
    return jsonify({"message": "¡Hola desde el Web Service con Python!"})

# --- Arranque del servidor ---

if __name__ == '__main__':
    # Inicia la aplicación en modo de depuración para facilitar el desarrollo.
    app.run(debug=True, port=5000)

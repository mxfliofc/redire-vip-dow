from flask import Flask, request, render_template_string, redirect
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>GET USER VIP</h1>"

@app.route('/get-video/<path:url>', methods=['GET'])
def redirect_video(url):
    try:
        # Verificar se a URL está presente nos parâmetros
        if not url:
            return "URL não fornecida", 400

        # Construir a nova URL modificada
        base_url = url.rsplit('/', 1)[0]
        video_id = url.split('/')[-1]
        new_url = f"{base_url}/f/{video_id}_x"

        # Redirecionar para a nova URL
        return redirect(new_url, code=302)
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
  

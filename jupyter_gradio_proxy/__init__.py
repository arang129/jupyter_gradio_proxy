import os

def setup_gradio_proxy():
    """ Proxy wrapper to launch Streamlit from JupyterHub """

    return {
        'command': [
            "python", "run", "/home/jupyter-data/webapp/gradio/gradio_app.py",
        ],
        'port':7860,
        'absolute_url': False,
        'timeout': 60,
        'launcher_entry': {
            'enabled': True,
            'title': 'Gradio',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'gradio.svg'),
        }
    }

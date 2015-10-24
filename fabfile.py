from fabric.api import *
import os
import sys
import SimpleHTTPServer
import SocketServer

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'

# Remote server configuration
env.hosts = ['nagasaki45@nagasaki45.com']
site_names = {
        'en': 'www.galilee-bedouin-camplodge.com',
        'heb': 'www.shevet-ahim.co.il',
}

# Rackspace Cloud Files configuration settings
env.cloudfiles_username = 'my_rackspace_username'
env.cloudfiles_api_key = 'my_rackspace_api_key'
env.cloudfiles_container = 'my_cloudfiles_container'


def clean():
    if os.path.isdir(env.deploy_path):
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))

def build(language='en', regenerate=False, publish_conf=False):
    css_dir_by_language(language)()
    cmd = ['pelican -t theme']
    if regenerate:
        cmd.append('-r')
    conf = 'publishconf_{}.py' if publish_conf else 'pelicanconf_{}.py'
    cmd += ['-s', conf.format(language)]
    local(' '.join(cmd))

def build_dependencies():
    local('pip install -r requirements.txt')
    local('npm install -g rtlcss')
    local('git clone --recursive https://github.com/getpelican/pelican-plugins')

def rtlcss():
    local('rtlcss -d theme/static/css_source theme/static/css')
    local('rename rtl\.css css theme/static/css/*')

def ltrcss():
    local('cp -r theme/static/css_source theme/static/css')

def css_dir_by_language(language):
    if language == 'en':
        return ltrcss
    if language == 'he':
        return rtlcss

def rebuild(language='en'):
    clean()
    build(language=language)

def regenerate(language='en'):
    build(language=language, regenerate=True)

def serve():
    os.chdir(env.deploy_path)

    PORT = 8000
    class AddressReuseTCPServer(SocketServer.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT), SimpleHTTPServer.SimpleHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()

def reserve(language='en'):
    build(language=language)
    serve()

def preview(language='en'):
    build(language=language, publish_conf=True)

def cf_upload(language='en'):
    rebuild(language=language)
    local('cd {deploy_path} && '
          'swift -v -A https://auth.api.rackspacecloud.com/v1.0 '
          '-U {cloudfiles_username} '
          '-K {cloudfiles_api_key} '
          'upload -c {cloudfiles_container} .'.format(**env))

def publish(language='en'):
    build(language=language, publish_conf=True)
    dest_path = '/home/nagasaki45/sites/{}/'.format(site_names[language])
    put(env.deploy_path, dest_path)

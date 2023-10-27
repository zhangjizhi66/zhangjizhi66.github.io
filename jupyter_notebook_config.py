import os
if 'JSROOTSYS' in os.environ:
    # Let use localy installed JSROOT as THttpServer does
    c.NotebookApp.extra_static_paths.append(os.environ['JSROOTSYS'])
    c.ServerApp.extra_static_paths.append(os.environ['JSROOTSYS'])
elif 'ROOTSYS' in os.environ:
    # By default use JSROOT from ROOTSYS if defined
    c.NotebookApp.extra_static_paths.append(os.path.join(os.environ['ROOTSYS'], 'js/'))
    c.ServerApp.extra_static_paths.append(os.path.join(os.environ['ROOTSYS'], 'js/'))
else:
    # Fall back to CMAKE_INSTALL_PREFIX/CMAKE_INSTALL_JSROOTDIR, e.g., for a system installation
    c.NotebookApp.extra_static_paths.append(os.path.join("/opt/ROOT/root62402", "js"))
    c.ServerApp.extra_static_paths.append(os.path.join("/opt/ROOT/root62402", "js"))

c.NotebookApp.password='argon2:$argon2id$v=19$m=10240,t=10,p=8$wzgFSz5HLoQoZ4utevsoig$QSViVjOM44ndK+N9+R03wuGxOINE3De8c7ptBxA5Lqo'
c.NotebookApp.port=8888
c.NotebookApp.ip='162.105.54.147'
c.NotebookApp.allow_remote_access=True
c.NotebookApp.open_browser=False
# c.NotebookApp.notebook_dir=''

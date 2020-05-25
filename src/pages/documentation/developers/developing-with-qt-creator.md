---
id: qtcreator
title: Developing with QtCreator
---

In order to develop with nymea and modify its code, it is advised to open the code using QtCreator. For 
that, select the repository to be modified and follow those steps:

1. Open QtCreator and click on *File* -> *Open file or project*

2. Navigate to the `.pro` file of the wanted project and open it.

3. In the next step, choose the wanted build kit. Unless you have special requirements, the default *Desktop* kit will do.

4. Press the *Build* button on the bottom left of the QtCreator window (<kbd>Ctrl</kbd> + <kbd>b</kbd>) and follow the build process in the *Compile output* section (<kbd>Alt</kbd> + <kbd>4</kbd>).

5. Before you can run the fresh compiled *nymea* binary, you need to export the library path to the libnymea and libnymea-core, otherwise you will get following message:
    ```bash
    $ nymead: error while loading shared libraries: libnymea.so.1: cannot open shared object file: No such file or directory
    ```

    In order to export the lib path, you can run following command in the terminal:
    > **Note:** customize the path `PATH_TO_NYMEA` to your nymea folder!

    ```bash
    $ export LD_LIBRARY_PATH=LD_LIBRARY_PATH:/PATH_TO_NYMEA/build-nymea-Desktop-Debug/libnymea/:PATH_TO_NYMEA/build-nymea-Desktop-Debug/libnymea-core/
    ```

    To make it permanent, you can add this line to the `/etc/bash.bashrc` file.

6. Now you should be able to run *nymead* by pressing the *Play* button in the QtCreator (or you can press <kbd>Ctrl</kbd> + <kbd>r</kbd>). You can follow the stdout in the *Application Output* section (<kbd>Alt</kbd> + <kbd>3</kbd>).

    If you want to run the application in the terminal you can start *nymead* with following command:
    ```bash
    $ cd build-nymea-Desktop-Debug/server/
    $ ./nymead -n
    ```



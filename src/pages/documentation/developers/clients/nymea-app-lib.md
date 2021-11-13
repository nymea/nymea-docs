---
id: nymea-app-lib
title: C++/Qt/QML
---

## nymea:app

nymea:app, while being a client application, is structured in a way that it provides a Qt library that wraps the 
entire [JSONRPC API](raw-api) in a Qt like fashion. It can be used in C++ projects as well as imported in a QML app
to have all nymea features available in QML.

## Building the library

Building the nymea:app library is no different than building nymea:app itself. Building should be possible on pretty
much every platform supported by Qt. Currrently the app is built and released officially for those platforms:

* Linux Desktop
* Windows Desktop
* macOS Desktop
* Android
* iOS
* Ubuntu Phone

### Prerequisites

At first, Qt needs to be installed. The minimum Qt version for nymea:app is 5.9. Qt6 is not yet supported.

The recommended way to install Qt for nymea:app is to use the Qt online installer from [qt.io](http://qt.io). The required modules
are:

* Qt base for the target plaform
* Qt Charts
* Qt Virtual Keyboard
* Qt WebEngine

![Wizard](/img/qt-installer-app.png)


#### Android extras

If building for Android, the Qt base for Android component needs to be selected in the Qt install wizard. In addition to that, the android SDK
and NDK need to be installed. Please refer to the upstream [Qt for android documentation](https://doc.qt.io/qt-5/android.html) for more details.

#### iOS/macOS extras

Building nymea:app for iOS or macOS requires to select the iOS or macOS components in the Qt install wizard. In addition to that it is required
to have XCode installed. Please refer to the upstrea [Qt for iOS](https://doc.qt.io/qt-5/ios.html) and [Qt for macOS](https://doc.qt.io/qt-5/macos.html) documentations for more details.

### Building

The first step is to obtain the code:

```bash
git clone https://github.com/nymea/nymea-app.git
cd nymea-app
git submodule update --init
```

The preferred way of building is using QtCreator by opening nymea-app.pro and clicking the build button. It is also possible to build 
without QtCreator using the usual build steps.

This requires to have Qt installed and the `qmake` binary added to the PATH variable.

```bash
qmake /path/to/nymea-app/
make
```

This will build the entire nymea:app. The library can be found in the build directory in libnymea-app. By default it will be built as a static library named
`libnymea-app.a`.

## Using the library

There is no API documentation for libnymea-app at this point yet. We recommend looking at nymea:app's QML files for examples on how to interact with the lib.

### Using it in C++/Qt

Using the library requires to add the source directory to the inlcude path and adding the library to the linker flags.

Depending on the build system used this might differ.

For example, using it in a qmake project would require something like this:

```bash
INCLUDEPATH += /path/to/nymea-app/libnymea-app
LIBS += -L/path/to/nymea-app-build/libnymea-app -lnymea-app
```

Please refer to your build system's documentation on how to add include paths and libraries. In the end, the added flags must be

```bash
-I/path/to/nymea-app/libnymea-app
```
for the compiler, and

```bash
-L/path/to/nymea-app-build/libnymea-app -lnymea-app
```

for the linker.

### Making it available in QML

In order to register all the types in QML, include the libnymea-app-core.h file in your c++ application loader and call `registerQmlTypes()`. 

```c++
#include <libnymea-app-core.h>

...
void main() {
    ....
    registerQmlTypes();

    QQmlApplicationEngine *engine = new QQmlApplicationEngine();
    engine->load(QUrl(QLatin1String("MyQmlApp.qml")));

    ...
}
```

After that, `Nymea 1.0` can be imported in QML files.


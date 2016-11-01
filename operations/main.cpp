#include "operations.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Operations w;
    w.show();

    return a.exec();
}

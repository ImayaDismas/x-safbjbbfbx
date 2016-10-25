#ifndef SETUP_H
#define SETUP_H

#include <QMainWindow>

namespace Ui {
class Setup;
}

class Setup : public QMainWindow
{
    Q_OBJECT

public:
    explicit Setup(QWidget *parent = 0);
    ~Setup();

private:
    Ui::Setup *ui;
};

#endif // SETUP_H

#ifndef OPERATIONS_H
#define OPERATIONS_H

#include <QMainWindow>

namespace Ui {
class Operations;
}

class Operations : public QMainWindow
{
    Q_OBJECT

public:
    explicit Operations(QWidget *parent = 0);
    ~Operations();

private:
    Ui::Operations *ui;
};

#endif // OPERATIONS_H

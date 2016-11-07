#ifndef IMAGE_H
#define IMAGE_H

#include <QMainWindow>

namespace Ui {
class Image;
}

class Image : public QMainWindow
{
    Q_OBJECT

public:
    explicit Image(QWidget *parent = 0);
    ~Image();

private:
    Ui::Image *ui;
};

#endif // IMAGE_H

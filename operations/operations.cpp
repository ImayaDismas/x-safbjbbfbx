#include "operations.h"
#include "ui_operations.h"

Operations::Operations(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::Operations)
{
    ui->setupUi(this);
}

Operations::~Operations()
{
    delete ui;
}

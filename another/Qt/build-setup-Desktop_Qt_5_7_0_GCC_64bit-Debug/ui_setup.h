/********************************************************************************
** Form generated from reading UI file 'setup.ui'
**
** Created by: Qt User Interface Compiler version 5.7.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_SETUP_H
#define UI_SETUP_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QGraphicsView>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListView>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTextBrowser>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Setup
{
public:
    QWidget *centralWidget;
    QGridLayout *gridLayout;
    QLineEdit *lineEdit;
    QPushButton *pushButton_8;
    QPushButton *pushButton;
    QListWidget *listWidget;
    QGraphicsView *graphicsView;
    QLabel *label;
    QLineEdit *lineEdit_2;
    QLabel *label_2;
    QLineEdit *lineEdit_3;
    QPushButton *pushButton_2;
    QTextBrowser *textBrowser;
    QPushButton *pushButton_3;
    QPushButton *pushButton_4;
    QPushButton *pushButton_5;
    QListView *listView;
    QPushButton *pushButton_6;
    QPushButton *pushButton_7;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *Setup)
    {
        if (Setup->objectName().isEmpty())
            Setup->setObjectName(QStringLiteral("Setup"));
        Setup->resize(1200, 510);
        centralWidget = new QWidget(Setup);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        gridLayout = new QGridLayout(centralWidget);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        lineEdit = new QLineEdit(centralWidget);
        lineEdit->setObjectName(QStringLiteral("lineEdit"));

        gridLayout->addWidget(lineEdit, 0, 0, 1, 1);

        pushButton_8 = new QPushButton(centralWidget);
        pushButton_8->setObjectName(QStringLiteral("pushButton_8"));

        gridLayout->addWidget(pushButton_8, 0, 1, 1, 1);

        pushButton = new QPushButton(centralWidget);
        pushButton->setObjectName(QStringLiteral("pushButton"));

        gridLayout->addWidget(pushButton, 0, 2, 1, 1);

        listWidget = new QListWidget(centralWidget);
        listWidget->setObjectName(QStringLiteral("listWidget"));

        gridLayout->addWidget(listWidget, 1, 0, 7, 2);

        graphicsView = new QGraphicsView(centralWidget);
        graphicsView->setObjectName(QStringLiteral("graphicsView"));

        gridLayout->addWidget(graphicsView, 1, 2, 5, 1);

        label = new QLabel(centralWidget);
        label->setObjectName(QStringLiteral("label"));

        gridLayout->addWidget(label, 1, 3, 1, 1);

        lineEdit_2 = new QLineEdit(centralWidget);
        lineEdit_2->setObjectName(QStringLiteral("lineEdit_2"));

        gridLayout->addWidget(lineEdit_2, 1, 4, 1, 2);

        label_2 = new QLabel(centralWidget);
        label_2->setObjectName(QStringLiteral("label_2"));

        gridLayout->addWidget(label_2, 2, 3, 1, 1);

        lineEdit_3 = new QLineEdit(centralWidget);
        lineEdit_3->setObjectName(QStringLiteral("lineEdit_3"));

        gridLayout->addWidget(lineEdit_3, 2, 4, 1, 2);

        pushButton_2 = new QPushButton(centralWidget);
        pushButton_2->setObjectName(QStringLiteral("pushButton_2"));

        gridLayout->addWidget(pushButton_2, 3, 3, 1, 2);

        textBrowser = new QTextBrowser(centralWidget);
        textBrowser->setObjectName(QStringLiteral("textBrowser"));

        gridLayout->addWidget(textBrowser, 3, 5, 3, 1);

        pushButton_3 = new QPushButton(centralWidget);
        pushButton_3->setObjectName(QStringLiteral("pushButton_3"));

        gridLayout->addWidget(pushButton_3, 4, 3, 1, 2);

        pushButton_4 = new QPushButton(centralWidget);
        pushButton_4->setObjectName(QStringLiteral("pushButton_4"));

        gridLayout->addWidget(pushButton_4, 5, 3, 1, 2);

        pushButton_5 = new QPushButton(centralWidget);
        pushButton_5->setObjectName(QStringLiteral("pushButton_5"));

        gridLayout->addWidget(pushButton_5, 6, 2, 1, 1);

        listView = new QListView(centralWidget);
        listView->setObjectName(QStringLiteral("listView"));

        gridLayout->addWidget(listView, 6, 3, 3, 3);

        pushButton_6 = new QPushButton(centralWidget);
        pushButton_6->setObjectName(QStringLiteral("pushButton_6"));

        gridLayout->addWidget(pushButton_6, 7, 2, 1, 1);

        pushButton_7 = new QPushButton(centralWidget);
        pushButton_7->setObjectName(QStringLiteral("pushButton_7"));

        gridLayout->addWidget(pushButton_7, 8, 2, 1, 1);

        Setup->setCentralWidget(centralWidget);
        statusBar = new QStatusBar(Setup);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        Setup->setStatusBar(statusBar);

        retranslateUi(Setup);

        QMetaObject::connectSlotsByName(Setup);
    } // setupUi

    void retranslateUi(QMainWindow *Setup)
    {
        Setup->setWindowTitle(QApplication::translate("Setup", "Setup", 0));
        pushButton_8->setText(QApplication::translate("Setup", "Search", 0));
        pushButton->setText(QApplication::translate("Setup", "ADD", 0));
        label->setText(QApplication::translate("Setup", "Name", 0));
        label_2->setText(QApplication::translate("Setup", "Group", 0));
        pushButton_2->setText(QApplication::translate("Setup", "Bio", 0));
        pushButton_3->setText(QApplication::translate("Setup", "Network ID", 0));
        pushButton_4->setText(QApplication::translate("Setup", "Notes", 0));
        pushButton_5->setText(QApplication::translate("Setup", "Operations", 0));
        pushButton_6->setText(QApplication::translate("Setup", "Calls", 0));
        pushButton_7->setText(QApplication::translate("Setup", "Sms", 0));
    } // retranslateUi

};

namespace Ui {
    class Setup: public Ui_Setup {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_SETUP_H

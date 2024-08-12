#ifndef HAVOCCLIENT_HCPAGELISTENER_H
#define HAVOCCLIENT_HCPAGELISTENER_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QSplitter>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QTableWidget>
#include <QtWidgets/QWidget>
#include <QtWidgets/QTextEdit>

QT_BEGIN_NAMESPACE

class HcListenerItem : public QWidget
{
public:
    QGridLayout* GridLayout  = {};
    QLabel*      LabelStatus = {};

    explicit HcListenerItem( QWidget* parent = nullptr );
    explicit HcListenerItem(
        const QString& text,
        QWidget*       parent = nullptr
    );

    auto setStatus(
        const QString& string
    ) const -> void;
};

typedef struct {
    QTableWidgetItem* Name;
    QTableWidgetItem* Type;
    QTableWidgetItem* Host;
    QTableWidgetItem* Port;
    HcListenerItem*   Status;

    QTextEdit*        Logger;

    auto stop() -> std::optional<std::string>;
    auto start() -> std::optional<std::string>;
    auto restart() -> std::optional<std::string>;
    auto edit() -> std::optional<std::string>;
} HcListener;

class HcPageListener : public QWidget
{
    bool SplitterMoveToggle = false;
    int  ListenersRunning   = 0;

    std::vector<HcListener*> TableEntries  = {};

public:
    QGridLayout*      gridLayout        = nullptr;
    QLabel*           ActiveLabel       = nullptr;
    QSpacerItem*      horizontalSpacer  = nullptr;
    QPushButton*      ButtonNewListener = nullptr;
    QSplitter*        Splitter          = nullptr;
    QTableWidget*     TableWidget       = nullptr;
    QTabWidget*       TabWidget         = nullptr;
    QTableWidgetItem* TitleName         = nullptr;
    QTableWidgetItem* TitleType         = nullptr;
    QTableWidgetItem* TitleHost         = nullptr;
    QTableWidgetItem* TitlePort         = nullptr;
    QTableWidgetItem* TitleStatus       = nullptr;
    std::vector<json> Protocols         = {};
    std::vector<json> Listeners         = {};

    explicit HcPageListener();
    auto retranslateUi() -> void;

    auto addListener(
        const json& data
    ) -> void;

    auto addListenerLog(
        const std::string& name,
        const std::string& log
    ) -> void;

    auto setListenerStatus(
        const std::string& name,
        const std::string& status
    ) -> void;

    auto updateListenersRunningLabel(
        int value
    ) const -> void;

    auto handleListenerContextMenu(
        const QPoint& pos
    ) -> void;

    auto tabCloseRequested(
        int index
    ) const -> void;

    auto buttonAddListener() -> void;
};

QT_END_NAMESPACE

#endif //HAVOCCLIENT_HCPAGELISTENER_H
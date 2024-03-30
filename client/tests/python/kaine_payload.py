import pyhavoc

import PySide6
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import time
import base64
import argparse

from os.path import exists
from struct import pack, calcsize

KAINE_COMMANDS: list = []

@pyhavoc.ui.HcUiBuilderRegisterView( "Kaine" )
class HcKaineBuilder( pyhavoc.ui.HcPayloadView ):

    def __init__( self, *args, **kwargs ):
        super().__init__( *args, **kwargs )

    ##
    ## main function to be executed
    ## should create the widgets inputs
    ## for the payload builder
    ##
    def main( self, widget: QWidget ):

        self.gridLayout = QGridLayout( widget )
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins( 0, 0, 0, 0 )

        self.ScrollAreaStack = QScrollArea( widget )
        self.ScrollAreaStack.setObjectName(u"ScrollAreaStack")
        self.ScrollAreaStack.setWidgetResizable(True)

        self.ScrollAreaWidget = QWidget()
        self.ScrollAreaWidget.setObjectName(u"ScrollAreaWidget")
        self.ScrollAreaWidget.setProperty( "HcWidgetDark", "true" )

        self.gridLayout_5 = QGridLayout(self.ScrollAreaWidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")

        self.GridLayoutHeader = QGridLayout()
        self.GridLayoutHeader.setObjectName(u"GridLayoutHeader")
        self.GridLayoutHeader.setSizeConstraint(QLayout.SetDefaultConstraint)

        self.ComboListener = QComboBox(self.ScrollAreaWidget)
        self.ComboListener.setObjectName(u"ComboListener")

        self.GridLayoutHeader.addWidget(self.ComboListener, 0, 1, 1, 1)

        self.LabelArch = QLabel(self.ScrollAreaWidget)
        self.LabelArch.setObjectName(u"LabelArch")

        self.GridLayoutHeader.addWidget(self.LabelArch, 1, 0, 1, 1)

        self.ComboArch = QComboBox(self.ScrollAreaWidget)
        self.ComboArch.setObjectName(u"ComboArch")

        self.GridLayoutHeader.addWidget(self.ComboArch, 1, 1, 1, 1)

        self.LabelListener = QLabel(self.ScrollAreaWidget)
        self.LabelListener.setObjectName(u"LabelListener")

        self.GridLayoutHeader.addWidget(self.LabelListener, 0, 0, 1, 1)

        self.LabelFormat = QLabel(self.ScrollAreaWidget)
        self.LabelFormat.setObjectName(u"LabelFormat")

        self.GridLayoutHeader.addWidget(self.LabelFormat, 2, 0, 1, 1)

        self.ComboFormat = QComboBox(self.ScrollAreaWidget)
        self.ComboFormat.setObjectName(u"ComboFormat")

        self.GridLayoutHeader.addWidget(self.ComboFormat, 2, 1, 1, 1)

        self.GridLayoutHeader.setColumnStretch(1, 1)

        self.gridLayout_5.addLayout(self.GridLayoutHeader, 0, 0, 1, 2)

        self.GroupCoreSettings = QGroupBox(self.ScrollAreaWidget)
        self.GroupCoreSettings.setObjectName(u"GroupCoreSettings")
        self.gridLayout_3 = QGridLayout(self.GroupCoreSettings)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.LabelKillDate = QLabel(self.GroupCoreSettings)
        self.LabelKillDate.setObjectName(u"LabelKillDate")

        self.gridLayout_3.addWidget(self.LabelKillDate, 0, 0, 1, 1)

        self.LabelStackSpoofing = QLabel(self.GroupCoreSettings)
        self.LabelStackSpoofing.setObjectName(u"LabelStackSpoofing")

        self.gridLayout_3.addWidget(self.LabelStackSpoofing, 3, 0, 1, 1)

        self.GroupSleepObf = QGroupBox(self.GroupCoreSettings)
        self.GroupSleepObf.setObjectName(u"GroupSleepObf")
        self.gridLayout_7 = QGridLayout(self.GroupSleepObf)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.GridLayoutSleepObf = QGridLayout()
        self.GridLayoutSleepObf.setObjectName(u"GridLayoutSleepObf")
        self.LabelSleepObfJmpGadget = QLabel(self.GroupSleepObf)
        self.LabelSleepObfJmpGadget.setObjectName(u"LabelSleepObfJmpGadget")

        self.GridLayoutSleepObf.addWidget(self.LabelSleepObfJmpGadget, 1, 0, 1, 1)

        self.LabelEncryption = QLabel(self.GroupSleepObf)
        self.LabelEncryption.setObjectName(u"LabelEncryption")

        self.GridLayoutSleepObf.addWidget(self.LabelEncryption, 2, 0, 1, 1)

        self.LabelSleepObfTechnique = QLabel(self.GroupSleepObf)
        self.LabelSleepObfTechnique.setObjectName(u"LabelSleepObfTechnique")

        self.GridLayoutSleepObf.addWidget(self.LabelSleepObfTechnique, 0, 0, 1, 1)

        self.CheckHeapEncryption = QCheckBox(self.GroupSleepObf)
        self.CheckHeapEncryption.setObjectName(u"CheckHeapEncryption")

        self.GridLayoutSleepObf.addWidget(self.CheckHeapEncryption, 4, 0, 1, 3)

        self.CheckStackDuplication = QCheckBox(self.GroupSleepObf)
        self.CheckStackDuplication.setObjectName(u"CheckStackDuplication")

        self.GridLayoutSleepObf.addWidget(self.CheckStackDuplication, 3, 0, 1, 3)

        self.ComboEncryption = QComboBox(self.GroupSleepObf)
        self.ComboEncryption.setObjectName(u"ComboEncryption")

        self.GridLayoutSleepObf.addWidget(self.ComboEncryption, 2, 1, 1, 2)

        self.ComboSleepObfJmpGadget = QComboBox(self.GroupSleepObf)
        self.ComboSleepObfJmpGadget.setObjectName(u"ComboSleepObfJmpGadget")

        self.GridLayoutSleepObf.addWidget(self.ComboSleepObfJmpGadget, 1, 1, 1, 2)

        self.ComboSleepObfTechnique = QComboBox(self.GroupSleepObf)
        self.ComboSleepObfTechnique.setObjectName(u"ComboSleepObfTechnique")

        self.GridLayoutSleepObf.addWidget(self.ComboSleepObfTechnique, 0, 1, 1, 2)

        self.GridLayoutSleepObf.setColumnStretch(1, 1)

        self.gridLayout_7.addLayout(self.GridLayoutSleepObf, 0, 0, 1, 1)

        self.VSpacerSleepObf = QSpacerItem(0, 3, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.VSpacerSleepObf, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.GroupSleepObf, 9, 0, 1, 3)

        self.InputModuleStomp = QLineEdit(self.GroupCoreSettings)
        self.InputModuleStomp.setObjectName(u"InputModuleStomp")

        self.gridLayout_3.addWidget(self.InputModuleStomp, 6, 1, 1, 2)

        self.InputSleep = QLineEdit(self.GroupCoreSettings)
        self.InputSleep.setObjectName(u"InputSleep")
        self.InputSleep.setValidator( QIntValidator() )

        self.gridLayout_3.addWidget(self.InputSleep, 1, 1, 1, 2)

        self.CheckKillDate = QCheckBox(self.GroupCoreSettings)
        self.CheckKillDate.setObjectName(u"CheckKillDate")

        self.gridLayout_3.addWidget(self.CheckKillDate, 0, 2, 1, 1)

        self.LabelAntiShellcode = QLabel(self.GroupCoreSettings)
        self.LabelAntiShellcode.setObjectName(u"LabelAntiShellcode")

        self.gridLayout_3.addWidget(self.LabelAntiShellcode, 4, 0, 1, 1)

        self.ComboAntiShellcode = QComboBox(self.GroupCoreSettings)
        self.ComboAntiShellcode.setObjectName(u"ComboAntiShellcode")

        self.gridLayout_3.addWidget(self.ComboAntiShellcode, 4, 1, 1, 2)

        self.LabelModuleLoad = QLabel(self.GroupCoreSettings)
        self.LabelModuleLoad.setObjectName(u"LabelModuleLoad")

        self.gridLayout_3.addWidget(self.LabelModuleLoad, 5, 0, 1, 1)

        self.InputJitter = QLineEdit(self.GroupCoreSettings)
        self.InputJitter.setObjectName(u"InputJitter")
        self.InputJitter.setValidator( QIntValidator( 0, 100 ) )

        self.gridLayout_3.addWidget(self.InputJitter, 2, 1, 1, 2)

        self.CheckModuleRndOrder = QCheckBox(self.GroupCoreSettings)
        self.CheckModuleRndOrder.setObjectName(u"CheckModuleRndOrder")

        self.gridLayout_3.addWidget(self.CheckModuleRndOrder, 8, 0, 1, 3)

        self.LabelModuleStomp = QLabel(self.GroupCoreSettings)
        self.LabelModuleStomp.setObjectName(u"LabelModuleStomp")

        self.gridLayout_3.addWidget(self.LabelModuleStomp, 6, 0, 1, 1)

        self.DateTimeKillDate = QDateTimeEdit( self.GroupCoreSettings )
        self.DateTimeKillDate.setObjectName( u"DateTimeKillDate" )
        self.DateTimeKillDate.setTimeSpec( PySide6.QtCore.Qt.TimeSpec.LocalTime )
        self.DateTimeKillDate.setCalendarPopup( True )
        self.DateTimeKillDate.setDateTime( PySide6.QtCore.QDateTime.currentDateTime() )
        self.DateTimeKillDate.setDisplayFormat("dd-MMM-yyyy hh:mm:00")

        self.gridLayout_3.addWidget(self.DateTimeKillDate, 0, 1, 1, 1)

        self.LabelSleep = QLabel(self.GroupCoreSettings)
        self.LabelSleep.setObjectName(u"LabelSleep")

        self.gridLayout_3.addWidget(self.LabelSleep, 1, 0, 1, 1)

        self.ComboStackSpoofing = QComboBox(self.GroupCoreSettings)
        self.ComboStackSpoofing.setObjectName(u"ComboStackSpoofing")

        self.gridLayout_3.addWidget(self.ComboStackSpoofing, 3, 1, 1, 2)

        self.ComboModuleLoad = QComboBox(self.GroupCoreSettings)
        self.ComboModuleLoad.setObjectName(u"ComboModuleLoad")

        self.gridLayout_3.addWidget(self.ComboModuleLoad, 5, 1, 1, 2)

        self.LabelJitter = QLabel(self.GroupCoreSettings)
        self.LabelJitter.setObjectName(u"LabelJitter")

        self.gridLayout_3.addWidget(self.LabelJitter, 2, 0, 1, 1)

        self.CheckIndirectSyscall = QCheckBox(self.GroupCoreSettings)
        self.CheckIndirectSyscall.setObjectName(u"CheckIndirectSyscall")

        self.gridLayout_3.addWidget(self.CheckIndirectSyscall, 7, 0, 1, 1)

        self.InputIndirectSyscall = QLineEdit(self.GroupCoreSettings)
        self.InputIndirectSyscall.setObjectName(u"InputIndirectSyscall")

        self.gridLayout_3.addWidget(self.InputIndirectSyscall, 7, 1, 1, 2)

        self.gridLayout_5.addWidget(self.GroupCoreSettings, 1, 0, 1, 2)

        self.GroupExecuteable = QGroupBox(self.ScrollAreaWidget)
        self.GroupExecuteable.setObjectName(u"GroupExecuteable")

        self.gridLayout_5.addWidget(self.GroupExecuteable, 0, 2, 2, 2)

        self.ScrollAreaStack.setWidget(self.ScrollAreaWidget)

        self.gridLayout.addWidget(self.ScrollAreaStack, 0, 0, 1, 1)

        self.LabelArch.setText(QCoreApplication.translate("KaineBuilder", u"Arch: ", None))
        self.LabelListener.setText(QCoreApplication.translate("KaineBuilder", u"Listener: ", None))
        self.LabelFormat.setText(QCoreApplication.translate("KaineBuilder", u"Format: ", None))
        self.GroupCoreSettings.setTitle(QCoreApplication.translate("KaineBuilder", u"Core Settings", None))
        self.LabelKillDate.setText(QCoreApplication.translate("KaineBuilder", u"Kill Date: ", None))
        self.LabelStackSpoofing.setText(QCoreApplication.translate("KaineBuilder", u"Stack Spoofing: ", None))
        self.GroupSleepObf.setTitle(QCoreApplication.translate("KaineBuilder", u"Sleep Obfuscation", None))
        self.LabelSleepObfJmpGadget.setText(QCoreApplication.translate("KaineBuilder", u"Jmp Gadget: ", None))
        self.LabelEncryption.setText(QCoreApplication.translate("KaineBuilder", u"Encryption:", None))
        self.LabelSleepObfTechnique.setText(QCoreApplication.translate("KaineBuilder", u"Technique: ", None))
        self.CheckHeapEncryption.setText(QCoreApplication.translate("KaineBuilder", u"Heap Encryption", None))
        self.CheckStackDuplication.setText(QCoreApplication.translate("KaineBuilder", u"Stack Duplication", None))
        self.CheckKillDate.setText(QCoreApplication.translate("KaineBuilder", u"Enable Killdate", None))
        self.LabelAntiShellcode.setText(QCoreApplication.translate("KaineBuilder", u"Anti-Shellcode mitigation: ", None))
        self.LabelModuleLoad.setText(QCoreApplication.translate("KaineBuilder", u"Module load technique: ", None))
        self.CheckModuleRndOrder.setText(QCoreApplication.translate("KaineBuilder", u"Module random load order", None))
        self.LabelModuleStomp.setText(QCoreApplication.translate("KaineBuilder", u"Module Stomp (Plugin): ", None))
        self.LabelSleep.setText(QCoreApplication.translate("KaineBuilder", u"Sleep: ", None))
        self.LabelJitter.setText(QCoreApplication.translate("KaineBuilder", u"Jitter (%): ", None))
        self.CheckIndirectSyscall.setText(QCoreApplication.translate("KaineBuilder", u"Indirect Syscall", None))
        self.GroupExecuteable.setTitle(QCoreApplication.translate("KaineBuilder", u"Executable:", None))

        QMetaObject.connectSlotsByName( widget )

        self.set_defaults()

        return

    ##
    ## refresh the widget based on following things:
    ##  - new listener started
    ##  - new script loaded
    ##  - new agent connected
    ##
    def refresh( self ) -> None:
        self.set_defaults()

    def set_defaults(self) -> None:

        self.ComboListener.clear()
        listeners = pyhavoc.core.HcListenerAll()
        if len( listeners ) == 0:
            self.ComboListener.addItem( "(no listener available)" )
            self.ComboListener.setEnabled( False )
        else:
            for i in listeners:
                self.ComboListener.addItem( i )

        self.ComboArch.clear()
        self.ComboArch.addItem( "x64" )
        self.ComboArch.addItem( "x86" )

        self.ComboFormat.clear()
        self.ComboFormat.addItem( "Windows Exe" )
        self.ComboFormat.addItem( "Windows Dll" )
        self.ComboFormat.addItem( "Windows Service Exe" )
        self.ComboFormat.addItem( "Windows Shellcode" )
        self.ComboFormat.addItem( "Windows VBS" )
        self.ComboFormat.addItem( "Windows PS1" )

        self.InputSleep.setText( "5" )
        self.InputJitter.setText( "10" )

        self.ComboStackSpoofing.clear()
        self.ComboStackSpoofing.addItem( "None" )
        self.ComboStackSpoofing.addItem( "Synthetic Frames" )

        self.ComboAntiShellcode.clear()
        self.ComboAntiShellcode.addItem( "None" )
        self.ComboAntiShellcode.addItem( "mov rax, [rax]" )

        self.ComboModuleLoad.clear()
        self.ComboModuleLoad.addItem( "LdrLoadDll" )
        self.ComboModuleLoad.addItem( "RtlRegisterWait( LoadLibraryW )" )
        self.ComboModuleLoad.addItem( "RtlCreateTimer( LoadLibraryW )" )
        self.ComboModuleLoad.addItem( "RtlQueueWorkItem( LoadLibraryW )" )
        self.ComboModuleLoad.addItem( "TpAllocWork( LoadLibraryW )" )
        self.ComboModuleLoad.addItem( "NtMapViewOfSection" )
        self.ComboModuleLoad.addItem( "NtAllocateVirtualMemory" )

        self.InputIndirectSyscall.setText( "NtAddBootEntry" )

        self.ComboSleepObfTechnique.clear()
        self.ComboSleepObfTechnique.addItem( "Ekko" )
        self.ComboSleepObfTechnique.addItem( "Zilean" )
        self.ComboSleepObfTechnique.addItem( "Foliage" )

        self.ComboSleepObfJmpGadget.clear()
        self.ComboSleepObfJmpGadget.addItem( "None" )
        self.ComboSleepObfJmpGadget.addItem( "jmp rax" )
        self.ComboSleepObfJmpGadget.addItem( "jmp rbx" )

        self.ComboEncryption.clear()
        self.ComboEncryption.addItem( "SystemFunction032 (RC4)" )
        self.ComboEncryption.addItem( "SystemFunction040 (3DES)" )

        return

    ##
    ## sanity check the given input
    ## return:
    ##  true  -> successful checked the input and nothing is wrong
    ##  false -> failed to check and something went wrong
    ##
    def sanity_check( self ) -> bool:
        return True

    ##
    ## pressing "Generate" action or
    ## while saving a profile
    ##
    def generate( self ) -> dict:

        config: dict = {
            "Listener": self.ComboListener.currentText(),
            "Arch"    : self.ComboArch.currentText(),
            "Format"  : self.ComboFormat.currentText(),

            "Core": {
                "Sleep"  : self.InputSleep.text(),
                "Jitter" : self.InputJitter.text(),
            }
        }

        if self.CheckKillDate.isChecked() :
            config[ "Core" ][ "Kill Date" ] = self.DateTimeKillDate.dateTime()

        return config

    ##
    ## pressing "Save Profile" action
    ##
    def profile_save( self ) -> dict:
        pass

    ##
    ## pressing "Load Profile" action
    ##
    def profile_load( self, profile: dict ) -> bool:
        pass

    ##
    ## payload has been generated
    ##
    def payload( self, payload: bytes ) -> None:
        pass

class HcKaineCommand:
    pass

class HcTableDict( dict ):

    def __init__( self, kaine_agent ):
        super( HcTableDict, self ).__init__()
        self.kaine = kaine_agent

    def __setitem__(self, key, item):
        print( f"HcTableDict.__setitem__( {key}, {item} ) " )
        self.kaine.key_set( key, item )

    def __getitem__(self, key):
        print( f"HcTableDict.__getitem__( {key} ) " )
        return self.kaine.key_get( key )

    def __repr__(self):
        print( f"HcTableDict.__repr__() " )

    def __len__(self):
        print( f"HcTableDict.__len__() " )

    def __delitem__(self, key):
        print( f"HcTableDict.__delitem__( {key} ) " )
        self.kaine.key_delete( key )

    def clear(self):
        print( f"HcTableDict.clear() " )
        pass

    def copy(self):
        print( f"HcTableDict.copy()" )
        pass

    def has_key(self, key):
        print( f"HcTableDict.has_key( {key} ) " )
        return self.kaine.key_exist( key )

    def update(self, *args, **kwargs):
        print( f"HcTableDict.update( {args}, {kwargs} ) " )
        pass

    def keys(self):
        print( f"HcTableDict.keys() " )
        pass

    def values(self):
        print( f"HcTableDict.keys() " )
        pass

    def items(self):
        print( f"HcTableDict.items() " )
        pass

    def pop(self, *args):
        pass

    def __cmp__(self, dict_):
        print( f"HcTableDict.__cmp__( {dict_} ) " )
        pass

    def __contains__(self, item):
        return self.kaine.key_exist( item )

    def __iter__(self):
        print( f"HcTableDict.__iter__()" )
        pass

    def __unicode__(self):
        print( f"HcTableDict.__unicode__()" )
        pass


@pyhavoc.agent.HcAgentRegisterInterface( "Kaine" )
class HcKaine( pyhavoc.agent.HcAgent ):

    def __init__( self, *args, **kwargs ):
        super().__init__( *args, **kwargs )

        self.key_store = HcTableDict( self )

        return

    def console_error( self, text ):
        self.console_print( "%x[%D %T]%$ %r[-]%$ " + text )
        return

    def console_log( self, text, type="info" ):
        self.agent_execute( {
            "command": "KnConsole",
            "arguments": {
                "type"   : type,
                "output" : text
            }
        }, True )

        return

    def console_input( self, text, local_only=False ):
        if local_only is True:
            self.console_print( "" )
            self.console_print( "%x[%D %T]%$ %pKaine%$ %c>>>%$ " + text )
        else:
            self.agent_execute( {
                "command": "KnConsole",
                "arguments": {
                    "type"   : "input",
                    "output" : text
                }
            }, True )

        return

    def input_dispatch( self, input: str ):
        ##
        ## setup available commands
        ##
        commands       = input.split()
        kaine_commands = []

        for KnTaskObject in KAINE_COMMANDS:
            kaine_commands.append( KnTaskObject( self ) )

        if commands[ 0 ].lower() == "help":
            largest_name_length = 0

            self.console_print( "" )
            self.console_print( "%x[%D %T]%$ %pKaine%$ %c>>>%$ " + input )
            self.console_print( "" )
            self.console_print( " Kaine Commands" )
            self.console_print( " ==============" )
            self.console_print( "" )

            ##
            ## find the largest command name
            ##
            for i in kaine_commands:
                if len(i.command) >= largest_name_length:
                    largest_name_length = len(i.command)

            self.console_print( f"   Command{' ' * (largest_name_length - 7)}   Description" )
            self.console_print( f"   -------{' ' * (largest_name_length - 7)}   -----------" )

            for i in kaine_commands:
                self.console_print( f"   {i.command + ' ' * (largest_name_length - len(i.command))}   {i.description}" )

            self.console_print( "" )
        else:
            found = False

            for i in kaine_commands:
                if commands[ 0 ] == i.command:
                    self.console_input( input )
                    i.execute( commands[ 1: ] )
                    found = True

            if found is False:
                self.console_input( input, local_only=True )
                self.console_error( f"invalid command: {input}" )

        return

    def key_get( self, key: str ) -> any:
        return self.agent_execute( {
            "command"   : "KnStoreGet",
            "arguments" : {
                "key": key
            },
        }, True )[ 'result' ]

    def key_set( self, key: str, val: any ) -> any:
        self.agent_execute( {
            "command"   : "KnStoreSet",
            "arguments" : {
                "key"   : key,
                "value" : val
            },
        }, True )

    def key_exist( self, key: str ) -> bool:
        return self.agent_execute( {
            "command"   : "KnStoreExist",
            "arguments" : {
                "key"   : key,
            },
        }, True )[ 'result' ]

    def key_delete( self, key: str ) -> None:
        self.agent_execute( {
            "command"   : "KnStoreDelete",
            "arguments" : {
                "key"   : key,
            },
        }, True )

    def task_generate(
        self,
    ) -> int:
        ##
        ## try to generate task uuid
        ##
        resp = self.agent_execute( {
            "command": "KnTaskGenerate"
        }, True )

        return resp[ 'task-uuid' ]

    def task_delete(
        self,
        task_uuid: int
    ) -> bool:

        ##
        ## try to generate task uuid
        ##
        resp = self.agent_execute( {
            "command": "KnTaskDelete",
            "arguments": {
                "task-uuid": task_uuid
            }
        }, True )

        return resp[ 'success' ]

    def object_free(
        self,
        handle         : int,
        wait_to_finish : bool = False,
        task_uuid      : int  = 0,
    ) -> dict:
        return self.agent_execute( {
            "command":   "IoObjectControl",
            "arguments": {
                "object"   : handle,
                "free"     : True,
                "task-uuid": task_uuid
            }
        }, wait_to_finish )

    def object_execute(
        self,
        object        : any,
        entry         : str   = "go",
        parameters    : any   = None,
        is_module     : bool  = False,
        base_address  : int   = 0,
        wait_to_finish: bool  = False,
        task_uuid     : int   = 0,
    ) -> dict:
        """
        execute an object file in memory

        :param object:
            object file bytes to load and execute in memory
            or object file handle that already has been loaded
            into memory

        :param entry:
             entry point function name to execute after
             loading the object file into memory

        :param parameters:
            arguments to pass to the entry point function

        :param is_module:
            if this argument is set to true then the object file
            won't be released from memory and is going to return
            the handle/address of the object file for further
            function invocation.
            be aware that if this flag is specified it is going
            to block the current execution and wait til the file
            has been loaded into memory to return the handle.

        :param base_address:
            base address of where to write the object file to.
            can be ann address from a stomped module or virtual
            private memory.

        :param wait_to_finish:
            wait til the execution of the bof finished

        :param task_uuid
            tasking id to use for the execution of the object file

        :return:
            status of executing the object file
        """

        wait: bool = wait_to_finish
        resp: dict = {}
        obj : any  = None

        ##
        ## we have to wait til we receive back the
        ## handle of the object file in memory
        ##
        if is_module:
           wait = True

        if type( object ) == bytes:
            obj = base64.b64encode( object ).decode( 'utf-8' )
        elif type( object ) == int:
            obj = object
        else:
            return {
                "status": -1,
                "return": "object is not a byte array or handle"
            }

        ##
        ## task the agent to invoke an object file
        ##
        resp = self.agent_execute( {
                "command":   "IoObjectControl",
                "arguments": {
                    "object"   : obj,
                    "entry"    : entry,
                    "args"     : base64.b64encode( parameters ).decode( 'utf-8' ),
                    "module"   : is_module,
                    "address"  : base_address,
                    "task-uuid": task_uuid
                }
            },
            wait
        )

        ##
        ## if there is something to parse then
        ## lets parse it and return it
        ##
        if wait_to_finish is True:
            if "return" in resp:
                resp[ "return" ] = base64.b64decode( resp[ "return" ].encode( 'utf-8' ) )

        return resp

@pyhavoc.agent.HcAgentExport
class HcKaineCommand:

    def __init__( self, agent: HcKaine ):

        self.__agent = agent
        self.command = ""
        self.description = ""
        self.is_module  = False
        self.opsec_safe = True

        return

    def agent( self ) -> HcKaine:
        return self.__agent

    def help( self ):
        pass

    def execute( self, commands: str ):
        pass

@pyhavoc.agent.HcAgentExport
def HcKaineRegister( interface ):

    KAINE_COMMANDS.append( interface )

    return

class KnPacker:
    def __init__(self):
        self.buffer : bytes = b''
        self.size   : int   = 0

    def build( self ):
        return pack("<L", self.size) + self.buffer

    def add_string(self, s):
        if s is None:
            s = ''
        if isinstance(s, str):
            s = s.encode("utf-8" )
        fmt = "<L{}s".format(len(s) + 1)
        self.buffer += pack(fmt, len(s)+1, s)
        self.size   += calcsize(fmt)

    def add_wide_string(self, s):
        if s is None:
            s = ''
        s = s.encode("utf-16_le")
        fmt = "<L{}s".format(len(s) + 2)
        self.buffer += pack(fmt, len(s)+2, s)
        self.size   += calcsize(fmt)

    def add_bytes(self, b):
        if b is None:
            b = b''
        fmt = "<L{}s".format(len(b))
        self.buffer += pack(fmt, len(b), b)
        self.size   += calcsize(fmt)

    def add_u8(self, b):
        fmt = '<c'
        self.buffer += pack(fmt, b)
        self.size   += 1

    def add_u32(self, dint):
        self.buffer += pack("<i", dint)
        self.size   += 4

    def add_u16(self, n):
        fmt = '<h'
        self.buffer += pack(fmt, n)
        self.size   += 2

@pyhavoc.agent.HcAgentExport
class KnObjectModule:

    def __init__(
        self,
        agent      : HcKaine,
        object     : any,
        function   : str   = "",
        *args,
        data       : bytes = b'',
        obfuscate  : bool  = False,
        veh_dbg    : bool  = False
    ):
        self.__agent   = agent
        self.__object  = object
        self.__handle  = 0
        self.__status  = ""
        self.__error   = ""
        self.__uuid    = 0
        buffer         = b''
        packer         = KnPacker()

        ##
        ## check if the object parameter is an
        ## byte array to be loaded by the agent
        ##
        if type( object ) == bytes:

            if len(args) > 0:
                for i in args:
                    if type( i ) == int:
                        packer.add_u32( i )
                    elif type( i ) == str:
                        packer.add_string( i )
                    elif type( i ) == bytes:
                        packer.add_bytes( i )

                buffer = packer.build()

            if len(data) > 0:
                buffer = data

            ##
            ## task the kaine agent to
            ## load the object file into memory
            ##
            ctx = self.__agent.object_execute( self.__object, entry=function, parameters=buffer, is_module=True, wait_to_finish=True )
            self.__status = ctx[ 'status' ]
            self.__uuid   = ctx[ 'task-uuid' ]

            if ctx[ 'status' ] != "STATUS_SUCCESS":
                self.__error  = ctx[ 'return' ].decode( 'utf-8' )
            else:
                self.__handle = ctx[ 'handle' ]
        else:
            self.__handle = object
            self.__status = 'STATUS_SUCCESS'

        return

    def uuid( self ) -> int:
        return self.__uuid

    def handle( self ) -> int:
        return self.__handle

    def error( self ) -> str:
        return self.__error

    def status( self ) -> str:
        return self.__status

    def invoke( self, function, *args, data=b'' ) -> dict:
        packer = KnPacker()
        buffer: bytes    = b''

        if self.status() != 'STATUS_SUCCESS':
            return {
                "error": self.error()
            }

        if len(args) > 0:

            for i in args:
                if type( i ) == int:
                    packer.add_u32( i )
                elif type( i ) == str:
                    packer.add_string( i )
                elif type( i ) == bytes:
                    packer.add_bytes( i )

            buffer = packer.build()

        if len(data) > 0:
            buffer = data
        
        ctx = self.__agent.object_execute( object=self.handle(), parameters=buffer, entry=function, wait_to_finish=True )

        if 'task-uuid' in ctx:
            self.__uuid = ctx[ 'task-uuid' ]

        return ctx

    def free( self ):
        return self.__agent.object_free( self.handle(), wait_to_finish=True )


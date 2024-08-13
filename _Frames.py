import customtkinter as ctk
from utils import fonts


def dash(self):
    """Dashboard widget"""
    self.clear_frame()
    self.bt_from_frame1 = ctk.CTkButton(
        self.frame, text="dash", command=lambda: print("test dash")
    )
    self.bt_from_frame1.grid(row=0, column=0, padx=20, pady=(10, 0))
    self.bt_from_frame2 = ctk.CTkButton(
        self.frame, text="dash 1", command=lambda: print("test dash 1")
    )
    self.bt_from_frame2.grid(row=1, column=0, padx=20, pady=(10, 0))


#  self.frame   ----> statement widget


def mqtt_setup(self):
    """MQTT Setup Widget"""
    self.clear_frame()
    ctk.CTkLabel(self.frame, text="Host", font=fonts.label).place(x=20, y=50)
    hostEntry = ctk.CTkEntry(
        self.frame, placeholder_text="Host", font=fonts.entry, width=300
    )
    hostEntry.place(x=20, y=80)

    ctk.CTkLabel(self.frame, text="Port", font=fonts.label).place(x=420, y=50)
    portEntry = ctk.CTkEntry(
        self.frame, placeholder_text="Port", font=fonts.entry, width=200
    )
    portEntry.place(x=420, y=80)

    ctk.CTkLabel(self.frame, text="Username",
                 font=fonts.label).place(x=40, y=250)
    unameEntry = ctk.CTkEntry(
        self.frame, placeholder_text="Username", font=fonts.entry, width=300
    )
    unameEntry.place(x=40, y=280)

    ctk.CTkLabel(self.frame, text="Password",
                 font=fonts.label).place(x=40, y=350)
    pwEntry = ctk.CTkEntry(
        self.frame, placeholder_text="Password", font=fonts.entry, width=300
    )
    pwEntry.place(x=40, y=380)

    # Connect
    def connect_event():
        print(f"Connect to {hostEntry.get()}:{portEntry.get()}")

    ctk.CTkButton(
        self.frame, text="Connect", font=fonts.button, command=connect_event
    ).place(relx=0.32, rely=0.90)


#  self.frame   ----> categories widget


def categories(self):
    """Categories Management Widget"""
    self.clear_frame()
    self.bt_from_frame4 = ctk.CTkButton(
        self.frame, text="categories", command=lambda: print("test cats")
    )
    self.bt_from_frame4.grid(row=0, column=0, padx=20, pady=(10, 0))


#   self.frame ----> GS config
def radio_config(self):
    """Ground Station Configuration Widget"""
    print("GS Config")
    self.clear_frame()

    # Frame Title
    ctk.CTkLabel(self.frame, text="Radio Config",
                 font=fonts.header).pack()

    # FREQUENCY
    freqLabel = ctk.CTkLabel(self.frame, text="Frequency", font=fonts.label)
    freqLabel.place(x=10, y=50)

    freqEntry = ctk.CTkEntry(
        self.frame, placeholder_text="Enter frequency", font=fonts.entry
    )
    freqEntry.place(x=150, y=50)

    freqCombo = ctk.CTkComboBox(self.frame, values=["Hz", "MHz"], width=70)
    freqCombo.place(x=300, y=50)

    # BANDWIDTH
    bwLabel = ctk.CTkLabel(self.frame, text="Bandwidth", font=fonts.label)
    bwLabel.place(x=10, y=100)
    """
    bwEntry = ctk.CTkEntry(
        self.frame, placeholder_text="Enter bandwidth", font=fonts.entry
    )
    bwEntry.place(x=150, y=100)

    bwCombo = ctk.CTkComboBox(self.frame, values=["Hz", "kHz"], width=70)
    bwCombo.place(x=300, y=100)
    """
    bwopts = {
        "7.8 kHz": 7800,
        "10.4 kHz": 10400,
        "15.6 kHz": 15600,
        "20.8 kHz": 20800,
        "31.2 kHz": 31250,
        "41.7 kHz": 41700,
        "62.5 kHz": 62500,
        "125 kHz": 125000,
        "250 kHz": 250000,
    }

    bwOption = ctk.CTkOptionMenu(
        self.frame,
        values=list(bwopts.keys()),
    )
    bwOption.place(x=150, y=100)

    # Spreading Factor
    def sfCallback(value):
        print("segmented button clicked:", value)

    ctk.CTkLabel(self.frame, text="Spreading Factor", font=fonts.label).place(
        x=10, y=200
    )
    sfSegmented = ctk.CTkSegmentedButton(
        self.frame, values=range(7, 12 + 1), command=sfCallback
    )
    sfSegmented.set("Value 1")
    sfSegmented.place(x=200, y=200)

    # CHECKSUM
    def chksumEvent():
        print("CHEKSUM: ", has_chksum.get())

    ctk.CTkLabel(self.frame, text="Checksum",
                 font=fonts.label).place(x=10, y=300)
    has_chksum = ctk.StringVar(value=True)
    chksumSwitch = ctk.CTkSwitch(
        self.frame,
        text="",
        command=chksumEvent,
        variable=has_chksum,
        onvalue=True,
        offvalue=False,
    )
    chksumSwitch.place(x=150, y=300)

    # SUBMIT
    def button_event():
        value, unit = (float(freqEntry.get()), freqCombo.get())
        freqval = value * 1e6 if unit == "MHz" else value
        print(value, unit, " -> ", freqval)

        value = bwopts[bwOption.get()]
        print(value)

    button = ctk.CTkButton(
        self.frame, text="Submit", font=fonts.button, command=button_event
    )
    button.place(relx=0.32, rely=0.90)


# ===================================================
# Change scaling of all widget 80% to 120%
def change_scaling_event(new_scaling):
    new_scaling_float = int(new_scaling.replace("%", "")) / 100
    ctk.set_widget_scaling(new_scaling_float)


def view(self):
    """edit UI"""
    self.clear_frame()
    self.scaling_label = ctk.CTkLabel(
        self.frame, text="UI Scaling:", anchor="w")
    self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))

    self.scaling_optionemenu = ctk.CTkOptionMenu(
        self.frame,
        values=["80%", "90%", "100%", "110%", "120%"],
        command=change_scaling_event,
    )
    self.scaling_optionemenu.grid(
        row=8, column=0, padx=20, pady=(10, 20), sticky="s")
    # TODO: Change theme

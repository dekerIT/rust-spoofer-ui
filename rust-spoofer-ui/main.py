
import customtkinter as ctk
from PIL import Image
from pathlib import Path


# ================= CONFIG =================

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")


class RustSpoofer(ctk.CTk):

    BG = "#101113"
    SIDEBAR = "#151618"
    CARD = "#1b1d20"
    CARD_HOVER = "#242629"

    RED = "#c83b32"
    RED_HOVER = "#a92e27"

    WHITE = "#f4f4f4"
    GRAY = "#92969d"
    GREEN = "#65c477"
    BORDER = "#292b2f"

    def __init__(self):
        super().__init__()

        self.title("Rust Spoofer")
        self.geometry("1000x620+200+120")
        self.minsize(850, 540)

        self.configure(fg_color=self.BG)

        self.demo = False

        self.load_logo()
        self.build_interface()

    # ================= LOGO =================

    def load_logo(self):
        path = Path(__file__).with_name("rust_logo.png")

        self.logo = None

        if path.exists():
            image = Image.open(path).convert("RGBA")
            image.thumbnail((430, 115), Image.Resampling.LANCZOS)

            self.logo = ctk.CTkImage(
                light_image=image,
                dark_image=image,
                size=image.size
            )

    # ================= MAIN UI =================

    def build_interface(self):

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.create_sidebar()
        self.create_dashboard()

    # ================= SIDEBAR =================

    def create_sidebar(self):

        sidebar = ctk.CTkFrame(
            self,
            width=215,
            corner_radius=0,
            fg_color=self.SIDEBAR
        )

        sidebar.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        sidebar.grid_propagate(False)

        # App identity

        brand = ctk.CTkFrame(
            sidebar,
            fg_color="transparent"
        )
        brand.pack(
            fill="x",
            padx=22,
            pady=(28, 35)
        )

        ctk.CTkLabel(
            brand,
            text="RUST",
            font=("Arial Black", 27),
            text_color=self.WHITE
        ).pack(anchor="w")

        ctk.CTkLabel(
            brand,
            text="SPOOFER",
            font=("Segoe UI", 10, "bold"),
            text_color=self.RED
        ).pack(anchor="w")

        # Navigation

        ctk.CTkLabel(
            sidebar,
            text="MAIN MENU",
            font=("Segoe UI", 10, "bold"),
            text_color=self.GRAY
        ).pack(
            anchor="w",
            padx=22,
            pady=(0, 12)
        )

        self.nav_button(
            sidebar,
            "◈    Dashboard",
            True
        )

        self.nav_button(
            sidebar,
            "⚙    Settings",
            False
        )

        self.nav_button(
            sidebar,
            "ⓘ    About",
            False
        )

        # Bottom section

        bottom = ctk.CTkFrame(
            sidebar,
            fg_color="transparent"
        )
        bottom.pack(
            side="bottom",
            fill="x",
            padx=20,
            pady=22
        )

        ctk.CTkFrame(
            bottom,
            height=1,
            fg_color=self.BORDER
        ).pack(fill="x", pady=(0, 16))

        ctk.CTkLabel(
            bottom,
            text="APPLICATION VERSION",
            font=("Segoe UI", 9, "bold"),
            text_color=self.GRAY
        ).pack(anchor="w")

        ctk.CTkLabel(
            bottom,
            text="Rust Spoofer v1.0",
            font=("Segoe UI", 12),
            text_color=self.WHITE
        ).pack(anchor="w", pady=(4, 0))

    def nav_button(self, parent, text, active):

        button = ctk.CTkButton(
            parent,
            text=text,
            anchor="w",
            height=43,
            corner_radius=8,
            fg_color="#30201f" if active else "transparent",
            hover_color=self.CARD_HOVER,
            text_color=self.WHITE if active else self.GRAY,
            font=("Segoe UI", 12, "bold" if active else "normal"),
            command=lambda: None
        )

        button.pack(
            fill="x",
            padx=12,
            pady=3
        )

    # ================= DASHBOARD =================

    def create_dashboard(self):

        main = ctk.CTkFrame(
            self,
            fg_color=self.BG,
            corner_radius=0
        )

        main.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=30,
            pady=25
        )

        main.grid_columnconfigure(0, weight=1)

        # Top header

        top = ctk.CTkFrame(
            main,
            fg_color="transparent"
        )
        top.grid(
            row=0,
            column=0,
            sticky="ew",
            pady=(0, 28)
        )

        ctk.CTkLabel(
            top,
            text="Dashboard",
            font=("Segoe UI", 27, "bold"),
            text_color=self.WHITE
        ).pack(side="left")

        ctk.CTkLabel(
            top,
            text="●  APPLICATION READY",
            text_color=self.GREEN,
            font=("Segoe UI", 10, "bold")
        ).pack(
            side="right",
            pady=10
        )

        # Welcome card

        hero = ctk.CTkFrame(
            main,
            fg_color=self.CARD,
            corner_radius=14,
            border_width=1,
            border_color=self.BORDER
        )

        hero.grid(
            row=1,
            column=0,
            sticky="ew",
            pady=(0, 18)
        )

        hero.grid_columnconfigure(0, weight=1)

        hero_content = ctk.CTkFrame(
            hero,
            fg_color="transparent"
        )
        hero_content.pack(
            fill="x",
            padx=25,
            pady=24
        )

        ctk.CTkLabel(
            hero_content,
            text="WELCOME BACK",
            font=("Segoe UI", 10, "bold"),
            text_color=self.RED
        ).pack(anchor="w")

        ctk.CTkLabel(
            hero_content,
            text="Rust Spoofer",
            font=("Segoe UI", 28, "bold"),
            text_color=self.WHITE
        ).pack(anchor="w", pady=(5, 3))

        ctk.CTkLabel(
            hero_content,
            text="Your application dashboard.",
            font=("Segoe UI", 12),
            text_color=self.GRAY
        ).pack(anchor="w")

        if self.logo:
            logo_label = ctk.CTkLabel(
                hero_content,
                text="",
                image=self.logo
            )
            logo_label.pack(
                anchor="w",
                pady=(17, 0)
            )

        # Status cards

        cards = ctk.CTkFrame(
            main,
            fg_color="transparent"
        )

        cards.grid(
            row=2,
            column=0,
            sticky="ew",
            pady=(0, 18)
        )

        cards.grid_columnconfigure((0, 1), weight=1)

        self.create_status_card(
            cards,
            "APPLICATION STATUS",
            "●  Ready",
            self.GREEN,
            0
        )

        self.create_status_card(
            cards,
            "HWID STATUS",
            "Not spoofed",
            self.GRAY,
            1
        )

        # Action section

        action = ctk.CTkFrame(
            main,
            fg_color=self.CARD,
            corner_radius=14,
            border_width=1,
            border_color=self.BORDER
        )

        action.grid(
            row=3,
            column=0,
            sticky="ew",
            pady=(0, 18)
        )

        action_content = ctk.CTkFrame(
            action,
            fg_color="transparent"
        )
        action_content.pack(
            fill="x",
            padx=22,
            pady=20
        )

        ctk.CTkLabel(
            action_content,
            text="QUICK ACTION",
            font=("Segoe UI", 10, "bold"),
            text_color=self.GRAY
        ).pack(anchor="w")

        ctk.CTkLabel(
            action_content,
            text="HWID Spoofer",
            font=("Segoe UI", 19, "bold"),
            text_color=self.WHITE
        ).pack(anchor="w", pady=(5, 3))

        ctk.CTkLabel(
            action_content,
            text="Demonstration interface only.",
            font=("Segoe UI", 11),
            text_color=self.GRAY
        ).pack(anchor="w", pady=(0, 15))

        self.action_button = ctk.CTkButton(
            action_content,
            text="Spoof HWID",
            height=46,
            corner_radius=9,
            fg_color=self.RED,
            hover_color=self.RED_HOVER,
            text_color=self.WHITE,
            font=("Segoe UI", 14, "bold"),
            command=self.demo_action
        )

        self.action_button.pack(
            fill="x"
        )

        # Footer

        footer = ctk.CTkFrame(
            main,
            fg_color="transparent"
        )

        footer.grid(
            row=4,
            column=0,
            sticky="ew"
        )

        ctk.CTkLabel(
            footer,
            text="Rust Spoofer  •  Version 1.0",
            font=("Segoe UI", 10),
            text_color=self.GRAY
        ).pack(side="left")

        ctk.CTkLabel(
            footer,
            text="DEMO BUILD",
            font=("Segoe UI", 10, "bold"),
            text_color=self.RED
        ).pack(side="right")

    # ================= STATUS CARDS =================

    def create_status_card(
        self,
        parent,
        title,
        value,
        color,
        column
    ):

        card = ctk.CTkFrame(
            parent,
            fg_color=self.CARD,
            corner_radius=12,
            border_width=1,
            border_color=self.BORDER
        )

        card.grid(
            row=0,
            column=column,
            sticky="ew",
            padx=(0, 8) if column == 0 else (8, 0)
        )

        ctk.CTkLabel(
            card,
            text=title,
            font=("Segoe UI", 9, "bold"),
            text_color=self.GRAY
        ).pack(
            anchor="w",
            padx=17,
            pady=(15, 5)
        )

        label = ctk.CTkLabel(
            card,
            text=value,
            font=("Segoe UI", 17, "bold"),
            text_color=color
        )

        label.pack(
            anchor="w",
            padx=17,
            pady=(0, 16)
        )

        if title == "HWID STATUS":
            self.hwid_card_label = label

    # ================= DEMO ACTION =================

    def demo_action(self):

        self.demo = not self.demo

        if self.demo:

            self.action_button.configure(
                text="Demo activated",
                fg_color="#355d3c",
                hover_color="#416d48"
            )

            self.hwid_card_label.configure(
                text="Demo only",
                text_color=self.GREEN
            )

        else:

            self.action_button.configure(
                text="Spoof HWID",
                fg_color=self.RED,
                hover_color=self.RED_HOVER
            )

            self.hwid_card_label.configure(
                text="Not spoofed",
                text_color=self.GRAY
            )


if __name__ == "__main__":
    app = RustSpoofer()
    app.mainloop()


import keyboard
import time
import vgamepad as vg

gamepad = vg.VDS4Gamepad()


stratagems = {
    "machine gun": "dldur",
    "anti-materiel rifle": "dlrud",
    "stalwart": "dlduul",
    "expendable anti-tank": "ddlur",
    "recoilless rifle": "dlrrl",
    "flamethrower": "dludu",
    "autocannon": "dlduur",
    "railgun": "drldulr",
    "spear": "ddudd",
    "gatling barrage": "rdluu",
    "airburst strike": "rrr",
    "120mmhe barrage": "rdlrd",
    "380mmhe barrage": "rduuld",
    "walking barrage": "rrdlrd",
    "laser": "rdurd",
    "railcannon strike": "ruddr",
    "strafing run": "urr",
    "airstrike": "urdr",
    "clusterbomb": "urddr",
    "napalm airstrike": "urdu",
    "jump pack": "duudu",
    "smoke strike": "urud",
    "110mm rocket pods": "urul",
    "500kg bomb": "urddd",
    "precision strike": "rru",
    "gas strike": "rrdr",
    "ems strike": "rrld",
    "smoke strike": "rrdu",
    "hmg emplacement": "dulrrl",
    "shield generator relay": "duldrr",
    "tesla tower": "durulr",
    "anti-personnel minefield": "dlur",
    "supply pack": "dlduud",
    "grenade launcher": "dluld",
    "laser cannon": "dldul",
    "incendiary mines": "dllud",
    "guard dog rover": "dulurrd",
    "ballistic shield": "dluuu",
    "arc thrower": "druld",
    "shield generator pack": "dulrlr",
    "machine gun sentry": "durru",
    "gatling sentry": "durl",
    "mortar sentry": "durrd",
    "guard dog": "dulurd",
    "auto cannon sentry": "durulu",
    "rocket sentry": "durrll",
    "ems mortar sentry": "dduul",
    "sos beacon": "udlu",
    "resupply": "ddur",
    "reinforce": "udrlu",
    "hellbomb": "duldurdu"
}


keys_translate = {
    "d": vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_SOUTH,
    "l": vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_WEST,
    "r": vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_EAST,
    "u": vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_NORTH
} 

hotkeys = {
    "0": "reinforce",
    ".": "laser",
    ",": "380mmhe barrage",
    "/": "laser cannon",
    "'": "resupply",
    "\\": "hellbomb",
    "]": "clusterbomb"
}

sleepy_time = 0.05

def on_key_event(e):

    if e.name in hotkeys:
        if e.event_type == "down":
            print(f"{hotkeys[e.name]} hotkey pressed.")
            gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_LEFT)
            gamepad.update()
            time.sleep(sleepy_time)
            k = stratagems[hotkeys[e.name]]
            for i in range(len(k)):
                gamepad.directional_pad(direction=keys_translate[k[i]])
                gamepad.update()
                time.sleep(sleepy_time)
                print(keys_translate[k[i]])
                gamepad.directional_pad(vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_NONE)
                gamepad.update()
                time.sleep(sleepy_time)
            gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_LEFT)
            gamepad.update()
            gamepad.reset()


# Set up the listener
keyboard.hook(on_key_event)

# Keep the program running
keyboard.wait('9')  # Wait for the 'esc' key to exit the program
